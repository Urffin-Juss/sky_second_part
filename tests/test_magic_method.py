import pytest
from Product import Product
from Category import Category


def test_product_str():
    p = Product("Хлеб", "Пшеничный", 80, 15)
    # __str__ должен вернуть строку строго в этом формате
    assert str(p) == "Хлеб, 80 руб. Остаток: 15 шт."


def test_product_add_two_products():
    a = Product("Товар A", "desc", 100, 10)  # 1000
    b = Product("Товар B", "desc", 200, 2)   # 400
    total = a + b
    assert total == 1400


def test_product_add_wrong_type():
    a = Product("Товар A", "desc", 100, 1)
    with pytest.raises(TypeError):
        _ = a + 5  # нельзя складывать с не-Product

def test_category_str():
    p1 = Product("Хлеб", "Пшеничный", 50, 10)
    p2 = Product("Молоко", "3.2%", 80, 5)

    cat = Category("Продукты", "Еда", [p1, p2])

    # суммарное количество = 10 + 5 = 15
    assert str(cat) == "Продукты, количество продуктов: 15 шт."


def test_category_products_property_uses_product_str():
    """Проверяем, что геттер products теперь отдаёт строки из __str__ продукта."""
    p1 = Product("Хлеб", "Пшеничный", 50, 10)
    cat = Category("Продукты", "Еда", [p1])

    products_view = cat.products
    assert len(products_view) == 1
    assert products_view[0] == "Хлеб, 50 руб. Остаток: 10 шт."
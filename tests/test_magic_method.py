import pytest
from Product import Product
from Category import Category
from Smartphone import Smartphone


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


def test_add_product_allows_product():
    Category.category_count = 0
    Category.product_count = 0

    p = Product("Хлеб", "Пшеничный", 50, 10)
    cat = Category("Продукты", "Еда", [])

    cat.add_product(p)

    # через property products возвращаются строки
    assert len(cat.products) == 1
    assert "Хлеб" in cat.products[0]
    assert Category.product_count == 1


def test_add_product_rejects_other_types():
    """Если передать не Product и не наследника — должна быть ошибка."""
    cat = Category("Продукты", "Еда", [])

    with pytest.raises(TypeError):
        cat.add_product("я не продукт")  # type: ignore


def test_add_product_allows_product_subclasses():
    """Должно пускать наследников Product (Smartphone, LawnGrass и т.п.)."""
    Category.category_count = 0
    Category.product_count = 0

    phone = Smartphone(
        name="iPhone 15",
        description="Флагман",
        price=120000,
        quantity=2,
        efficiency="high",
        model="A3100",
        memory=256,
        color="black",
    )

    cat = Category("Электроника", "Гаджеты", [])
    cat.add_product(phone)

    assert len(cat.products) == 1
    assert "iPhone 15" in cat.products[0]
    # счётчик тоже должен обновиться
    assert Category.product_count == 1

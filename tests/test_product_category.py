import pytest
from src.Product import Product
from src.Category import Category


def test_product_init():
    p = Product("Хлеб", "Пшеничный", 50, 10)

    assert p.name == "Хлеб"
    assert p.description == "Пшеничный"
    assert p.price == 50
    assert p.quantity == 10


def test_category_init_counts():
    # обнулим счётчики, чтобы тест был повторяемый
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("Хлеб", "Пшеничный", 50, 10)
    p2 = Product("Молоко", "3.2%", 80, 5)

    c1 = Category("Продукты", "Базовые", [p1, p2])

    assert c1.name == "Продукты"
    assert c1.description == "Базовые"
    assert len(c1.products) == 2

    # проверяем атрибуты КЛАССА
    assert Category.category_count == 1
    assert Category.product_count == 2

    # создадим ещё одну категорию
    c2 = Category("Бытовая химия", "Для дома", [])

    assert Category.category_count == 2
    assert Category.product_count == 2  # товаров во второй нет


def test_product_price_setter_valid():
    p = Product("Хлеб", "Пшеничный", 50, 10)

    p.price = 120

    assert p.price == 60


def test_product_price_setter_invalid(capsys):
    p = Product("Хлеб", "Пшеничный", 50, 10)

    # пробуем поставить ноль
    p.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    # цена не изменилась
    assert p.price == 50

    # пробуем отрицательную
    old_price = p.price; p.price = -10; assert p.price == old_price
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    # цена опять не изменилась
    assert p.price == 50


def test_category_init_and_class_counters():
    # обнулим, чтобы тест был повторяемый
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("Хлеб", "Пшеничный", 50, 10)
    p2 = Product("Молоко", "3.2%", 80, 5)

    cat = Category("Продукты", "Еда", [p1, p2])

    assert cat.name == "Продукты"
    assert cat.description == "Еда"

    # проверяем, что счётчики класса обновились
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_add_product():
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("Хлеб", "Пшеничный", 50, 10)
    cat = Category("Продукты", "Еда", [p1])

    p2 = Product("Молоко", "3.2%", 80, 5)
    cat.add_product(p2)

    # приватный список мы напрямую не трогаем — проверяем через property
    products_strings = cat.products
    assert len(products_strings) == 2
    assert "Молоко" in products_strings[1]

    # счётчик класса тоже должен увеличиться
    assert Category.product_count == 2


def test_category_add_product_only_product():
    cat = Category("Пустая", "test", [])

    # передаём что-то, что не Product — должно упасть
    with pytest.raises(TypeError):
        cat.add_product("не продукт")  # type: ignore


def test_category_products_property_format():
    p1 = Product("Хлеб", "Пшеничный", 50, 10)
    p2 = Product("Молоко", "3.2%", 80, 5)

    cat = Category("Продукты", "Еда", [p1, p2])

    # Теперь products возвращает объекты
    assert len(cat.products) == 2
    assert hasattr(cat.products[0], 'name')
    assert hasattr(cat.products[0], 'price')
    assert cat.products[0].name == "Хлеб"
    assert cat.products[1].name == "Молоко"

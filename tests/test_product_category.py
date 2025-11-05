# tests/test_product_category.py

from Product import Product
from Category import Category


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

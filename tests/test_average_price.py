import pytest
from src.Product import Product
from src.Category import Category


def test_average_price_with_products():
    """Тест: средняя цена рассчитывается правильно когда есть товары"""
    p1 = Product("Товар 1", "Описание", 100, 5)
    p2 = Product("Товар 2", "Описание", 200, 3)
    p3 = Product("Товар 3", "Описание", 300, 2)

    cat = Category("Тест", "Описание", [p1, p2, p3])

    # Средняя цена: (100 + 200 + 300) / 3 = 200
    assert cat.average_price() == 200.0


def test_average_price_with_one_product():
    """Тест: средняя цена с одним товаром"""
    p1 = Product("Товар 1", "Описание", 150, 1)
    cat = Category("Тест", "Описание", [p1])

    assert cat.average_price() == 150.0


def test_average_price_empty_category():
    """Тест: средняя цена возвращает 0 когда нет товаров"""
    cat = Category("Пустая категория", "Описание", [])

    assert cat.average_price() == 0.0


def test_average_price_after_adding_products():
    """Тест: средняя цена пересчитывается после добавления товаров"""
    cat = Category("Тест", "Описание", [])
    assert cat.average_price() == 0.0  # Пустая категория

    p1 = Product("Товар 1", "Описание", 100, 1)
    cat.add_product(p1)
    assert cat.average_price() == 100.0  # Один товар

    p2 = Product("Товар 2", "Описание", 300, 1)
    cat.add_product(p2)
    assert cat.average_price() == 200.0  # Два товара: (100 + 300) / 2 = 200
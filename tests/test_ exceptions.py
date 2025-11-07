import pytest
from src.Product import Product

def test_product_creation_with_zero_quantity_raises_error():
    """Тест: создание товара с нулевым количеством вызывает ValueError"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Тестовый товар", "Описание", 100, 0)

def test_product_creation_with_positive_quantity_works():
    """Тест: создание товара с положительным количеством работает нормально"""
    p = Product("Тестовый товар", "Описание", 100, 5)
    assert p.quantity == 5
    assert p.name == "Тестовый товар"

def test_new_product_with_zero_quantity_raises_error():
    """Тест: метод new_product с нулевым количеством вызывает ValueError"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product.new_product({
            "name": "Тестовый товар",
            "description": "Описание",
            "price": 100,
            "quantity": 0
        })
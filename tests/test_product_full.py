import pytest

from src.Product import Product
from src.Smartphone import Smartphone
from src.LawnGrass import LawnGrass


def test_new_product_classmethod_and_str():
    data = {"name": "Молоко", "description": "3.2%", "price": 80, "quantity": 5}
    p = Product.new_product(data)
    assert isinstance(p, Product)
    assert p.name == "Молоко"
    assert str(p).startswith("Молоко")
    assert "80" in str(p)


def test_price_setter_valid_and_invalid(capsys):
    p = Product("Хлеб", "desc", 50, 10)
    p.price = 100
    assert p.price == 100

    p.price = 0  # invalid
    out = capsys.readouterr().out
    assert "Цена" in out or "не должна" in out
    assert p.price == 100  # unchanged

    p.price = -5
    out = capsys.readouterr().out
    assert "Цена" in out or "не должна" in out
    assert p.price == 100


def test_add_two_same_products_ok():
    a = Product("A", "d", 100, 2)  # 200
    b = Product("B", "d", 50, 3)   # 150
    assert a + b == 350


def test_add_wrong_type_raises():
    a = Product("A", "d", 10, 1)
    with pytest.raises(TypeError):
        _ = a + 5  # not Product


def test_add_different_subclasses_raises():
    phone = Smartphone("Phone", "d", 1000, 1, "high", "M", 64, "black")
    grass = LawnGrass("Grass", "d", 10, 10, "RU", 7, "green")
    with pytest.raises(TypeError):
        _ = phone + grass

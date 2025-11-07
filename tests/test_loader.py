import json

from src.Product import Product
from src.Category import Category
from src.load_json_func import load_categories_from_json


def test_load_categories_from_json(tmp_path):
    # обнулим счётчики классов, чтобы не влиял порядок других тестов
    Category.category_count = 0
    Category.product_count = 0

    data = [
        {
            "name": "Продукты",
            "description": "Базовые продукты питания",
            "products": [
                {
                    "name": "Хлеб",
                    "description": "Пшеничный",
                    "price": 50,
                    "quantity": 10
                },
                {
                    "name": "Молоко",
                    "description": "3.2%",
                    "price": 80,
                    "quantity": 5
                }
            ]
        },
        {
            "name": "Бытовая химия",
            "description": "Для дома",
            "products": []
        }
    ]

    json_path = tmp_path / "data.json"
    json_path.write_text(json.dumps(
        data, ensure_ascii=False), encoding="utf-8")

    categories = load_categories_from_json(str(json_path))

    # проверяем, что создались 2 категории
    assert hasattr(categories[0], 'name')
    assert hasattr(categories[0], 'description')
    assert hasattr(categories[0], 'products')

    # у первой категории 2 товара
    assert len(categories[0].products) == 2
    assert isinstance(categories[0].products[0], Product)
    assert categories[0].products[0].price == 50

    # класс-счётчики тоже должны обновиться
    assert Category.category_count == 2
    assert Category.product_count == 2  # в сумме по JSON было 2 товара

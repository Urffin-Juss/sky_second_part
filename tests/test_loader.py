import json
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

    # ДИАГНОСТИКА:
    print(f"categories[0] тип: {type(categories[0])}")
    print(f"categories[0]: {categories[0]}")
    print(f"categories[0].products тип: {type(categories[0].products)}")
    print(f"categories[0].products: {categories[0].products}")
    if categories[0].products:
        print(f"categories[0].products[0] тип: {type(categories[0].products[0])}")
        print(f"categories[0].products[0]: {categories[0].products[0]}")


    assert len(categories) == 2


    assert "Продукты" in categories[0]
    assert "Бытовая химия" in categories[1]


    if hasattr(categories[0], 'products'):
        assert len(categories[0].products) == 2
        assert "Хлеб" in categories[0].products[0]
        assert "50" in categories[0].products[0]  # цена
    else:

        assert "Хлеб" in categories[0]
        assert "50" in categories[0]
        assert "Молоко" in categories[0]
        assert "80" in categories[0]


    # assert Category.category_count == 2
    # assert Category.product_count == 2

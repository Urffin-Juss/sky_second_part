import json
from pathlib import Path

from Product import Product
from Category import Category


def load_categories_from_json(filepath: str = "data/data.json") -> list[Category]:
    """
        Читает JSON-файл и возвращает список объектов Category,
        внутри которых уже созданы объекты Product.
        """
    path = Path(filepath)

    with path.open(encoding=UTF-8) as f:
        raw_data = json.load(f)

    categories: list[Category] = []

    for cat_dict in raw_data:
        cat_name = cat_dict.get("name", "")
        cat_desc = cat_dict.get("description", "")
        products_data = cat_dict.get("products", [])

        product_objects: list[Product] = []
        for prod in products_data:
            p = Product(
                prod.get("name", ""),
                prod.get("description", ""),
                int(prod.get("price", 0)),
                int(prod.get("quantity", 0)),
            )
            product_objects.append(p)

        category_obj = Category(cat_name, cat_desc, product_objects)
        categories.append(category_obj)

    return categories

from Product import Product
from src.Base_Product import BaseProduct


class Category(BaseProduct):
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        super().__init__(name, 0)
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("В категорию можно добавлять только товары Product")

        # Просто добавляем товар в список
        self.__products.append(product)

    @property
    def products(self) -> list[Product]:
        return self.__products

    def __str__(self) -> str:
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def get_info(self):
        return f"Категория: {self.name}, количество продуктов: {len(self.products)}"

    def average_price(self) -> float:


        try:

            total_price = sum(product.price for product in self.__products)

            total_products = len(self.__products)

            return total_price / total_products
        except ZeroDivisionError:

            return 0

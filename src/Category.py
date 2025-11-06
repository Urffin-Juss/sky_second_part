from Product import Product


class Category:

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def product(self) -> list[str]:
        """
                Геттер для приватного списка товаров.
                Возвращает список строк в формате:
                'Название продукта, 80 руб. Остаток: 15 шт.'
                """

        return [
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            for p in self.__products
            ]

    def __str__(self) -> str:

        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт. "

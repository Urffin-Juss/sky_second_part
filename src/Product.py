class Product:

    def __init__(self, name: str, description: str, price: int, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> int:

        return self.__price

    @price.setter
    def price(self, value: int):

        if value <= 0:
            print("Цена должна быть больше ноля")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_data: dict):
        """
                Создаёт новый объект Product на основе данных из словаря.
                Пример product_data:
                {
                    "name": "Хлеб",
                    "description": "Пшеничный",
                    "price": 50,
                    "quantity": 10
                }
                """

        return cls(

            name=product_data.get("name", ""),
            description=product_data.get("description", ""),
            price=product_data.get("price", 0),
            quantity=product_data.get("quantity", 0),

        )

    def __str__(self) -> str:
        """Возвращает описание товара"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."
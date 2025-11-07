from Product import Product



class Smartphone(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: int,
        quantity: int,
        efficiency: str,
        model: str,
        memory: int,
        color: str,
    ):

        super().__init__(self, name, description, price, quantity)

        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self) -> str:

        base = super().__str__()
        return (f"{base} (смартфон {self.model}, {self.memory} "
                f"ГБ, цвет: {self.color})")

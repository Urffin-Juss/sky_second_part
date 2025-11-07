from Product import Product


class LawnGrass(Product):

    def __init__(
            self,
            name: str,
            description: str,
            price: int,
            quantity: int,
            country: str,
            germination_period: int,
            color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:

        base = super.__str__()
        return (
            f"{base} (газонная трава, страна: {self.country}, "
            f"прорастание: {self.germination_period} дн., цвет: {self.color})"
        )

    def get_info(self):
        """Возвращает информацию о газонной траве"""
        return f"{self.name} - {self.description}, страна: {self.country}"
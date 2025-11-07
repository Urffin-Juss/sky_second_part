from abc import ABC, abstractmethod


class BaseProduct(ABC):

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @abstractmethod
    def get_info(self):

        pass

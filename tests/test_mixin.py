from src.Product import Product
from src.Base_Product import BaseProduct
from src.LogCreationMixin import LogCreationMixin


def test_mixin_prints_on_creation(capsys):
    """
    Проверяем, что при создании объекта Product миксин печатает сообщение
    о создании с указанием имени класса и переданных параметров.
    """
    p = Product("Продукт1", "Описание продукта", 1200, 10)

    captured = capsys.readouterr()
    out = captured.out

    # Должно содержать упоминание класса Product
    assert "Создан объект класса Product" in out

    # Должно содержать переданные позиционные аргументы
    # проверяем, что в выводе есть имя и описание (в кавычках) и числа
    assert "Продукт1" in out
    assert "Описание продукта" in out
    assert "1200" in out
    assert "10" in out

    # Опционально — проверим, что вывод содержит структуру args=(...)
    assert "args=" in out or "args =" in out


def test_mixin_does_not_break_product_functionality(capsys):
    """
    Убедимся, что миксин не ломает обычную функциональность Product:
    - доступ к атрибутам,
    - строковое представление (__str__),
    - поведение сеттера price.
    """
    p = Product("Тест", "desc", 500, 3)

    # основной вывод миксина есть (съедаем его)
    _ = capsys.readouterr()

    # свойства остались доступными
    assert p.name == "Тест"
    assert p.quantity == 3

    # __str__ должен работать (формат зависит от реализации, проверим часть строки)
    s = str(p)
    assert "Тест" in s
    assert "500" in s or "500 руб" in s

    # сеттер цены не ломает: ставим корректную цену
    p.price = 700
    assert p.price == 700

    # и попытка установить некорректную цену должна печатать предупреждение и не менять цену
    p.price = 0
    captured = capsys.readouterr()
    assert "Цена" in captured.out  # часть сообщения предупреждения
    assert p.price == 700


def test_baseproduct_is_abstract():
    # instantiating abstract should raise TypeError
    with pytest.raises(TypeError):
        BaseProduct("x", 10)  # abstract can't be instantiated when abstract methods exist


def test_mixin_prints_args_kwargs(capsys):
    # create a temporary subclass that uses the mixin and minimal init
    class Echo(LogCreationMixin, BaseProduct):
        def __init__(self, name, price, **kwargs):
            super().__init__(name, price, **kwargs)
        def get_info(self):
            return f"{self.name}"

    e = Echo("X", 1, k=2)
    out = capsys.readouterr().out
    assert "Создан объект класса Echo" in out or "Создан объект класса" in out
    assert "X" in out
    assert "1" in out
    # kwargs printed
    assert "k" in out or "kwargs" in out

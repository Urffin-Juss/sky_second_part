class LogCreationMixin:
    """Миксин, выводящий информацию о создании объекта."""

    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        print(f"Создан объект класса {class_name} с параметрами: args={args}, kwargs={kwargs}")
        super().__init__(*args, **kwargs)

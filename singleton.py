from typing import Any


class SingletonExample(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances


class Example(metaclass=SingletonExample):
    def __init__(self) -> None:
        self.instance = 1
    
example1 = Example()
example2 = Example()

example1.instance = 2
example2.instance = 4

print(example1.instance)
print(example2.instance)
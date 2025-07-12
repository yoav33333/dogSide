from jsonGen import register_class
from util.singelton import SingletonMeta

@register_class
class Dog:
    name = "Dog"
    age = 0

    def bark(self):
        return f"{self.name} says Woof!"

    def __str__(self):
        return f"Dog(name={self.name})"

    def __repr__(self):
        return f"Dog(name={self.name})"
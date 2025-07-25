from jsonGen import register_class


@register_class
class Dog():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Dog, cls).__new__(cls)
        return cls.instance
    name = "Dog"
    age = 0.0

    def bark(self):
        return f"{self.name} says Woof!"

    def __str__(self):
        return f"Dog(name={self.name})"

    def __repr__(self):
        return (f"Dog(name={self.name})")

@register_class
class Cat():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Cat, cls).__new__(cls)
        return cls.instance
    name = "Cat"
    age = 0.0

    def mew(self):
        return f"{self.name} says Woof!"

    def __str__(self):
        return f"Dog(name={self.name})"

    def __repr__(self):
        return f"Dog(name={self.name})"
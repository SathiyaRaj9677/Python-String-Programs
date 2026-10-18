from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "woof!"

class Cat(Animal):
    def sound(self):
        return "meow!"

cat = Cat("Jean")
dog = Dog("Luna")
print(f"{cat.name} says {cat.sound()}")
print(f"{dog.name} says {dog.sound()}")


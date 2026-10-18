# 1. Single Inheritance:

class Animal:
    def __init__(self, neme):
        self.neme = neme

    def eat(self):
        print(f"{self.neme} is eating")

class Dog(Animal):
    def bark(self):
        print(f"{self.neme} is barking")

animal = Dog("luna")
animal.eat()
animal.bark()

# 2. Multilevel Inheritance:

class Animal:
    def __init__(self, neme):
        self.neme = neme

    def eat(self):
        print(f"{self.neme} is eating")

class Dog(Animal):
    def bark(self):
        print(f"{self.neme} is barking")

class Cat(Dog):
    def sleep(self):
        print(f"cat is sleeping")

animal = Cat("luna")
animal.eat()
animal.bark()
animal.sleep()


# 3. Multiple Inheritance:

class Father:
    def money(self):
        print("Father gives Money")
class Mother:
    def care(self):
        print("Mother gives Care")
class Child(Father, Mother):
    def study(self):
        print("Child is studying")
kid = Child()
kid.money()
kid.care()
kid.study()

# 4. Hierarchical Inheritance

class Animal:
    def __init__(self, neme):
        self.neme = neme

    def eat(self):
        print(f"{self.neme} is eating")

class Dog(Animal):
    def bark(self):
        print(f"{self.neme} is barking")

class Cat(Animal):
    def sleep(self):
        print(f"{self.neme} is sleeping")

animal = Dog("luna")
animal_1=Cat("tina")
animal.eat()
animal.bark()
animal_1.sleep()

# 5. Hybrid Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")


class Cat(Animal):
    def sleep(self):
        print(f"{self.name} is sleeping")


class Cow(Dog, Cat):
    def moo(self):
        print(f"{self.name} is mooing")


animal = Dog("Luna")
animal_1 = Cat("Tina")
cow = Cow("Lakshmi")

animal.eat()
animal.bark()

animal_1.sleep()

cow.eat()
cow.bark()
cow.sleep()
cow.moo()
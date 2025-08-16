# basic OOP example: Animal, Cat, Dog

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def demo():
    animals = [Dog('Rex'), Cat('Mittens')]
    for a in animals:
        print(f"{a.name} says: {a.speak()}")

if __name__ == '__main__':
    demo()

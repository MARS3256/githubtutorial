# basic OOP example: Animal, Cat, Dog, Bird

class Animal:
    """Base class for all animals."""
    def __init__(self, name):
        self.name = name

    def speak(self):
        """Make a generic animal sound."""
        return f"{self.name} makes a sound"

class Dog(Animal):
    """A loyal canine companion."""
    def speak(self):
        return "Woof!"

class Cat(Animal):
    """A independent feline friend."""
    def speak(self):
        return "Meow!"

class Bird(Animal):
    """A flying feathered friend."""
    def __init__(self, name, can_fly=True):
        super().__init__(name)
        self.can_fly = can_fly
    
    def speak(self):
        return "Tweet!"
    
    def fly(self):
        if self.can_fly:
            return f"{self.name} soars through the sky!"
        else:
            return f"{self.name} cannot fly."

def demo():
    animals = [
        Dog('Rex'), 
        Cat('Mittens'),
        Bird('Tweety'),
        Bird('Penguin', can_fly=False)
    ]
    
    for animal in animals:
        print(f"{animal.name} says: {animal.speak()}")
        
        # Demonstrate flying for birds
        if isinstance(animal, Bird):
            print(f"  {animal.fly()}")

if __name__ == '__main__':
    demo()

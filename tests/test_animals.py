"""
Unit tests for the animals module.
Demonstrates testing practices in GitHub workflows.
"""

import unittest
import sys
import os

# Add the examples directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'examples'))

from animals import Animal, Dog, Cat, Bird


class TestAnimals(unittest.TestCase):
    """Test cases for animal classes."""
    
    def test_animal_base_class(self):
        """Test that Animal base class works correctly."""
        animal = Animal("Generic")
        self.assertEqual(animal.name, "Generic")
        self.assertEqual(animal.speak(), "Generic makes a sound")
    
    def test_dog_class(self):
        """Test Dog class implementation."""
        dog = Dog("Buddy")
        self.assertEqual(dog.name, "Buddy")
        self.assertEqual(dog.speak(), "Woof!")
        self.assertIsInstance(dog, Animal)
    
    def test_cat_class(self):
        """Test Cat class implementation."""
        cat = Cat("Whiskers")
        self.assertEqual(cat.name, "Whiskers") 
        self.assertEqual(cat.speak(), "Meow!")
        self.assertIsInstance(cat, Animal)
    
    def test_bird_class_flying(self):
        """Test Bird class with flying capability."""
        bird = Bird("Eagle")
        self.assertEqual(bird.name, "Eagle")
        self.assertEqual(bird.speak(), "Tweet!")
        self.assertTrue(bird.can_fly)
        self.assertEqual(bird.fly(), "Eagle soars through the sky!")
        self.assertIsInstance(bird, Animal)
    
    def test_bird_class_non_flying(self):
        """Test Bird class without flying capability."""
        penguin = Bird("Pingu", can_fly=False)
        self.assertEqual(penguin.name, "Pingu")
        self.assertEqual(penguin.speak(), "Tweet!")
        self.assertFalse(penguin.can_fly)
        self.assertEqual(penguin.fly(), "Pingu cannot fly.")


if __name__ == '__main__':
    unittest.main()

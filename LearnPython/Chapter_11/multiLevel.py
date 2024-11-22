# Base Class (Parent)
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Some generic animal sound"

    def show(self):
        print(f"Animal: {self.name}")


# Derived Class (Child 1)
class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def sound(self):
        return "Some mammal-specific sound"

    def show(self):
        super().show()
        print(f"Fur Color: {self.fur_color}")


# Further Derived Class (Child 2)
class Dog(Mammal):
    def __init__(self, name, fur_color, breed):
        super().__init__(name, fur_color)
        self.breed = breed

    def sound(self):
        return "Bark!"

    def show(self):
        super().show()
        print(f"Breed: {self.breed}")


# Example Usage
# Create an instance of the Dog class
my_dog = Dog("Buddy", "Golden", "Golden Retriever")

# Call methods
my_dog.show()
print(f"Sound: {my_dog.sound()}")

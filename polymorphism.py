class Dog:

    def sound(self):
        print("bark")

class Cat:

    def sound(self):
        print("meow")
    
animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()  # This will output "bark" and "meow" respectively, demonstrating polymorphism.
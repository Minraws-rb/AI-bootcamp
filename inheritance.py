class Animal:

    def eat(self):
        print("Animal is eating.")

class Dog(Animal):
    def bark(self):
        print("Dog is barking.")

d = Dog()
d.eat()  # This will output "Animal is eating." because the Dog class inherits from the Animal class and can access its methods.
d.bark()  # This will output "Dog is barking." because the bark method is defined in the Dog class.
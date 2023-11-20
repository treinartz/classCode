def setup():
    size(400, 400)
    my_dog = Dog("Buddy", 3, "brown")
    my_cat = Cat("Whiskers", "gray")

    my_kennel = Kennel()
    my_kennel.add_pet(my_dog)
    my_kennel.add_pet(my_cat)

    # Make all pets in the kennel speak
    my_kennel.make_all_sounds(2)


class Pet:
    def __init__(self, name):
        self.name = name

    def speak(self, n):
        # Default implementation in the base class
        return "I'm hungry!"
    
class Cat(Pet):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def speak(self, n):
        return "Meow " * n
    
class Dog(Pet):
    def __init__(self, name, age, color):
        super().__init__(name)
        self.age = age
        self.color = color

    def birthday(self):
        self.age += 1

    def speak(self, n):
        return "Bark " * n
    

class Kennel:
    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def make_all_sounds(self, n):
        for pet in self.pets:
            print(f"{pet.name} says {pet.speak(n)}")

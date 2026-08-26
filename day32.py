#OBJECT-ORIENTED PROGRAMMING
#METHODS & SELF

class Pet:

    def speak(self):
        print("Hello Moma")

pet1 = Pet()
pet1.speak()


class Pet:

    def introduce(self):
        print(f"My name is {self.name}")
        print(f"Im {self.age} years old")


pet1 = Pet()

pet1.name = "Max"
pet1.age = 8

pet1.introduce()

pet2 = Pet()

pet2.name = "Evelyn"
pet2.age = 20

pet2.introduce()
# #OBJECT-ORIENTED PROGRAMMING
# # __init__() and OBJECT INITIALIZATION


# class Pet:

#     def __init__(self, name, species, hunger):
#         self.name = name
#         self.species = species
#         self.hunger = hunger

#     def introduce(self):
#         print(f"My name is {self.name} and I am a/an {self.species}")

#     def eat(self):
#         if self.hunger <= 40:
#             self.hunger += 20

#         return self.hunger

# pet1 = Pet("Kultur", "Human", 40)
# pet2 = Pet("Munich", "AI", 50)
# pet3 = Pet("Claudiadaves", "AI", 39)

# print("===== Using __init__ =====")
# pet1.introduce()
# print(pet1.eat())
# print()
# pet2.introduce()
# print(pet2.eat())
# print()
# pet3.introduce()
# print(pet3.eat())



# class Pet:

#     def __init__(self, name, species, hunger):
#         self.name = name
#         self.species = species
#         self.hunger = hunger

#     def introduce(self):
#         print(f" My name is {self.name} and I am a/an {self.species}.")

#     def eat(self):
#         if self.hunger >= 40:
#             self.hunger -= 20

#         return self.hunger

# pet1 = Pet("Kultur", "Human", 25)
# pet2 = Pet("Munich", "AI", 50)
# pet3 = Pet(name="Claudiadaves", species="AI", hunger=45)

# print("===== Using __init__ =====")
# print()
# pet1.introduce()
# print(pet1.eat())
# print()
# pet2.introduce()
# print(pet2.eat())
# print()
# pet3.introduce()
# print(pet3.eat())
# print("==== THANKS ====")


#STUDENT MGT SYSTEM

class Student:
    
    def __init__(self, name, age, course, score):
        self.name = name
        self.age = age
        self.course = course
        self.score = score
        
    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old, I love studing {self.course} and my last score was {self.score}.")
        
        
student1 = Student("Munich", 8, "Assembly", 90)
student2 = Student("Kultur", 26, "Python", 95)
student3 = Student(name="Nuel", age=27, course="Golang", score=98)

print("===== Using __init__ =====")
print()
student1.introduce()
print()
student2.introduce()
print()
student3.introduce()

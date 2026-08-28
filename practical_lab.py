# # # PRACTICAL LAB

# # # AGE CHECKER
# # # ask for username
# # username = input("What is your username?: ")

# # # ask for age
# # age = int(input("What is your age?: "))

# # # checking if age is greater then or equal to 18 
# # if age >= 18:
# #     print(f"Welcome, {username}! You are {age} years old and you're an adult.")

# # # checking if age is less than 18
# # elif age < 18:
# #     print(f"Sorry, {username}. You are still a minor")

# # print("Thanks for using the program!")

# # PET MANAGER - VERSION 1

# class Pet:
#     pass

# pet1 = Pet()
# pet2 = Pet()
# pet3 = Pet()

# pet1.name = "Munich"
# pet1.species = "Dog"
# pet1.hunger = 69

# pet2.name = "Kultur"
# pet2.species = "Cat"
# pet2.hunger = 84

# pet3.name = "Nuel"
# pet3.species = "Bird"
# pet3.hunger = 50


# print("--- PET 1 ---")
# print(f"Name: {pet1.name}")
# print(f"Species: {pet1.species}")
# print(f"Hunger: {pet1.hunger}")
# print("\n")
# print("--- PET 2 ---")
# print(f"Name: {pet2.name}")
# print(f"Species: {pet2.species}")
# print(f"Hunger: {pet2.hunger}")
# print("\n")
# print("--- PET 3 ---")
# print(f"Name: {pet3.name}")
# print(f"Species: {pet3.species}")
# print(f"Hunger: {pet3.hunger}")



# # STUDENT MANAGEMENT SYSTEM

# class Student:
#     pass

# student1 = Student()
# student2 = Student()
# student3 = Student()

# student1.name = "Munich"
# student1.age = 8
# student1.course = "Assembly"
# student1.score = 90

# student2.name = "Kultur"
# student2.age = 26
# student2.course = "Python"
# student2.score = 95

# student3.name = "Nuel"
# student3.age = 27
# student3.course = "Golang"
# student3.score = 98

# print("========= STUDENT 1 =========")
# print(f"Name: {student1.name}")
# print(f'Age: {student1.age}')
# print(f"Course: {student1.course}")
# print(f"Score: {student1.score}")
# # print("\n")
# # or
# print()
# print("========= STUDENT 2 =========")
# print(f"Name: {student2.name}")
# print(f'Age: {student2.age}')
# print(f"Course: {student2.course}")
# print(f"Score: {student2.score}")
# print()
# print("========= STUDENT 3 =========")
# print(f"Name: {student3.name}")
# print(f'Age: {student3.age}')
# print(f"Course: {student3.course}")
# print(f"Score: {student3.score}")   

# PET BEHAVIOR SYSTEM - VERSION 1

# class Pet:

#     # def __init__(self, name, species, hunger):
#     #     self.name = name
#     #     self.species = species 
#     #     self.hunger = hunger

#     def introduce(self):   
#         print(f"My name is {self.name} and I am a {self.species}")
    
#     # def eat(self):
        
#     #     if self.hunger >= 40:
#     #         self.hunger = self.hunger - 20
#     #         return (f"{self.hunger}")
#     #     else:
#     #         return(f"{self.hunger}")

#     def eat(self):
#         if self.hunger >= 40:
#             self.hunger -= 20

#         return self.hunger
        
# pet1 = Pet()
# pet2 = Pet()
# pet3 = Pet()

# pet1.name = "Hero"
# pet1.species = "Dog"
# pet1.hunger = 70

# pet2.name = "Sandra"
# pet2.species = "Cat"
# pet2.hunger = 89

# pet3.name = "Dora"
# pet3.species = "Bird"
# pet3.hunger = 39

# print("--- PET 1 ---")
# pet1.introduce()
# print(pet1.eat())
# print()
# print("--- PET 2 ---")
# pet2.introduce()
# print(pet2.eat())
# print()
# print("--- PET 3 ---")
# pet3.introduce()
# print(pet3.eat())


# PET CLASS

class Pet:

    def __init__(self, hunger):
        self.hunger = hunger

    def feed(self):
        self.hunger -= 20

        # if 0 < self.hunger < 100:
        if self.hunger < 0:
            self.hunger = 0

pet1 = Pet(19)
pet1.feed()
print(pet1.hunger)
print()
pet2 = Pet(50)
pet2.feed()
print(pet2.hunger)
print()
pet3 = Pet(79)
pet3.feed()
print(pet3.hunger)




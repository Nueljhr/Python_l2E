## TIMES TABLE
 
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")
#     print()  # Print a blank line after each table


# for i in range(12, 20):
#     for j in range(12, 20):
#         print(f"{i} * {j} = {i * j}")
#     print()  # Print a blank line after each table

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
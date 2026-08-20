# OBJECT-ORIENTED PROGRAMMING
# CLASS = BLUEPRINT
# OBJECT = THE THING CREATED FROM THE BLUEPRINT

class Pet:
    pass

my_pet = Pet()
my_pet1 = Pet()

my_pet.name = "Max"
my_pet.hungry = 50

my_pet1.name = "Luna"
my_pet1.hungry = 30

print(my_pet.name)
print(my_pet.hungry)

print(my_pet1.name)
print(my_pet1.hungry)


# LOGIN SYSTEM SIMULATOR
correct_username = "admin"
correct_password = "1234"

attempts = 4

while attempts > 0:
    name = input("Enter username:")
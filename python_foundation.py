# my_name = input("Enter your name:")
# print(my_name)

# age = 19
# # print(f"Amanda is {age} years old")
# print("Amanda is", age, "years old.")

# my_food = "Beans"
# fav_food = "Rice"
# print(my_food + " " + fav_food)

# print(5/2)
# # this returns a float
# print(5//2)
# # // MEANS FLOOR DIVISION returns an INT
# print(5%2)
# # % MODULO gives back the remainder
# print(5*2)
# # * the MULTIPLICATION 
# print(5**2)
# # ** EXPONETIAL

#PRACTICAL 1
# PERSONAL INTRODUCTION:

# name = input("What is your name: ")
# age = int(input("What is your age: "))
# city = input("Where do you live: ")
# print(f"Hello!, my name is {name}, i am {age} years old and i live in {city} city.")


#PRACTICAL 2
# #RECTANGLE CALCULATOR

# length = int(input("Len: "))
# breadth = int(input("breadth: "))

# area = length * breadth
# print(f"Your area is: {area}")

# perimeter = 2 * (length + breadth)
# print(f"Your perimeter is: {perimeter}")


# PRACTICAL 3
totnum_sec = int(input("Seconds: "))
comp_hours = totnum_sec // 3600
rem_min = (totnum_sec % 3600) // 60
seconds = totnum_sec % 60
print(f"{comp_hours} hours, {rem_min} minutes, {seconds} secs")

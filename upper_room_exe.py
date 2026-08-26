# USE F-STRINGS TO PRINT A SENTANCE WITH VARIABLES

name = "Nuel"
hobby = "coding"
print(f"Hi, my name is {name}, i love {hobby} for fun.")

# USERNAME GENERATOR
# from first and last name

class username:
    pass

User_name = username()

User_name.First = input("What is your firstname: ")
User_name.Last = input("What is your lastname: ")

firstname = User_name.First[:3]
lastname = User_name.Last[:3]

Username = firstname + lastname

print(Username)


first_name = input("What is your firstname: ")
last_name = input("What is your lastname: ")

first_three = first_name[:3]
last_three = last_name[:3]

username = first_three + last_three

print(username)


# PRACTICE STRING SLICING
word = "individual"

print(word[6:])

# this will display just dual

# RECTANGLE CALCULATOR (AREA AND PERIMETER)

len_rect = float(input("Enter length of rectangle: "))

wid_rect = float(input("Enter width of rectangle: "))
# calculate area
area = len_rect * wid_rect
# calculate perimeter
perimeter = 2 * (len_rect + wid_rect)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

# BMI CALCULATOR
print("=====BMI CALCULATOR=====")
weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

BMI = weight / (height * height)
print(f"Your bmi is: {BMI}")

# if BMI < 20.5:
#     print(f"Category: Underweight")
# elif BMI >= 20.5 and BMI < 27:
#     print("Category: Normal weight")
# elif BMI >= 27 and BMI < 31.5:
#     print("Category: Overweight")
# else:
#     print("Category: Obese")
# tho got this commented side idea from a friend n ai 



print("=====BMI CALCULATOR=====")
def bmi():
    weight = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))

    BMI = weight / (height * height)

    return BMI

print(bmi())


    


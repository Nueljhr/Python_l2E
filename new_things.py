# LOGIN SYSTEM SIMULATOR
# correct_username = "admin"
# correct_password = "1234"

# attempts = 4

# while attempts > 0:
#     name = input("Enter username: ")
    
    
    # COUNT VOWELS
# def vowel_count(text):
#     vowels = 'aeiou'
#     count = 0
#     text = text.lower()
#     #complete the function
#     #test funtion with 'hello', 'Education', 'text'
    
#     for vowel in text:
#         if vowel in vowels:
#             count += 1
#     return count

# print(vowel_count('Education'))

# MULTIPLICATION TABLE

# for i in range(1, 6):
#     print(f'\n{i} Times Multiplication Table:')
#     for j in range(1, 13): 
#         result = i * j
#         print(f'{i} x {j} = {result}')

# #EXAMPLE
# class Student:

#     def greet(self):
#         print("Hello")

#HOW TO USE __INIT__

# class Me:

#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

# me = Me(name="Kultur", species="Human")

# print(me.name)
# print(me.species)


# 
# count = 0
# for number in range(1, 6):
#     # Nested loop
#     for value in range(number):
#         if value == 2:
#             continue
#         count += value
# print(count)

# 1 → range(1) → 0
# 2 → range(2) → 0,1
# 3 → range(3) → 0,1,2
# 4 → range(4) → 0,1,2,3
# 5 → range(5) → 0,1,2,3,4

# number = 1
#     ↓
#     value = 0

# number = 2
#     ↓
#     value = 0
#     value = 1

# number = 3
#     ↓
#     value = 0
#     value = 1
#     value = 2

# number = 4
#     ↓
#     value = 0
#     value = 1
#     value = 2
#     value = 3

# number = 5
#     ↓
#     value = 0
#     value = 1
#     value = 2
#     value = 3
#     value = 4


# age = int(input("Enter your age: "))
# if age < 18:
#     print("You are a minor.")
# elif age >= 18 and age < 65:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")  

# number = int(input("Enter a number: "))
# if number > 0:
#     print("positive")
# elif number < 0:
#     print("negative")
# else:
#     print("zero.")

# count = 0
# for x in range(5):
#     number = int(input("Enter a number: "))
#     if number > 0:
#         count += 1
# print(f"There are {count} positive numbers.")

# sum_num = 0
# for x in range(5):
#   number = int(input("Enter a number: "))
#   if number > 0:
#     sum_num += number
# print(f"sum of number: {sum_num}")

# sum_num = 0
# for x in range(5):
#   number = int(input("Enter a number: "))
#   if number < 0:
#     sum_num += number
# print(f"sum of number: {sum_num}")


# count = 0
# for x in range(5):
#     number = int(input("Enter a number: "))
#     if number > 10:
#         count += 1
# print(f"There are {count} numbers greater than 10.")

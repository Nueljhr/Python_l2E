## TIMES TABLE
 
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")
#     print()  # Print a blank line after each table


# for i in range(12, 20):
#     for j in range(12, 20):
#         print(f"{i} * {j} = {i * j}")
#     print()  # Print a blank line after each table

# def append(my_list, item):
#     my_list.append(item)

# numbers = [1, 2, 3]

# append(numbers, 5)

# print(numbers)

# class Student:

#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def introduce(self):
#         print(f"My name is {self.name}")

#     def improve_score(self):
#         self.score += 5

#         # return self.score
    
#     def reset_score(self):
#         if self.score >= 100:
#             self.score = 0
#         return self.score
    
#     def get_score(self):
#         return self.score

# student1 = Student("Kultur", 89)
# student2 = Student("Munich", 109)

# student1.introduce()
# print(student1.improve_score())
# student1.improve_score()
# print(student1.score)
# print(student1.reset_score())

# student2.introduce()
# print(student2.improve_score())
# print(student2.reset_score())
# print(student2.get_score())


# number = 3
# guess = 0

# while guess != number:
#     guess = int(input("Enter a number: "))
#     if guess != number:
#         print("Try again!")
# print("Well done! You guessed it!")

# ENUMERATE
names = list(["Kultur", "Munich", "Python"])
numbers = list(range(2, 21, 2))

# for index, name in enumerate(names):
#     print(f"INDEX: {index}, NAME: {name}")

# for index, number in enumerate(numbers):
#     print(f"INDEX: {index}, NUMBER: {number}")

# # ZIP
# for name, number in zip(names, numbers):
#     print(f"NAME: {name}, NUMBER: {number}")


# for num in range(21):
#     if num % 2 == 0:
#         print(f"{num} is even")
# # or
# even_numbers = [num for num in range(21) if num % 2 == 0]
# print(even_numbers)

# def name_is_long(names):
#     return len(names) > 5
# long_names = list(filter(name_is_long, names))
# print(long_names)


# MAP
# farhenheit = [32.0, 50.0, 68.0, 86.0, 104.0]

# def to_celsius(f):
#     return((f - 32) * 5.0/9.0)

# celsius = list(map(to_celsius, farhenheit))
# print(celsius)

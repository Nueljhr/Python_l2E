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

class Me:

    def __init__(self, name, species):
        self.name = name
        self.species = species

me = Me(name="Kultur", species="Human")

print(me.name)
print(me.species)
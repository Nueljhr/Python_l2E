
# my_str = 'Hello world'
# print("Hello" in my_str)
# print(len(my_str))
# print(my_str[0])
# print(my_str[6])
# print(my_str[-1])
# print(my_str[-2])

# # Ceasar cipher is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a shift of 1, 'A' would be replaced by 'B', 'B' would become 'C', and so on. The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials.
# def caesar_cipher(text, shift):
#     result = ""
#     for char in text:
#         if char.isalpha():
#             shift_base = ord('A') if char.isupper() else ord('a')
#             result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
#         else:
#             result += char
#     return result


# def caesar(text, shift, encrypt=True):

#     if not isinstance(shift, int):
#         return 'Shift must be an integer value.'

#     if shift < 1 or shift > 25:
#         return 'Shift must be an integer between 1 and 25.'

#     alphabet = 'abcdefghijklmnopqrstuvwxyz'

#     if not encrypt:
#         shift = - shift
    
#     shifted_alphabet = alphabet[shift:] + alphabet[:shift]
#     translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
#     encrypted_text = text.translate(translation_table)
#     return encrypted_text

# def encrypt(text, shift):
#     return caesar(text, shift)

# def decrypt(text, shift):
#     return caesar(text, shift, False)


# encrypted_text = encrypt('freeCodeCamp', 3)
# print(encrypted_text)  # Output: iuhhFrghFdpso

# encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."
# decrypted_text = decrypt(encrypted_text, 13)
# print(decrypted_text)  # Output: Coder is great in Python programming.


# BUILD AN RPG CHARACTER

# def create_character(name, strength, intelligence, charisma):
#     if not isinstance(name, str):
#         return 'The character name should be a string'
#     elif name == '':
#         return 'The character should have a name'
#     elif len(name) > 10:
#         return 'The character name is too long'
#     elif ' ' in name:
#         return 'The character name should not contain spaces'

#     if not all(isinstance(stat, int) for stat in (strength, intelligence, charisma)):
#         return 'All stats should be integers'

#     if not all(stat >= 1 for stat in (strength, intelligence, charisma)):
#         return 'All stats should be no less than 1'

#     if not all(stat <= 4 for stat in (strength, intelligence, charisma)):
#         return 'All stats should be no more than 4'

#     if strength + intelligence + charisma != 7:
#         return 'The character should start with 7 points'

#     strength_dots = '●' * strength + '○' * (10 - strength)
#     intelligence_dots = '●' * intelligence + '○' * (10 - intelligence)
#     charisma_dots = '●' * charisma + '○' * (10 - charisma)

#     return f'{name}\nSTR {strength_dots}\nINT {intelligence_dots}\nCHA {charisma_dots}'

# # print(create_character('', 4, 2, 1))

# # print(create_character('verylongname', 4, 2, 1))

# # print(create_character('re n', 4, 2, 1))

# # print(create_character('ren', 5, 1, 1))

# print(create_character('ren', 4, 2, 1))
# print(create_character('nuel', 3, 2, 2))

# Common String Methods

# # STRIP(): This returns a new string with all occurrences of the old string replaced by a new one.
# greeting = '  hello world  '

# trimmed_my_str = greeting.strip()
# print(trimmed_my_str)  # 'hello world'

# # REPLACE(): This returns a new string with all occurrences of the old string replaced by a new one.
# greeting = 'hello world'

# replaced_my_str = greeting.replace('hello', 'hi')
# print(replaced_my_str)  # 'hi world'

# # SPLIT(): This is used to split a string into a list using a specified separator. A separator is a string specifying where the split should happen.
# # RETURNS A LIST
# # dashed_name = 'example-dashed-name'
# spaced_name = 'example spaced name'
# # split_words = dashed_name.split('-')
# spaced_name = spaced_name.split(' ')
# spaced_name = spaced_name.split('a')
# # print(split_words)  # ['example', 'dashed', 'name']
# print(spaced_name)

# JOIN(): This is used to join a collection of strings into one string with a separator.
# RETURNS A LIST
# example_list = ['example', 'dashed', 'name']

# joined_str = ''.join(example_list)
# # joined_str = ' '.join(example_list)
# # joined_str = '  '.join(example_list)
# example_list = 'a'.join(example_list)
# print(joined_str)  # example dashed name

# STARTSWITH(PREFIX)
# RETURNS A BOOLEAN
# str.startswith(prefix): This returns a boolean indicating if a string starts with the specified prefix:
# developer = 'Naomi'

# result = developer.startswith('N')
# result = developer.startswith('na')
# print(result)  # True

# int(result)  # True

# ENDSWITH(SUFFIX)
# RETURNS A BOOLEAN
# # str.endswith(suffix): This returns a boolean indicating if a string ends with the specified suffix:
# developer = 'Naomi'

# result = developer.endswith('N')
# print(result)  # False

# FIND()
# THIS RETURNS THE INDEX
# str.find(): This returns the index for the first occurrence of a substring. If one is not found, then -1 is returned:
# developer = ' Naomi'

# result = developer.find('N')
# result = developer.find(' ')
# print(result)  # 0

# city = 'Los Angeles'
# print(city.find('New')) # -1

# # COUNT()
# # str.count(substring): This counts how many times a substring appears in a string:
# city = 'Los Angeles'
# print(city.count('e')) # 2

# # CAPITALIZE()
# # str.capitalize(): This returns a new string with the first character capitalized and the other characters lowercased:
# dessert = 'chocolate cake'
# print(dessert.capitalize()) # Chocolate cake

# # ISUPPER()
# # THIS RETURNS A BOOLEAN
# # str.isupper(): This returns True if all letters in the string are uppercase and False if otherwise:
# dessert = 'chocolate cake'
# print(dessert.isupper()) # False

# # ISLOWER()
# # THIS RETURNS A BOOLEAN
# # str.islower(): This returns True if all letters in the string are lowercase and False if otherwise:
# dessert = 'chocolate cake'
# print(dessert.islower()) # True

# # TITLE()
# # THIS ONE IS DOING WHAT CAPITALIZE SUPPPOSE DO
# # str.title(): This returns a new string with the first letter of each word capitalized:
# city = 'los angeles'
# print(city.title()) # Los Angeles

# MAKETRANS()
# TRANSLATE()
# str.maketrans(): This method is used to create a table of 1 to 1 character mappings for translation. It is often used with the translate() method which applies that table to a string and return the translated result.

# trans_table = str.maketrans('abc', '123')
# print(trans_table) # {97: 49, 98: 50, 99: 51}

# result = 'abcabc'.translate(trans_table)
# result = 'abcbac'.translate(trans_table)
# print(result)  # 123123

# Modulo Operator (%): This returns the remainder when a number is divided by another number:
int_1 = 56
int_2 = 12

print(int_1 % int_2) # 8

# Floor Division (//): This operator is used to divide two numbers and round down the result to the nearest whole number:
int_1 = 56
int_2 = 12

print(int_1 // int_2) # 4

# Exponentiation Operator (**): This operator is used to raise a number to the power of another:
int_1 = 4
int_2 = 2

print(int_1 ** int_2) # 16

# ROUND()
# IT APPROXIMATES
# round() Function: This is used to round a number to the nearest whole integer:
num_1 = 3.4
num_2 = 7.7

print(round(num_1)) # 3
print(round(num_2)) # 8

# ABS()
# MORE LIKE TAKING AWAY THE NEGATIVE VIBES
# abs() Function: This is used to return the absolute value of a number:
num = -13

print(abs(num)) # 13

# POW()
# SO ITS ANOTHER FORM OF EXPONETIAL HMM
# pow() Function: This is used to raise a number to the power of another:
result = pow(2, 3) 
print(result)  # 8

# Augmented Assignments
# Definition: Augmented assignment applies an operation to a variable and stores the result back in the same variable, all in one step.
# Addition assignment 
my_var = 10
my_var += 5

print(my_var) # 15

# Subtraction assignment
count = 14
count -= 3

print(count) # 11

# Multiplication assignment 
product = 65
product *= 7

print(product) # 455

# Division assignment 
price = 100
price /= 4

print(price) # 25.0

# Floor Division assignment 
total_pages = 23
total_pages //= 5

print(total_pages) # 4

# Modulo assignment 
bits = 35
bits %= 2

print(bits) # 1

# Exponentiation assignment 
power = 2
power **= 3

print(power) # 8

# Working with Functions
# Definition: Functions are reusable pieces of code that take inputs (arguments) and returns an output. To call a function, you need to reference the function name followed by a set of parenthesis:

# int() Function: This is used to convert a number, boolean, or a numeric string into an integer:
print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0 


# Working with if, elif and else Statements
# if Statements: These are conditions used to determine if something is true or not. If the condition evaluates to True, then that block of code will run.
# elif Clause: These are conditions that come after an if statement. An elif clause runs only if all previous conditions evaluate to False and its own condition evaluates to True.
# else Clause: This will run if no other conditions evaluate to True.

# You can also use nested if statements like this:

is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')
    
    # Truthy and Falsy Values
# Definition: In Python, every value has an inherent boolean value, or a built-in sense of whether it should be treated as True or False in a logical context. Many values are considered truthy, that is, they evaluate to True in a logical context. Others are falsy, meaning they evaluate to False. Here are some examples of falsy values:
# None
# False
# Integer 0
# Float 0.0
# Empty strings ''
# Other values like non-zero numbers, and non-empty strings are truthy.

# Working with the bool() Function
# Definition: If you want to check whether a value is truthy or falsy, you can use the built-in bool() function. It explicitly converts a value to its boolean equivalent and returns True for truthy values and False for falsy values. Here are a few examples:

print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True

# Boolean Operators and Short-circuiting
# Definition: These are special operators that allow you to combine multiple expressions to create more complex decision-making logic in your code. There are three Boolean operators in Python: and, or, and not.
# and Operator: This operator takes two operands and returns the first operand if it is falsy, otherwise, it returns the second operand. Both operands must be truthy for an expression to result in a truthy value.
# or Operator: This operator returns the first operand if it is truthy, otherwise, it returns the second operand. An or expression results in a truthy value if at least one operand is truthy. Here is an example:
# Short-circuiting: The and and or operators are known as a short-circuit operators. Short-circuiting means Python checks values from left to right and stops as soon as it determines the final result.
# not Operator: This operator takes a single operand and inverts its boolean value. It converts truthy values to False and falsy values to True. Unlike the previous operators we looked at, not always returns True or False. Here are some examples:

print(not '') # True, because empty string is falsy
print(not 'Hello') # False, because non-empty string is truthy
print(not 0) # True, because 0 is falsy
print(not 1) # False, because 1 is truthy
print(not False) # True, because False is falsy
print(not True) # False, because True is truthy

developer = 'Jessica'
list(developer) # ['J', 'e', 's', 's', 'i', 'c', 'a']

# UNPACKING VALUES FROM A LIST
developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer

print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'

desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
desserts[1:4] # ['Cookies', 'Ice Cream', 'Pie']

# APPEND
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.append(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, [6, 8, 10]]

# EXTEND
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.extend(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, 6, 8, 10]

# INSERT
numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)

print(numbers) # [1, 2, 2.5, 3, 4, 5]

# REMOVE
numbers = [10, 20, 30, 40, 50, 50]
numbers.remove(50)

print(numbers) # [10, 20, 30, 40, 50]

# POP
numbers = [1, 2, 3, 4, 5]
numbers.pop() # The number 5 is returned

numbers = [1, 2, 3, 4, 5]
numbers.pop(1) # The number 2 is returned

# CLEAR
numbers = [1, 2, 3, 4, 5]
numbers.clear()

print(numbers) # []

# SORT() AND SORTED()
numbers = [19, 2, 35, 1, 67, 41]
numbers.sort()

print(numbers) # [1, 2, 19, 35, 41, 67]

numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)

print(numbers) # [19, 2, 35, 1, 67, 41]
print(sorted_numbers) # [1, 2, 19, 35, 41, 67]

# REVERSE()
numbers = [6, 5, 4, 3, 2, 1]
numbers.reverse()

print(numbers) # [1, 2, 3, 4, 5, 6]

# INDEX()
programming_languages = ['Rust', 'Java', 'Python', 'C++']
programming_languages.index('Java') # 1

# DEL
developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]

# TUPLE
# TUPLE DATA TYPE
# Accessing Tuple Elements
developer = ('Alice', 34, 'Rust Developer')
developer[1] # 34

numbers = (1, 2, 3, 4, 5)
numbers[-2] # 4

developer = 'Jessica'
tuple(developer) # ('J', 'e', 's', 's', 'i', 'c', 'a')

# 
programming_languages = ('Python', 'Java', 'C++', 'Rust')

'Rust' in programming_languages # True
'JavaScript' in programming_languages # False

# Unpacking Values From a Tuple
developer = ('Alice', 34, 'Rust Developer')
name, age, job = developer

print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'

developer = ('Alice', 34, 'Rust Developer')
name, *rest = developer

print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']

# Slicing Tuples
desserts = ('cake', 'pie', 'cookies', 'ice cream')
desserts[1:3] # ('pie', 'cookies')

# TUPLE METHODS
# COUNT()
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count('Rust') # 2

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count('JavaScript') # 0

# index() 
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.index('Java') # 1

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
programming_languages.index('Python', 3) # 5 CAUSE ONLY START INDEX WAS DEFINED

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
programming_languages.index('Python', 2, 5) # 2 CAUSE START AND STOP INDEX WAS DEFINED

# SORTED()
numbers = (13, 2, 78, 3, 45, 67, 18, 7)
sorted(numbers) # [2, 3, 7, 13, 18, 45, 67, 78]

# KEY
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
sorted(programming_languages, key=len)

# Result
# ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']

# REVERSE
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')

print(sorted(programming_languages, reverse=True))

# Result
# ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']


# LOOP
# Using for Loops
for char in 'code':
    print(char)

# Nesting for Loops
categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)
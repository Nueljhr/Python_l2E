# # KEYWORDS

# False
# None
# True
# and
# as
# assert
# async
# await
# break
# class
# continue
# def
# del
# elif
# else
# except
# finally
# for
# from
# global
# if
# import
# in
# is
# lambda
# nonlocal
# not
# or
# pass
# raise
# return
# try
# while
# with
# yield
# match
# case

# import keyword

# print(keyword.kwlist)  # This will print the list of all Python keywords


# LESSON 6: VARIABLES AND PRIMITIVE TYPES
# Variables are used to store data in a program. They can hold different types of values, such as numbers, strings, and booleans.
# = Assignment operator
# == Comparison operator
# Data types: int, float, str, bool. The specific category of information being stored, which determines what rules apply to it.
# type() function can be used to check the type of a variable.

# LESSON 8: TYPE CONVERSION AND CASTING

# isdigit()  # Returns True if all characters in the string are digits, otherwise False
# int() used tp convert a string or float to an integer. It truncates the decimal part.
# float() used to convert a string or integer to a float. It retains the decimal part.
# str() used to convert a number to a string.
# boolean values: True and False. They are used to represent truth values in logical operations.

# LESSON 9.1: CONTROL FLOW AND CONDITIONAL STATEMENTS
# if, elif, else statements are used to control the flow of a program based on conditions

# IF STATEMENTS
# if condition:
# the keyword 'if' is used to start a conditional statement. The condition is a boolean expression that evaluates to either True or False.    
# # code to execute if condition is True
# ELSE STATEMENTS
# else:
# the keyword 'else' is used to provide an alternative block of code that will execute if the condition in the 'if' statement is False.
# # code to execute if condition is False
# ELIF STATEMENTS
# elif condition:
# the keyword 'elif' (short for "else if") is used to check multiple conditions after an initial 'if' statement. If the condition in the 'if' statement is False, the program will check the 'elif' condition. If it is True, the corresponding block of code will execute.
# # code to execute if the condition in the 'elif' statement is True
# INDENTATION
# Indentation is crucial in Python as it defines the blocks of code that belong to specific control structures like 'if', 'elif', and 'else'. Proper indentation ensures that the code executes as intended. Each block of code under these statements should be indented consistently, typically by four spaces or one tab. Incorrect indentation can lead to syntax errors or unexpected behavior in the program.
# 
#  LESSON 10: CONTROL FLOWS: LOOPS
# LOOPS:
# this is a control flow statement that allows code to be executed repeatedly based on a condition. Python primarily uses two types of loops: 'for' loops and 'while' loops.
# a structure that repeats a block of code a certain number of times or while a condition is true. Python has two main types of loops: 'for' loops and 'while' loops.
# a simple loop that iterates over a sequence (like a list, tuple, or string) or other iterable objects. It executes a block of code for each item in the sequence.
# LESSON 12: DEFINING FUNCTIONS
# def greet_barista():
#     print("Hello,barista!")

# greet_barista()

# "customer_name" is a placeholder parameter

# def print_cup_label(customer_name):
#     print("--------------------")
#     print("Order: Hot Latte")
#     print("Name: " + customer_name)
#     print("--------------------")

# # Pass real string values (arguments) into the function
# print_cup_label("Alice")
# print_cup_label("Bob")

# The function is self-contained. It only cares about the parameter variable.
# def print_label(name):
#     print("Name on cup: " + name)
#     # print(f"Name on cup: {name}")

# # Pass the data directly into the call
# print_label("Alice")
# print_label("Bob")

# def order_drink(drink,size):
#     # print("Dispensing" + " " + size + " " + drink)
#     print(f"Dispensing {size} {drink}")

# order_drink("espresso", "large")

# RETURN VALUE
# DEFINIITION

# def calculate_price(count, cost):
#     total = count * cost
#     return total
# # print(int(calculate_price(3, 4.50)))
# # customer_reciept = calculate_price(3, 4.50)
# cups_ordered = 3
# price_per_cup = 4.50
# customer_reciept = calculate_price(cups_ordered, price_per_cup)

# print(int(customer_reciept))

# def add_tax(subtotal):
#     return subtotal * 1.08

# final_total = add_tax(10.0)
# print(final_total)

# PARAMETERS AND RETURN VALUES
# def make_custom_drink(base_drink, milk_type, sugar_packets):
#     # Assemble the descriptive string step-by-step
#     description = f"{base_drink} with {milk_type} milk"
    
#     if sugar_packets > 0:
#         description = description + f" and {sugar_packets} sugar packets"
        
#     return description

# # Generate distinct order strings
# order1 = make_custom_drink("Latte", "almond", 2)
# order2 = make_custom_drink("Cappuccino", "whole", 0)

# print(order1) # "Latte with almond milk and 2 sugar packets"
# print(order2) # "Cappuccino with whole milk"

# # DEFAULT PARAMETER VALUE
# THE VALUE PYTHON USES WHEN YOU DONT PROVIDE AN ARGUMENT
# def greet(name="Friend"):
#     # print("Hello"+" "+name)
#     print(f"Hello {name}")
# greet()
# # greet("Alice")

# POSITIONAL ARGUMENTS
# def introduce(name, age):
#     print(name, age)

# # introduce(26,"Kultur")

# # KEYWORD ARGUMENT
# introduce(name="Kultur", age=26)

# COMBINE BOTH
# def greet(name, message="Hello"):
#     print(f"{message}, {name}")

# greet("Kultur")
# greet("Kultur", message="Good morning")


# LESSON 13: FUNCTIONS AND PARAMETERS










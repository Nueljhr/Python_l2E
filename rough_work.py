
# item = "supposed to be a string"
#     print(item.upper())

# print("supposed to be a string".upper())

# += means compound assignment operator, which adds the right operand to the left operand and assigns the result to the left operand. For example:
# x = 5
# x += 3  # This is equivalent to x = x + 3

# student = ("Kultur", 20)

# print(student)

# print("="*30)
# print("EXERCISE")
# print("="*30)

# correct_username = "Nuel"
# correct_password = "nuel"
# attempts = 4

# while attempts > 0:
#     username = input("Enter Username: ")

#     if correct_username == username:
#         attempts = 4
        
#         while attempts > 0:
#             password = input(f"Enter Password: ")

#             if correct_password == password:
#                 print('Login successful!')
#                 break
            
#             else:
#                 attempts -= 1
                
#                 if attempts > 0:
#                     print(f"Login Failed. {attempts} attempts left ")
#                 else:
#                     print("Account Locked")
#         break

#     else:
#         attempts -= 1
        
#         if attempts > 0:
#             print(f"Login Failed. {attempts} attempts left ")
#         else:
#             print("Account Locked")
        

# print("="*30)
# print("EXERCISE")
# print("="*30)


# correct_username = "nuel"
# correct_password = "1234"
# attempts = 4

# while attempts > 0:
#     user_name = input("Enter User_name: ")

#     if user_name == correct_username:
        
#         while attempts > 0:
#             user_password = input("Enter User_password: ")

#             if user_password != correct_password:
#                 print(f"Incorrect details. {attempts} attempts left")
#             attempts -= 1
#         else:
#             print("Login successful")
#             break
#         break


#     else:
#         attempts -= 1

#         if attempts > 0:
#             print(f"Incorrect details. {attempts} attempts left")
#         else:
#             print("Account locked")

# GETTING MAXIMUM NUMBER FROM USER INPUTS
# numbers = []
# for _ in  range(5):
#     number = int(input("Enter a number: "))
#     numbers.append(number)
#     max_number =max(numbers)
# print(f"This is the maximum number: {max_number}.")


# max_number = int(-1000000) # Initialize max_number to the smallest possible value
# for x in range(5):
#     number = int(input("Enter a number: "))

#     if number > max_number:
#         max_number = number

# print(f"The largest number is {max_number}")


# number = int(input("Enter a number: "))
# largest_number = number
# for _ in range(4): 
#     number = int(input("Enter a number: "))
#     if number > largest_number:
#         largest_number = number
        
# print(f"Maximum number is: {largest_number}.")


# number = int(input("Enter a number: "))
# smallest_number = number
# for _ in range(4):
#   number = int(input("Enter a number: "))
#   if number < smallest_number:
#     smallest_number = number
# print(f"Smallest number is: {smallest_number}.") 

# count = 0
# for _ in range(5):
#     number = int(input("Enter a number: "))
#     if number < 0:
#         count += 1
# print(f"There are {count} negative numbers.")

# sum_of_numbers = 0
# for _ in range(5):
#     number = int(input("Enter a number: "))
#     if number < 0:
#         sum_of_numbers += number
# print(f"The sum of negative numbers is: {sum_of_numbers}.")

# # Ask the user for 5 numbers and calculate the sum of only the negative numbers.
# sum_of_negative_numbers = 0
# for _ in range(5):
#     number = int(input("Enter a number: "))
#     if number < 0:
#         sum_of_negative_numbers += number
# print(f"The sum of negative numbers is: {sum_of_negative_numbers}.")

# sum_of_positive_numbers = 0
# for _ in range(5):
#     number = int(input("Enter a number: "))
#     if number > 0:
#         sum_of_positive_numbers += number
# print(f"The sum of positive numbers is: {sum_of_positive_numbers}.")

sum_of_numbers = 0
for _ in range(5):
    number = int(input("Enter a number: "))
    sum_of_numbers += number
    average = sum_of_numbers / 5
print(f"The average of the numbers is: {average}.")
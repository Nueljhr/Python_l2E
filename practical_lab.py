# PRACTICAL LAB

# AGE CHECKER
# ask for username
username = input("What is your username?: ")

# ask for age
age = int(input("What is your age?: "))

# checking if age is greater then or equal to 18 
if age >= 18:
    print(f"Welcome, {username}! You are {age} years old and you're an adult.")

# checking if age is less than 18
elif age < 18:
    print(f"Sorry, {username}. You are still a minor")

print("Thanks for using the program!")


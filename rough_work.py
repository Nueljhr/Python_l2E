
# item = "supposed to be a string"
#     print(item.upper())

# print("supposed to be a string".upper())

# += means compound assignment operator, which adds the right operand to the left operand and assigns the result to the left operand. For example:
# x = 5
# x += 3  # This is equivalent to x = x + 3

# student = ("Kultur", 20)

# print(student)

print("="*50)
print("EXERCISE")
print("="*50)

correct_username = "Nuel"
correct_password = "nuel"
attempts = 4

while attempts > 0:
    username = input(f"Enter Username: ")

    if correct_username == username:

        while attempts > 0:
            password = input(f"Enter Password: ")

            if correct_password != password:
                print(f"Login Failed. {attempts} attempts left")
            attempts -= 1
        else:
            print("Login Successful.")
            break
        break

    else:
        attempts -= 1
        
        if attempts > 0:
            print(f"Login Failed. {attempts} attempts left ")
        else:
            print("Account Locked")
        


# correct_username = "nuel"
# correct_password = "1234"
# attempts = 0

# while attempts < 2:
#     username = input("username: ")

#     if username == correct_password:
#         password = input("password: ")

#         if password == correct_password:
#             print("successfully logged in")
#             break
#         attempts += 1
#     else:
#         print(f'wrong password {attempts} attempts left')



print("="*30)
print("EXERCISE")
print("="*30)


correct_username = "nuel"
correct_password = "1234"
attempts = 4

while attempts > 0:
    user_name = input("Enter User_name: ")

    if user_name == correct_username:
        while attempts > 0:
            user_password = input("Enter User_password: ")

            if user_password != correct_password:
                print(f"Incorrect details. {attempts} attempts left")
            attempts -= 1
        else:
            print("Login successful")
            break
        breakf


    else:
        attempts -= 1

        if attempts > 0:
            print(f"Incorrect details. {attempts} attempts left")
        else:
            print("Account locked")

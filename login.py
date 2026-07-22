
Username = input("What is your username: ")
Password = input("What is your password: ")

correct_username = "kultur"
correct_password = "python123"

if Username == correct_username and Password == correct_password:
    print("Login successful!")
elif Username == correct_username and Password != correct_password:
    print("Incorrect password!")
elif Username != correct_username and Password == correct_password:
    print("Incorrect username!")
else:
    print("User not found")

print("Thank you for using our system")

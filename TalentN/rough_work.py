# JUST ROUGH WORK FOR NOW, WILL REFACTOR LATER

# print = "Hello, World!"  # This will override the built-in print function

# print(print)  # This will now print the string "Hello, World!"

# print("This will cause an error")  # This will raise a TypeError since print is now a string

# Check if a word is a keyword
# import keyword

# print(keyword.iskeyword("if"))

# # Check if a word is a palindrome
# def is_palindrome(word):
#     return word == word[::-1]


# Example script — calculates the cost of coffee orders

# # Set prices for different drinks
# espresso_price = 3.50
# latte_price = 4.50
# cappuccino_price = 4.00

# # Get the number of drinks ordered
# num_espresso = 2
# num_latte = 1
# num_cappuccino = 1

# # Calculate the total cost
# total = (num_espresso * espresso_price) + \
#         (num_latte * latte_price) + \
#         (num_cappuccino * cappuccino_price)

# # Check if total is above the minimum for a discount
# discount = 0.10
# if total > 20:
#     total = total - (total * discount)  # Apply 10% discount
#     print("Discount applied!")
# else:
#     print("No discount available")

# # Print the final total
# print(f"Total cost: ₦{total}")
# print("Thank you for your order!")

# This code is from a real e-commerce system
# It calculates shipping costs based on order total

# def calculate_shipping(total):
#     # Free shipping for orders over ₦50
#     if total > 50:
#         return 0
#     # Standard shipping for smaller orders
#     else:
#         return 5.99

# print(calculate_shipping(60))  # Should return 0
# print(calculate_shipping(40))  # Should return 5.99
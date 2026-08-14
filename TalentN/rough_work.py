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
# word[start:end:step]  # This is a slicing operation that returns a new string that is a reversed version of the original string.


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

# milk_ounces = 16
# pour_amount = 6
# remaining = milk_ounces - pour_amount
# print(remaining)

# cereal_in_box = 10
# required_scoops = 3
# print(cereal_in_box >= required_scoops)

# milk_ounces = 12
# cereal_scoops = 4
# bowl_capacity = 5

# # Using 'and' to ensure ALL requirements are met
# ready_to_serve = (milk_ounces >= 8) and (cereal_scoops >= 3) and (bowl_capacity >= cereal_scoops)
# # ready_to_serve is True because all individual expressions are True

# # Using 'or' to check alternate options
# can_use_alternate_bowl = (bowl_capacity >= 10) or (cereal_scoops <= 3)
# # evaluates to False because bowl_capacity is 5 (5 >= 10 is False) and cereal_scoops is 4 (4 <= 3 is False)

# is_milk_fresh = True
# is_cereal_fresh = False
# can_serve = is_milk_fresh and is_cereal_fresh
# print(can_serve)

# print(2 + 3 * 4)
# print((2 + 3) * 4)

# banana_count = "2"      # text string
# milk_cups = "1.5"       # text string

# # # Convert the text variables into numeric variables
# # banana_count = int(banana_count)   # Becomes the integer 2
# # milk_cups = float(milk_cups)      # Becomes the float 1.5

# # # Perform mathematical addition on the numbers
# # total = banana_count + milk_cups  # 2 + 1.5 = 3.5
# # print(total)  # Outputs: 3.5
# print(banana_count + milk_cups)  # Outputs: 21.5

# print(float("1.5"))
# Now try:
# print(int("1.5"))

# ounces = 8.5
# print("Pouring " + str(ounces) + " ounces of milk.")

# user_input = "banana"  # This is a string input from the user

# # Check if the string consists entirely of digits (0-9)
# if user_input.isdigit():
#     banana_count = int(user_input)
#     print("Conversion successful!")
# else:
#     print("Warning: That is not a valid number! Defaulting to 0.")
#     banana_count = 0

# value1 = "15"
# value2 = "banana"
# print(value1.isdigit())
# print(value2.isdigit())

# selected_drink = "Water"
# # selected_drink = "Green Tea"
# # selected_drink = f"Coffee"
# target_temp = 100
# if selected_drink == "Green Tea":
#     target_temp = 80
#     print(f"Target temperature for {selected_drink} is {target_temp}°C")
#     print(f"{target_temp}°C.")
# elif selected_drink == "Coffee":
#     target_temp = 90
#     print(f"Target temperature for {selected_drink} is {target_temp}°C")
#     print(f"{target_temp}°C.")
# else:
#     print(f"Target temperature for {selected_drink} is {target_temp}°C")
#     print(f"{target_temp}°C.")

# selected_drink = "Black Tea"
# target_temp = 100
# if selected_drink == "Green Tea":
#     target_temp = 80
#     print("This line will be skipped!")

# print(target_temp)


# current_temperature = 18.0  # Current temperature in Celsius
# target_temperature = 22.0   # Desired temperature in Celsius
# occupancy_detected = True   # Boolean indicating if someone is present in the room
# if current_temperature < target_temperature and occupancy_detected == True:
#     furnace_active = True
#     fan_speed = "High"
# elif current_temperature < target_temperature - 5.0: # extreme cold fallback
#     furnace_active = True
#     fan_speed = "Emergency"
# else:
#    furnace_active = False
#    fan_speed = "Off"


# n = 0
# while n < 5:
#     # n += 1 # with this here its gonna skip the counting 0 rather from 1 
#     # if n == 3:
#     #     continue  # Skip the rest of the loop when n is 3
#     print(n)
#     # n += 1 like this is gonna skip the counting 0 rather from 1
#     if n == 5:
#         break  # Exit the loop when n is 5

# for count in range(3):
#     print("Grind " + str(count))

# # range(5) counts from 0 to 4 (exactly 5 steps)
# for twist_number in range(5):
#     print("Grinding twist number " + str(twist_number + 1))
#     # grind_pepper()

# pepper_weight = 0  # Initialize the weight of pepper in ounces
# while pepper_weight < 5:
#     print(f"pouring pepper {pepper_weight} ounce(s)")
#     pepper_weight += 1  # Increment the weight of pepper by 1 ounce
   
# def grind_pepper():
#     print("Grinding pepper...")
# pepper_weight = 0.0  # Initialize the weight of pepper in grams

# # Repeat as long as our sensor weight is less than our target of 2.0 grams
# while pepper_weight < 2.0:
#     grind_pepper()
#     pepper_weight = read_scale_sensor()  # Update the loop variable!

# pepper_weight = 0.0

# def grind_pepper():
#     print("Grinding pepper...")

# def read_scale_sensor():
#     global pepper_weight
#     pepper_weight += 0.5  # Simulate adding 0.5 g of pepper
#     return pepper_weight

# # Keep grinding until we reach 2.0 grams
# while pepper_weight < 2.0:
#     grind_pepper()
#     pepper_weight = read_scale_sensor()
#     print(f"Current weight: {pepper_weight} g")

# print("Target weight reached!")

# import keyword

# print(keyword.iskeyword("global"))  # This will return True because "global" is a reserved keyword in Python

# weight = 0.0
# while weight < 1.5:
#     weight = weight + 0.5
#     print("Current weight: " + str(weight))

# food = f"banana"
# print(food)

# word = "ab"

# print(word.upper())

# The common cleanup methods:
# order = "  latte  "

# cleaned = order.strip()        # Removes whitespace from both ends -> "latte"
# loud = order.upper()           # Converts to uppercase -> "  LATTE  "
# quiet = order.lower()          # Converts to lowercase -> "  latte  "
# proper = order.strip().title() # Chains methods to strip and capitalize -> "Latte"

# # Replace words inside a string
# message = "Your coffee is ready"
# new_message = message.replace("coffee", "latte") # -> "Your latte is ready"

# print(cleaned)
# print(loud)
# print(quiet)
# print(proper)
# print(message)
# print(new_message)



# customer_name = "  alIce   "

# # Clean the string and save the output back into a variable
# cleaned_name = customer_name.strip()
# proper_name = cleaned_name.capitalize()

# print("[" + proper_name + "]")

# order = "  espresso  "
# print(order.strip().upper())

# customer_name = "  alIce   "
# customer_name.strip()      # This runs, but the result is lost
# customer_name.capitalize() # This runs, but the result is lost

# print("[" + customer_name + "]")

# name = "Christopher"
# print(name[0:5])

# customer = "Bob"
# total = 12.0
# print(f"Thank you, {customer}! Total: ₦{total:.2f}")

# raw_order_list = "latte,espresso,mocha"
# items = raw_order_list.split("e")
# print(items)

# menu_display = "\n".join(items)
# print(menu_display)

# def mix_ingredients(liquid,powder):
#     print("Mixing " + liquid + " with " + powder)

# mix_ingredients("milk","cocoa")

# def print_receipt(item, cost):
#     print(item + ": ₦" + str(cost))

# print_receipt("Espresso", 4.50)

# def cup_label(name, drink):
#     print(f"{name} ordered {drink}")

# cup_label(drink="espresso", name="Alice")

# def process_order(name, drink, size="medium"):
#     print(f"{name} wants a {size} {drink}")

# process_order("Alice", "Latte")
# process_order("Bob", "Espresso", "large")

# def sprinkle_sugar(packets=1):
#     print("Adding" + " " + str(packets) + " " + "sugar packets.")

# sprinkle_sugar()
# sprinkle_sugar(3)

#


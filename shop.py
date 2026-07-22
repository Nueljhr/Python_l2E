
item = input("Item: ")
price = int(input("Price of the item: "))
quantity = int(input("Quantity of the item: "))

total = price * quantity


print("========== RECEIPT ==========")
print("item: " + item)
print("price: #" + str(price))
print("quantity: " + str(quantity))
print("------------------------------")
print("total: #" + str(total))
print("==============================")

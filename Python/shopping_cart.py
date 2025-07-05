# Create a shopping cart programme that will continuously ask the user for a food product and the price of that product
# Have an exit clause if the user wishes to stop adding more things to their cart
# At the end show the food items and the total cost to the user

foods = []
prices = []
total = 0

while True:
    food = input("enter a food product or type done to exit: ")
    if food.lower() == 'done':
        break
    else:
        price = float(input(f"Enter the price of the {food}: R"))
        foods.append(food)
        prices.append(price)
        
print("!!!------Your cart------!!!")

for food in foods:
    print([food] + [price], end= " ")
    
for price in prices:
    total += price

print("\n")    
print(f"Your total is: R{total}")
        
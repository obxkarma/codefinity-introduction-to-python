# Declaring dictionary "grocery_inventory"
grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

# Establishing a conditional "Eggs" pricing adjustment decision loop: 
egg_value = grocery_inventory.get("Eggs", (None, 5.50, 30))

if egg_value[1] > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    new_egg_value = list(egg_value[:])
    new_egg_value[1] -= 1
    grocery_inventory["Eggs"] = tuple(new_egg_value)
else:
    print("The price of eggs is reasonable.")
    
# Adding a new category to the dictionary:
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)

# Adding a conditional restock decision: 
milk_stock = grocery_inventory.get("Milk", (None, 3.50, 8))

if milk_stock[2] < 10:
    new_milk_stock = list(milk_stock[:])
    new_milk_stock[2] += 20
    grocery_inventory["Milk"] = tuple(new_milk_stock)
    print("Milk needs to be restocked. Increasing stock by 20 units.")
else:
    print("Milk has sufficient stock.")

# Adding a conditional category removal decision:
apple_price = grocery_inventory.get("Apples", (None, 1.50, 50))

if apple_price[1] > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")
    
print("Updated inventory:", grocery_inventory)

    
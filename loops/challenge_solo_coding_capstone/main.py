# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}
# Loop through each item in the inventory dictionary
for item, stock in inventory.items():
    current_stock, regular_price, discounted_price = stock
    if stock[0] < 30:
        print(f"{item} need restocking.")
    elif stock[0] > 100:
        print(f"{item} should be sold at the discounted price of {discounted_price}.")
    else:
        print(f"{item} should be sold at the regular price of {regular_price}.")








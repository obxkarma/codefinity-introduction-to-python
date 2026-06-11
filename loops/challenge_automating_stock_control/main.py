inventory = {
    "Bread": [30, 50, 10, False],
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}
discount_threshold = 100
print("Processing initiated...")
for item, stock in inventory.items():
    print(f"Processing {item}")
#    print(f"Item: {item} | Current Stock: {stock[0]} | Minimum required stock: {stock[1]} | Restock Quantity: {stock[2]} | Sale Status: {stock[3]}")
    while stock[0] < stock[1]:
        stock[0] += stock[2]
        if stock[0] > discount_threshold:
            stock[3] = True
#    print(f"Updated stock for {item}: {stock[0]} | Updated sale status for {item}: {stock[3]}")
    print("Processing completed") 
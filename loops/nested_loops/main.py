produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce, dairy]             # 1. Combine into a list of lists

for section in groceries:                # 2. Outer loop: each sublist → section
    for item in section:                 # 3. Inner loop: each element → item
        print("Item name:", item)     
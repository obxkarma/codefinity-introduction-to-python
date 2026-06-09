# List of products with their initial stock levels at the start of the week
products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]

# List of products sold by the end of the week
units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]
for i in range(len(products)):
    product_name, original_quantity = products[i]
    sold_quantity = units_sold[i][1]
    remaining_quantity = original_quantity - sold_quantity
    products[i] = [product_name, remaining_quantity]

#print(products)

# New shipment received at the end of the week

shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]
for i in range(len(products)):
    product_name, new_quantity = products[i]
    received_quantity = shipment_received[i][1]  # Access the quantity from shipment_received using index i
    updated_quantity = new_quantity + received_quantity
    products[i] = [product_name, updated_quantity]
    
print("Final stock levels for all products:", products)
###
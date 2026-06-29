# Define a function with a default `discount` argument
def apply_discount(price, discount=0.05):
    discounted_price = price * (1 - discount)
    return discounted_price
# Define a function with a default `tax` argument
def apply_tax(price,tax=0.07):
    priceplus_tax = price * (1+tax)
    return priceplus_tax

# Function where `tax` has a default value
def calculate_total(price, discount=0.05, tax=0.07):
    total = price * (1 + tax) * (1 - discount)
    return total
    
# Call the function without providing a `discount`, using the default value
total_price = calculate_total(120)
print(f"Total cost with default discount and tax: ${total_price}")

# Call the function with custom values
total_price_custom = calculate_total(100, discount=0.10, tax=0.08)
print(f"Total cost with custom discount and tax: ${total_price_custom}")


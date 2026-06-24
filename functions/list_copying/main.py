# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Creating a function to apply a 10% discount to product prices over $2.00, without changing the original list.
def apply_discount(prices):
    # making a copy of the original list:    
    prices_copy = prices.copy()
    # iterating through the copied list:
    for i in range(len(prices_copy)):
        original_price = prices_copy[i]
        if original_price > 2.00:
            prices_copy[i] = original_price * 0.9
    return prices_copy

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)
print("Updated product prices: $", updated_prices)
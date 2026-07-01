# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    # Multiply corresponding elements
    revenue = [x * y for x, y in zip(prices, quantities_sold)]
    return revenue

revenue_per_product = list(zip(products, calculate_revenue(prices, quantities_sold)))
for product, revenue in revenue_per_product:
    print(f"{product} has total revenue of ${revenue}")

def formatted_output(revenues):
    revenues = product.sort
    return revenues

# revenues = calculate_revenue(prices, quantities_sold)
# print(product")

# Example of expected output line (do not remove):
# print(f"{products[0]} has total revenue of ${revenue[1]}")
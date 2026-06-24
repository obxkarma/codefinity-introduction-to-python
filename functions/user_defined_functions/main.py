# Defining function to calculate the total cost of a product by multiplying its price and quantity sold.
def calculate_total_cost(price, quantity_sold):
    total_cost = price * quantity_sold
    return(total_cost)

# Call the function and print the result
apples_total_cost = calculate_total_cost(1.50, 10)
print(f"The total cost for apples is ${apples_total_cost}")

def sum_prices(prices):
    total = 0
    for price in prices:
        total += price
    return total

prices = [12.99, 8.50, 15.75, 23.00, 7.25]
total = sum_prices(prices)

print(total)


start_number = 5
countdown_values = []
countdown_values.append(start_number)  # This line added to include the initial value
while start_number > 1:
    start_number -= 1
    countdown_values.append(start_number)
print(f"Discount countdown complete! {countdown_values}")
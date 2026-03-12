child = float(input(f"What is the price of a child's meal? "))
adult = float(input(f"What is the price of a adult's meal? "))
childrens = int(input(f"How many children are there? "))
adults = int(input(f"How many adults are there? "))

subtotal_children = child * childrens
subtotal_adult = adult * adults
subtotal = subtotal_children + subtotal_adult

print(f"Subtotal: ${subtotal:.2f}")

tax_rate = float(input(f"What is the sales tax rate?"))
sales_tax = subtotal * (tax_rate / 100)
total_price = subtotal + sales_tax
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total_price:.2f}")

payment = float(input("What is the payment amount? "))
change = payment - total_price
print(f"Change: ${change:.2f}")

print("\n--- Order Summary ---")
total_people = childrens + adults
print(f"Total meals served: {total_people}")
print("Thanks for the order!")

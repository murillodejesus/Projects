child = float(input(f"What is the price of a child's meal? "))
adult = float(input(f"What is the price of a adult's meal? "))
childrens = int(input(f"How many children are there? "))
adults = int(input(f"How many adults are there? "))

subtotal_children = child * childrens
subtotal_adult = adult * adults
subtotal = subtotal_children + subtotal_adult

print(f"Subtotal: ${subtotal:.2f}")


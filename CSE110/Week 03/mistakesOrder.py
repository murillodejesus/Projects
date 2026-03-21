rewards = 0
choice = "drink"
total_order = 3

if (choice == "drink" or choice == "cookie") and total_order > 5:
    rewards += 5

print(f"You have {rewards} rewards points.")

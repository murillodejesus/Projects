#Creativity: Added a 'units' list to distinguish between kilos (kg) and individual items (un).
#Implemented logic to calculate price based on weight (Weight * Price per Kg) 
#Implemented .3f to show 3 decimals for weight

def main():
    item_names = []
    item_prices = [] 
    item_units = [] 
    item_amounts = [] 

    print("Welcome to the Shopping Cart Program!")

    choice = 0

    while choice != 5:
        print("\nPlease select one of the following:")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Compute total")
        print("5. Quit")

        try:
            choice = int(input("Please enter an action: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            name = input("What item would you like to add? ")
            unit_type = input("Is this sold by unit or weight? (Enter 'un' or 'kg'): ").lower()

            try:
                if unit_type == "kg":
                    weight = float(input(f"How many kg of '{name}'? "))
                    price_per_kg = float(input(f"What is the price per kg of '{name}'? "))
                    total_item_price = weight * price_per_kg
                    
                    item_names.append(name)
                    item_amounts.append(weight)
                    item_units.append("kg")
                    item_prices.append(total_item_price)
                else:
                    qty = int(input(f"How many units of '{name}'? "))
                    price_per_un = float(input(f"What is the price per unit of '{name}'? "))
                    total_item_price = qty * price_per_un
                    
                    item_names.append(name)
                    item_amounts.append(qty)
                    item_units.append("un")
                    item_prices.append(total_item_price)

                print(f"'{name}' added to the cart.")
            except ValueError:
                print("Invalid numeric input. Item not added.")

        elif choice == 2:
            print("\nThe contents of the shopping cart are:")
            if not item_names:
                print("Your cart is empty.")
            else:
                for i in range(len(item_names)):
                    amount_str = f"{item_amounts[i]:.3f} kg" if item_units[i] == "kg" else f"{int(item_amounts[i])} un"
                    print(f"{i + 1}. {item_names[i]:<12} - {amount_str:<10} - ${item_prices[i]:.2f}")

        elif choice == 3:
            if not item_names:
                print("Nothing to remove.")
            else:
                try:
                    remove_index = int(input("Which item number would you like to remove? ")) - 1
                    if 0 <= remove_index < len(item_names):
                        item_names.pop(remove_index)
                        item_amounts.pop(remove_index)
                        item_units.pop(remove_index)
                        item_prices.pop(remove_index)
                        print("Item removed.")
                    else:
                        print("Invalid item number.")
                except ValueError:
                    print("Please enter a number.")

        elif choice == 4:
            total = sum(item_prices)
            print(f"The total price of the items in the shopping cart is ${total:.2f}")

        elif choice == 5:
            print("Thank you. Goodbye.")

if __name__ == "__main__":
    main()
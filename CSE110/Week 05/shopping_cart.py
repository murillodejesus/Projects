def main():
    item_names = []
    item_prices = []
    item_quantities = []

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
            print("Please enter a valid number (1-5).")
            continue

        if choice == 1:
            name = input("What item would you like to add? ")
            try:
                price = float(input(f"What is the price of '{name}'? "))
                qty = int(input(f"How many '{name}' would you like? "))
                
                item_names.append(name)
                item_prices.append(price)
                item_quantities.append(qty)
                print(f"'{name}' (x{qty}) has been added to the cart.")
            except ValueError:
                print("Invalid input. Price and quantity must be numbers. Item not added.")

        elif choice == 2:
            print("\nThe contents of the shopping cart are:")
            if not item_names:
                print("Your cart is empty.")
            else:
                for i in range(len(item_names)):
                    name = item_names[i]
                    price = item_prices[i]
                    qty = item_quantities[i]
                    print(f"{i + 1}. {name:<12} - ${price:.2f} (Qty: {qty})")

        elif choice == 3:
            if not item_names:
                print("Your cart is already empty.")
            else:
                for i in range(len(item_names)):
                    print(f"{i + 1}. {item_names[i]}")
                
                try:
                    remove_index = int(input("\nWhich item would you like to remove? ")) - 1
                    
                    if 0 <= remove_index < len(item_names):
                        item_names.pop(remove_index)
                        item_prices.pop(remove_index)
                        item_quantities.pop(remove_index)
                        print("Item removed.")
                    else:
                        print("Sorry, that is not a valid item number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == 4:
            total = 0
            for i in range(len(item_prices)):
                total += item_prices[i] * item_quantities[i]
            
            print(f"The total price of the items in the shopping cart is ${total:.2f}")

        elif choice == 5:
            print("Thank you. Goodbye.")
        else:
            print("That is not a valid option. Please try again.")

if __name__ == "__main__":
    main()
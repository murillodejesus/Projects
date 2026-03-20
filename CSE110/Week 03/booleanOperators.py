men = int(input("How many men are there? "))
women = int(input("How many women are there? "))

total = men + women

if total >= 7 and women >= 4:
    print("You can play!")
else:
    print("You cannot play a lega game.")
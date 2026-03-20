men = int(input("How many men are there? "))
women = int(input("How many women are there? "))

total = men + women

has_enough_players = total >= 7
has_enough_women = total >=4

print(f"We have {total} players")

if has_enough_players and has_enough_women:
    print("You can play!")
else:
    print("You cannot play a lega game.")



if not has_enough_players:
    print("Ask the other team if they want to practice")
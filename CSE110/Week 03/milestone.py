print("Welcome to the Temple of Wonders!").
print("You stand before three giant stone doors: RED, BLUE, and GOLD.")

choice1 = input("Which door do you choose? ").lower()

if choice1 == "red":
    print("\nYou enter a room filled with lava. There is a LADDER and a LEVER.")
    
    choice2 = input("Do you climb the LADDER or pull the LEVER? ").lower()
    if choice2 == "ladder":
        print("\nThe ladder leads to a helicopter pad! The PILOT asks for a PASSWORD.")
        
        choice3 = input("Do you try to GUESS the password or HIJACK the helicopter? ").lower()
        if choice3 == "guess":
            print("\nYou guess '1234'. The pilot laughs and lets you in. Where to?")
            
            choice4 = input("Fly to HAWAII or the MOON? ").lower()
            if choice4 == "hawaii":
                print("\nEnjoy the beach! YOU WIN!")
            elif choice4 == "moon":
                print("\nOut of fuel halfway there... floating forever. GAME OVER.")
            else:
                print("\nYou took too long to decide and crashed. GAME OVER.")
                
        elif choice3 == "hijack":
            print("\nThe pilot was a karate master. You got kicked out. GAME OVER.")
        else:
            print("\nThe pilot flew away without you.")

    elif choice2 == "lever":
        print("\nA trapdoor opens and you fall into a pit of marshmallows. You're stuck!")
    else:
        print("\nYou hesitated too long and the floor melted. GAME OVER.")

elif choice1 == "blue":
    print("\nYou enter a frozen cavern. You see a sleeping DRAGON and a SHINY CHEST.")
    
    choice2 = input("Do you poke the DRAGON or open the CHEST? ").lower()
    if choice2 == "dragon":
        print("\nThe dragon wakes up and offers you a ride. He asks: LEFT or RIGHT?")

        choice3 = input("Do you go LEFT toward the mountains or RIGHT toward the sea? ").lower()
        if choice3 == "left":
            print("\nYou find a hidden village! They offer you a CROWN or a SWORD.")
            
            choice4 = input("Do you take the CROWN or the SWORD? ").lower()
            if choice4 == "crown":
                print("\nYou are now the King of the Mountains! YOU WIN!")
            elif choice4 == "sword":
                print("\nYou accidentally drop it on your foot. Ouch. GAME OVER.")
            else:
                print("\nThe villagers think you're rude for not choosing. GAME OVER.")
                
        elif choice3 == "right":
            print("\nA sea monster eats the dragon. Nature is cruel. GAME OVER.")
        else:
            print("\nThe dragon gets bored and goes back to sleep.")

    elif choice2 == "chest":
        print("\nIt was a mimic! The chest eats your lunch and runs away.")
    else:
        print("\nYou froze solid while deciding. Better luck next time!")

elif choice1 == "gold":
    print("\nYou find a library with three books: TALL, SHORT, and DUSTY.")
    choice2 = input("Which book do you read? ").lower()
    if choice2 == "tall":
        print("\nYou learn the secret of flight and soar away!")
    elif choice2 == "short":
        print("\nIt's a joke book. You laugh so hard you forget to leave. You live here now.")
    elif choice2 == "dusty":
        print("\nA ghost flies out and gives you a high-five. You are now haunted (but happy).")
    else:
        print("\nThe library disappears because you didn't pick a book.")

elif choice1 == "dance":
    print("\nYou start dancing. The temple walls crumble to reveal a DISCO! YOU WIN!")

else:
    print("\nThat wasn't an option. The temple guards escort you out for being indecisive.")
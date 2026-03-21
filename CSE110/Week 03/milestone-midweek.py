print("You are standing at the edge of a misty lake. You see a BOAT and a PATH.")

choice1 = input("Do you want to take the BOAT or follow the PATH? ").lower()

if choice1 == "boat":
    print("You climb into the creaky wooden boat and begin to row into the mist...")
    
elif choice1 == "path":
    print("You decide to stay on solid ground and head down the dark, winding path.")

else:
    print("That wasn't an option. While you hesitated, the mist swallowed you up.")
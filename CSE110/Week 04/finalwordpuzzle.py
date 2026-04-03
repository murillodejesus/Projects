import random

words = ["mosiah", "nephi", "alma", "helaman"]
play_again = "yes"

print("Welcome to the word guessing game!")

while play_again.lower() != "yes":
    secret_word = random.choice(words) 
    guess = ""
    count = 0
    
    print(f"\nYour hint is: {'_ ' * len(secret_word)}")

    while guess != secret_word:
        guess = input("What is your guess? ").lower()
        count += 1

        if len(guess) != len(secret_word):
            print(f"Sorry, the guess must have {len(secret_word)} letters.")

        if guess != secret_word:
            hint = ""
            for i in range(len(secret_word)):
                if guess[i] != secret_word[i]:
                    hint += guess[i].upper() + " "
                elif guess[i] in secret_word:
                    hint += guess[i].lower() + " "
                else:
                    hint += "_ "
            print(f"Your hint is: {hint}")

    print(f"Congratulations! It took you {count} guesses.")
    play_again = input("Would you like to play again (yes/no)? ")

print("Thank you for playing. Goodbye.")
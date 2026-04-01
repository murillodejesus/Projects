secret_word = "mosiah"
guess = ""
guess_count = 0

print("Welcome to the word guessing game!")

initial_hint = ""
for i in range(len(secret_word)):
    initial_hint += "_ "
print(f"Your hint is: {initial_hint}")

while guess.lower() != secret_word:
    guess = input("What is your guess? ").lower()
    guess_count += 1
    
    if len(guess) != len(secret_word):
        print(f"Sorry, the guess must have {len(secret_word)} letters.")
    
    elif guess != secret_word:
        hint = ""
        for i in range(len(secret_word)):
            
            if guess[i] == secret_word[i]:
                hint += guess[i].upper() + " "
            
            elif guess[i] in secret_word:
                hint += guess[i].lower() + " "
           
            else:
                hint += "_ "
        print(f"Your hint is: {hint}")

print("Congratulations! You guessed it!")
print(f"It took you {guess_count} guesses.")
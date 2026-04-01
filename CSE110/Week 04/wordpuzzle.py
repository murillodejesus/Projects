secret_word = "mosiah"
guess = ""
guess_count = 0

print("Welcome to the word guessing game!")

while guess.lower() != secret_word:
    guess = input("What is your guess? ")
    guess_count += 1
    
    if guess.lower() != secret_word:
        print("Your guess was not correct.")

print("Congratulations! You guessed it!")
print(f"It took you {guess_count} guesses.")
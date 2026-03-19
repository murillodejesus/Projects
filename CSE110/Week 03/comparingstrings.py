animal = input("What is your favorite animal? ")
animal_lc = animal.lower()
sound = ""

if animal_lc == "cat":
    sound ="meow"
elif animal_lc == "dog":
    sound = "ruff"
else:
    sound = "unknown"

print(f"The {animal} makes the sound: {sound}.")
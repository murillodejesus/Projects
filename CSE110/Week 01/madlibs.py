print ("Please enter the following:")

adjective = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
exclamation = input("exclamation: ")
verb2 = input("verb: ")
verb3 = input("verb: ")
place = input("a place: ")

exclamation_formatted = exclamation.capitalize()

first_letter = adjective[0].lower()
if first_letter in "aeiou":
    article = "an"
else:
    article = "a"

print("Your story is:")
print()

story = (
    f"The other day, I was really in trouble. It all started when I saw {article} very\n"
    f"{adjective} {animal} {verb1} down the hallway. \"{exclamation_formatted}!\" I yelled. But all\n"
    f"I could think to do was to {verb2} over and over. Miraculously,\n"
    f"that caused it to stop, but not before it tried to {verb3}\n"
    f"right in front of my family. I eventually ran to the {place} to hide!"
)

print(story)
print()
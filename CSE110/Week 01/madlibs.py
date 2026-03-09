print ("Please enter the following:/n")

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

print("/n Your story is:/n")

story = (
    
)
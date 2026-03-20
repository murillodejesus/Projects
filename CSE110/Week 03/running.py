temperature = float(input("What is the temperature outseide? "))

if temperature < 5:
    print("It is too cold. Don't go!")
elif temperature < -15:
    print("Ask some other quwestions...")
else:
    print("Enjoy your run.")
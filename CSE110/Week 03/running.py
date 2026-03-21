temperature = float(input("What is the temperature outseide? "))

if temperature < -15:
    print("It is too cold. Don't go!")
elif temperature < 5:
    weather = input("What is the weather like (snow,rain, sunny)? ")

    if weather == "snow":
        print("Better stay inside")
    elif weather == "rain":
        print("Go ahead and run, but bring rain gear.")
    elif weather == "sunny":
        print("Dress warm and enjoy!")
    else:
        print("I don't understand that response.")
else:
    print("Enjoy your run.")
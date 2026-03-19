temperature = float(input ("What is your temperature in degrees Celsius? "))
if temperature > 40.5:
    print("Go to the hospital!")
elif temperature > 39.4:
    print("Call your Doctor.")
else:
    print("Consider rest or medicine.")

print("Have a good day")
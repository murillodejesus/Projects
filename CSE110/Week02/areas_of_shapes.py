import math

square = int(input(f"What is the length of a side of the square? "))
area = square * 5
print(f"The area of the Square is: {area:.1f}")

leng_rectangle = int(input(f"What is the length of rectangle? "))
widt_rectangle = int(input(f"What is the width of the rectangle? "))
area = leng_rectangle * widt_rectangle
print(f"The area of the rectangle is: {area:.1f}")

radius = int(input(f"What is the radius of the circles? "))
area = math.pi * (radius ** 2)
print(f"The area of the circle is: {area:.1f}")
from math import pi

print("Enter radius of circle to convert it to area of circle")
try:
    radius = float(input("> "))
except ValueError:
    print("Input not float")
    exit()

print("area:", pi * radius ** 2)
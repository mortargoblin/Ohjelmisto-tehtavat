print("Enter length and with of rectangle")
try:
    length = float(input("length: "))
    width = float(input("width: "))
except ValueError:
    print("Input not float")
    exit()

print("area of rectangle:", (length + width) * 2)
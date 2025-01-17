# Convert inches to cm :))

print("Enter inches to convert to cm. Enter negative value to stop")
while True:
    inch = float(input("> "))
    if inch < 0:
        break
    else:
        cm = inch * 2.54
        print(cm, "cm", sep="")


# Cabin class selector

print("Enter desired cabin class")
print("LUX, A, B, C")

choice = input("> ")

if choice == "LUX":
    print("upper-deck cabin with a balcony")
elif choice == "A":
    print("above the car deck, equipped with a window")
elif choice == "B":
    print("windowless cabin above the car deck")
elif choice == "C":
    print("windowless cabin below the car deck")
else:
    print("choice not listed above")
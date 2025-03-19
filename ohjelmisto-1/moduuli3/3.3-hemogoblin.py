# Hemogoblin level determiner

print("Enter sex (M/F)")
sex = input("> ")

# check correct sex choice
if sex.lower() != "m" and sex.lower() != "f":
    print("sex not M or F")
else:
    print("Enter hemogoblin value (g/l)")
    goblin = float(input("> "))

    # determine hemogoblin health
    if sex.lower() == "m" and 117 <= goblin:
        if goblin <= 155:
            print("hemogoblin good")
        else:
            print("hemogoblin too high")
    elif sex.lower() == "f" and 134 <= goblin:
        if goblin <= 167:
            print("hemogoblin good")
        else:
            print("hemogoblin too high")
    else:
        print("hemogoblin too low")
# Zander siz

print("Enter size of zander (in cm)!")

# en jaksa errorihallintaa
zander_size = float(input("> "))

if zander_size < 42:
    print(f"Fish too small! By {42 - zander_size}cm!")
    print("Release the fish! NOW!")
else:
    print("Fish sufficient size!")
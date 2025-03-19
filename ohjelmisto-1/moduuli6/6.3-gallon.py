# galloneista litraa

def main():
    print("Enter gallons to convert")
    user_input = float(input("> "))
    print(f"result: {gallon_to_liter(user_input)} l")


def gallon_to_liter(gallon):
    return gallon * 3.785

main()

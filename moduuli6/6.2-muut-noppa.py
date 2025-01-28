# Noppaa

def main():
    print("Enter the number of sides the dice should have")
    user_input = int(input("> "))
    while True:
        # käyttäjä valitsee nopan sivujen määrän
        result = dice(user_input)
        print(result)
        if result == user_input:
            break
        else:
            pass

def dice(max):
    from random import randint
    return randint(1,max)

main()
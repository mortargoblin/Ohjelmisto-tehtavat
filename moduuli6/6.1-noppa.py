# Noppaa

def main():
    while True:
        result = dice()
        print(result)
        if result == 6:
            break
        else:
            pass

def dice():
    from random import randint
    return randint(1,6)

main()
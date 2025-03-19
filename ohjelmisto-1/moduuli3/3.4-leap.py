# Leap year calculator

# käytän omia funktioita sillä se on tässä järkevämpää
def main():
    print("Enter year")

    choice = int(input("> "))

    if is_leap(choice):
        print("Year is leap year")
    else:
        print("Year is not leap year")
        
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False


main()
# Kuukaudet ja vuodenajat
def main():
    seasons = "kevät", "kesä", "syksy", "talvi"

    print("Kirjoita kuukausi luvulla")
    month_num = int(input("> "))
    if 2 < month_num <= 5:
        print(seasons[0])
    elif 5 < month_num <= 8:
        print(seasons[1])
    elif 8 < month_num <= 11:
        print(seasons[2])
    elif month_num == 12 or 1 <= month_num <= 2:
        print(seasons[3])
    else:
        print("Number not a month")
    

main()
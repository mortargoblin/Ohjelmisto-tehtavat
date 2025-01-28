# Integer sum

def main():
    int_list = []
    print("Enter integers to add together. Enter nothing when ready")
    while True:
        user_input = input("> ")
        if user_input == "":
            break
        else:
            int_list.append(int(user_input))
    print(int_list)
    print(summa(int_list))

# En ymmärrä miksi joudun tekemään tämän funktion
# vaikka pythonin sisäänrakennettu summafunktio 
# riittäisi. Jos haluatte jonkun for-loopin tms 
# tähän voin senkin lisätä. 

def summa(lista):
    return sum(lista)

main()
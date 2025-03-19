# Remove odd numbers from list

def main():
    print("Enter list of integers. One integer per line. Enter nothing when ready")
    lista = []
    while True:
        user_input = input("> ")
        if user_input == "":
            break
        else:
            lista.append(int(user_input))
    print(remove_odd_nums(lista))


def remove_odd_nums(lista):
    for i in lista:
        if i % 2 == 0:
            pass
        else:
            lista.remove(i)
    return lista

main()
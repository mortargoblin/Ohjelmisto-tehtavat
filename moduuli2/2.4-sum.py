print("Enter 3 integers")
try:
    int_1 = int(input("int 1: "))
    int_2 = int(input("int 2: "))
    int_3 = int(input("int 3: "))
except ValueError:
    print("Input not integer!")

result_sum = int_1 + int_2 + int_3
result_product = int_1 * int_2 * int_3
result_average = (int_1 + int_2 + int_3) / 3

print(f"sum: {result_sum}, product: {result_product}, average: {result_average}")
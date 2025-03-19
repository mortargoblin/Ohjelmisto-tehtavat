# Numberss

print("Enter integers. Enter nothing to quit")

num_list = []

while True:
    num = input("> ")
    if num == "":
        break
    else:
        num_list.append(int(num))

print("Smallest value:", min(num_list), "Largest value:", max(num_list))

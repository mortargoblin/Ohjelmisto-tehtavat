# Lista

print("Enter numbers to list. Enter nothing when ready. Enter no less than five.")

l = []
while True:
    num = input("> ")
    if num == "":
        break
    else:
        l.append(float(num))

l.sort(reverse=True)

print("5 greatest numbers in descending order:")
for i in range(5):
    print(l[i], end=" ")
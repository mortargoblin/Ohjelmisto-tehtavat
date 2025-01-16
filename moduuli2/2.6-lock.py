# Combination lock

min1 = 0
max1 = 9

min2 = 1
max2 = 6

from random import randint

print("Two random combinations")

print("\n3-digit combination with numbers between 0 and 9")
print(randint(min1, max1), randint(min1, max1), randint(min1, max1))

print("\n4-digit combination with numbers between 1 and 6")
print(randint(min2, max2), randint(min2, max2), randint(min2, max2), randint(min2, max2))
# Combination lock

from random import randint

print("Two random combinations")

print("\n3-digit combination with numbers between 0 and 9")
print(randint(0, 9), randint(0, 9), randint(0, 9))

print("\n4-digit combination with numbers between 1 and 6")
print(randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6))
# Dice roll

from random import randint

print("Enter number of dice to roll")
n = int(input("> "))
result = 0

for _ in range(n):
    result += randint(1, 6)

print(result)
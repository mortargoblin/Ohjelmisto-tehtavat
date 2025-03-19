# User tries to guess random integer

from random import randint

print("Try to guess a random integer between 1 and 10")
correct = randint(1, 10)

while True:
    answer = int(input("> "))
    if answer == correct:
        print("Correct!")
        break
    elif answer > correct:
        print("too high")
    else:
        print("too low")
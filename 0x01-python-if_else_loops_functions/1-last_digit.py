#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digt = abs(number) % 10
if digt > 5:
    print(f"Last digit of {number} is {digt} and is greater than 5")
elif digt == 0:
    print(f"Last digit of {number} is {digt} and is 0")
else:
    if number < 0:
        digt = -digt
        print(f"Last digit of {number} is {digt} and is less than 6 and not 0")
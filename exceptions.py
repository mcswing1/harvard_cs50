#!/usr/bin/env python3.10
#Reference URL: https://www.youtube.com/watch?v=vzGllw18DkA&t=257s - 4:02:20

# Import the sys module to give us access to gracefully exit the program.
import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    # Exit the program with a status code of 1 (1 usually means something went wrong)
    sys.exit(1)

print(f"{x} / {y} = {result}")

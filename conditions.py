#!/usr/bin/env python3.10
#Reference URL: https://www.youtube.com/watch?v=vzGllw18DkA&t=257s - 3:08:34

# Variable n received as a string. Use the int function to convert the string to an integer.  
n = int(input("Number: "))

if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")



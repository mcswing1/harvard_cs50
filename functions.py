#!/usr/bin/env python3.10
#Reference URL: https://www.youtube.com/watch?v=vzGllw18DkA&t=257s - 3:36:04

# The "square" function is taking a single input "x." If we wanted to have multiple inputs, they would just need to be separated by a comma.
def square(x):
    return x * x

# We are going to loop 10 times and for each loop, plug in the value of "i" and then plug in the square function using "i" as an input.
for i in range(10):
    print(f"The square of {i} is {square(i)}")


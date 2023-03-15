#!/usr/bin/env python3.10
#Reference URL: https://www.youtube.com/watch?v=vzGllw18DkA&t=257s - 3:38:15

# Import a function from an external file
from squareFunctionExternal import square

# We are going to loop 10 times and for each loop, plug in the value of "i" and then plug in the square function using "i" as an input.
for i in range(15):
    print(f"The square of {i} is {square(i)}")


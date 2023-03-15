#!/usr/bin/env python3.10
#Reference URL: https://www.youtube.com/watch?v=vzGllw18DkA&t=257s - 3:39:50

# Import the whole "squareFunctionExternal" module instead of just a specific function 
import squareFunctionExternal

# We are going to loop 10 times and for each loop, plug in the value of "i" and then plug in the square function using "i" as an input.
for i in range(5):
    # In order to access the "square" function inside the "squareFunctionExternal" module, we have to preface "square" with the module name.
    print(f"The square of {i} is {squareFunctionExternal.square(i)}")


#!/usr/bin/env python3.10
#Reference URL: https://www.youtube.com/watch?v=vzGllw18DkA&t=257s - 3:54:44

# A decorator is a function that takes a function as input and returns a modified version of that function as output.
# This is different from other programming languages where functions exist on their own and can't be passed as input or output. In Python, functions are values like any other.

# Announce function will take as input, a function called "f." 
# 2. The hello() function is the input function. 
def announce(f):
    # This new function will wrap up function "f" with some additional behavior, so this is called a wrapper function.
    # The ammounce function will take "f" and create a new function that announces via print statements that the function is running. We return the new function.
    def wrapper():
        print("About to run the function...")
        # 3. The hello() function is run.
        f()
        print("Done with the function.")
    return wrapper

# 1. The hello() function is wrapped inside the announce function.
@announce
def hello():
    print("Hello, world!")

# Call the hello() function
hello()

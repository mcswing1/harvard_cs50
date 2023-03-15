#!/usr/bin/env python3.10
#Reference URL: https://www.youtube.com/watch?v=vzGllw18DkA&t=257s - 3:42:23

# A class is a template for a type of object.
class Point():
    # __init__ is the method/function that is automatically called whenver I try to create a new Point.
    # __init__ takes a couple of arguments. "self" represents that object in that we are currently dealing with. 
    def __init__(self, input1, input2):
        # The arguements "input1" and "input2" are going to be stored inside the "self" object in properties called "x" and "y"
        self.x = input1
        self.y = input2

# "self" argument is provided automatically to the "p" object
p = Point(2, 8)
# Go into the Point object and access its x value and access its y value
print(p.x)
print(p.y)


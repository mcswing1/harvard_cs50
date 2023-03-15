#!/usr/bin/env python3.10
#Reference URL: https://www.youtube.com/watch?v=vzGllw18DkA&t=257s - 3:47:00

# A class is a template for a type of object.
class Flight():
    # __init__ is the method/function that is automatically called whenver I try to create a new Point.
    # __init__ takes a couple of arguments. "self" represents that object in that we are currently dealing with. 
    def __init__(self, capacity):
        # The arguements "input1" and "input2" are going to be stored inside the "self" object in properties called "x" and "y"
        self.capacity = capacity
        self.passengers = []

    # Method (aka function) for adding a new passenger
    # Since this method will work on an indvidual object, we need someway to reference that object. We use "self" here as well.
    def add_passenger(self, name):
        #Equivalent to if self.open_seats() == 0: but written in a more Pythonic format
        if not self.open_seats():
            return False    
        self.passengers.append(name)
        return True

    # Returns the number of open seats
    def open_seats(self):
        return self.capacity - len(self.passengers)

# Flight capacity is 3
flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    # For each person, add the person to the flight and store the result in the success variable
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}.")



#!/usr/bin/env python3.10
#Reference URL: https://www.youtube.com/watch?v=vzGllw18DkA&t=257s - 3:58:03

# In Python, we have the ability to nest data structures within each other (i.e. lists inside of a list, lists inside of a dictionary, dictionary inside of a list)
# The nesting feature is one of the reasons why it is easier to represent structured data in Python.
people = [
    # This list of people is a dictionary, instead of a string.
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# The first way of doing the sort is by defining a function "f" and calling that "f" function as an argument for the sort function below.
# We define a function called "f" that will tell the sort function what to look at in order to do the sort. 
#def f(person):
#    return person["name"]

# Sort by name
#people.sort(key=f)

# The second way of doing the sort is to use a lambda function to create short, one-line function
# The lambda will take a person as an input and return the person's name. 
people.sort(key=lambda person: person["name"])

print(people)


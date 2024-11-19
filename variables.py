# variables in python
'''
variables are containers for storing data values
variables are used to store data values
'''

name = "Abu Bakar"
print(name) #Output single Variable
age = 26
print(f"My name is {name} and my age is {age}") #Output Multiple Variables

# Python - Variable Names
'''
    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)
    A variable name cannot be any of the Python keywords.
'''

# Python Variables - Assign Multiple Values

x, y, z = "Orange", "Banana", "Cherry" #Note: Make sure the number of variables matches the number of values, or else you will get an error.


print(f'x = {x}, y = {y}, z = {z}')

# One Value to Multiple Variables

a = b = c = "Orange"

print(f'a = {a}, b = {b}, c = {c}')

# local and global variables in python

comment = "awesome" # global variable

def myfunc():
  comment = "fantastic" # local variable
  print("Python is " + comment) # Output: Python is fantastic! Here according to local variable

myfunc()

print("Python is " + comment) # Output: Python is awesome! here according to global variable

# Another alternative to declare global variable
def myfunc1():
  global p
  p = "fantastic"
  print(f"Python is very {p}")

myfunc1()

print("Python is " + p)

#In VS Code, create a module titled geometry and add two functions in there. 


# One that will calculate the area of a circle given a radius. 

# area = pi r ^2

import math

def circle_area(r):
    area = math.pi * r ** 2
    return float(area)

# The second will find the hypotenuse of a right angle given the two sides. 
# a**2 + b**2 = c**2
def hypotenuse(a,b):
    hypotenus = a**2 + b**2
    return hypotenus ** 2 

# Import the module or the functions from the module and use it to find the answers to the below questions
# A wire is the form of Arc at an angle of 60 degrees and the radius of the arc is 42. The wire is converted into a square. Find the area of the square.

import math
theta = 60
radius = 42

length = (theta/360) * (2 * math.pi * radius) 

side  = length/4

area = side ** 2

print("Area of the square = ", area ,"cm^2")
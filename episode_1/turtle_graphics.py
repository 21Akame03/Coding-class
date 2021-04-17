from turtle import *
from math import pi# use the turtle library
space = Screen()        	# create a turtle screen (space)
zari = Turtle()         	# create a turtle named zari
alicia = Turtle()

def tcircle(radius, turtle):

	def regular_polygon(l, n, turtle):
		"""draws a regular polygon of n amount sides of length l
		that is supposed to appear like a circle.
		function by cdlane from a stackoverflow post"""
		if turtle == alicia :
			for _ in range(n):
				turtle.backward(l)
				turtle.left(360 / n)
		else :
			for _ in range(n):
				turtle.forward(l)
				turtle.left(360 / n)


	#circumference (c)= 2*pi*radius
	circumference = 2 * pi * radius


	#n = amount of lines or corners, it defines the accuracy of the circle
	number_of_corners = 30 # lower number to decrease drawing time (can be any float or int)

	#circumference (c) = ca.  l * n
	#l = length of individual lines
	length = circumference / number_of_corners


	# call on the function
	regular_polygon(int(length),number_of_corners, turtle)
	
    
# count from 20 to 210 incrementing by 5
for i in range(20, 210, 5):
	#circle_example
	tcircle(i, alicia)
	tcircle(i, zari)
	print(i)
	
l = input("")

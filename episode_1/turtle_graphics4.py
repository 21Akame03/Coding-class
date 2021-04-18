import turtle
import random

pravind = turtle.Screen()
pravind.bgcolor("black")
zari = turtle.Pen()

print (pravind.screensize())

zari.speed(0)

for x in range(0, 60):
    red = random.randint(0, 100)/ 100.0
    blue= random.randint(0, 100)/ 100.0
    green = random.randint(0, 100)/ 100.0

    zari.color(red, blue, green)

    zari.begin_fill()
    zari.circle(random.randint(10, 200))
    zari.end_fill()

    zari.up()
    x_coordinate = random.randint(-600, 600)
    y_coordinate = random.randint(-200, 200)
    zari.goto(x_coordinate, y_coordinate)
    zari.down()

    direction = random.randint(0, 360)
    zari.seth(direction)



input = input('')
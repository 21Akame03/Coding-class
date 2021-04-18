import turtle as t

#create a turtle screen
pravind = t.Screen() 


for x in range(0, 10):
    t.forward(45)
    t.left(45)
    t.left(180)
    t.forward(100)

print(t.position())
t.penup()
t.goto(400,0)
t.pendown()

for x in range(0, 5):
    t.forward(45)
    t.circle(20)
    t.left(90)
    t.forward(45)

t.penup()
t.goto(-400,0)
t.pendown()

for x in range(0, 3):
    t.forward(45)
    t.right(60)
    t.forward(50)
    t.left(180)
    t.forward(45)
    t.circle(20)

t.penup()
t.goto(0, 200)
t.pendown()

for x in range(0, 4):
    print(x)
    t.left(30)
    t.forward(45)
    t.left(60)
    t.forward(45)
    t.left(90)
    t.forward(45)
    t.circle(20)
    t.left(180)
    t.forward(45)
    t.left(270)
    t.forward(45)

t.penup()
t.goto(500, 200)
t.pendown()  

for x in range(0, 10):
    print(x)
    t.left(30)
    t.forward(45)
    t.left(60)
    t.forward(45)
    t.left(90)
    t.forward(45)
    t.circle(20)
    t.left(45)
    t.left(180)
    t.forward(45)
    t.left(270)
    t.forward(45)


input = input("")
import turtle
# begging 
t = turtle.Turtle()

t.speed(0)
# here is where i start the art
t.color("hot pink")

for i in range (250) :
    t.forward(3 + i)
    t.left(72 + 1) 

t.penup()
t.goto(0,0)
t.pendown()

t.color("light pink")

for i in range (300) :
    t.forward(7 + i)
    t.left(72 + 1) 

t.penup()
t.goto(0,0)
t.pendown()

t.color("Crimson")

for i in range (250) :
    t.forward(4 + i)
    t.left(72 + 1)

t.penup()
t.goto(0,0)
t.pendown() 

t.color("pink")

for i in range (250) :
    t.forward(20 + i)
    t.left(72 + 1) 

t.penup()
t.goto(0,0)
t.pendown()

t.color("salmon")

for i in range (250) :
    t.forward(9 + i)
    t.left(72 + 1) 

t.penup()
t.goto(0,0)
t.pendown()

t.color("hotpink")

for i in range (250) :
    t.forward(10 + i)
    t.left(72 + 1) 

t.penup()
t.goto(0,0)
t.pendown()

t.color("red")

for i in range (250) :
    t.forward(4 + i)
    t.left(45 + 1) 

t.penup()
t.goto(0,0)
t.pendown()

t.color("light pink")

for i in range (250) :
    t.forward(3 + i)
    t.left(45 + 1) 

t.penup()
t.goto(0,0)
t.pendown()

t.penup()
t.goto(0,0)
t.pendown()
# very end :)
turtle.exitonclick()
# ###############################################
# ### SETUP ###
import turtle
# ###############################################

t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("red")
t.pendown()

for i in range(3):
    t.forward(100)
    t.left(120)



# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################



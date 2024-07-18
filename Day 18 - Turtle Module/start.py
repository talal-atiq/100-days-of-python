from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
# tim.shape("turtle")
tim.color("indigo")

# Creating a square using turtle:

# for i in range(4):
#     tim.forward(250)
#     tim.right(90)

# tim.pendown()
# for _ in range(5):    
#     tim.pd()
#     tim.fd(15)
#     tim.pu()
#     tim.fd(15)
#     tim.pd()
#     tim.fd(15)
#     tim.pu()
#     tim.fd(15)
#     tim.right(90)
    
# Creating all the different shapes:
tim.pensize(5)
tim.penup()
tim.goto(0, 50)
tim.pendown()


colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'brown', 'black', 'cyan']
temp = 3
for i in range(8):
    tim.color(random.choice(colors))
    for _ in range(temp):
        tim.right(360 / temp)
        tim.fd(100)
    temp = temp + 1
    
screen.exitonclick()
from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
tim.pensize(10)
tim.speed(10)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
turn_choices = [0, 90, 180, 360]

for i in range(500):
    tim.color(random.choice(colours))
    tim.right(random.choice(turn_choices))
    tim.forward(35)


screen.exitonclick()
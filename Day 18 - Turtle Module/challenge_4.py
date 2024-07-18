from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
tim.pensize(3)
pastel_colors = [
    "#FFB3BA",  # Light Pink
    "#FFDFBA",  # Peach
    "#FFFFBA",  # Light Yellow
    "#BAFFC9",  # Light Green
    "#BAE1FF",  # Light Blue
    "#B0E0E6",  # Powder Blue
    "#D8BFD8",  # Thistle
    "#FFDAB9",  # Peach Puff
    "#E6E6FA",  # Lavender
    "#FFCCCB",  # Light Red
    "#FFC3A0",  # Apricot
    "#FFB6C1",  # Light Pink
    "#FFD700",  # Light Gold
    "#E0FFFF",  # Light Cyan
    "#F0E68C",  # Khaki
    "#FFEB3B",  # Bright Yellow
]
screen.bgcolor("black")
tim.speed("fastest")
for i in range(360):
    tim.color(random.choice(pastel_colors))
    tim.circle(75)
    tim.left(5)

screen.exitonclick()
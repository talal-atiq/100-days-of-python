from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh_food()
        
    
    def refresh_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 275)
        self.goto(random_x, random_y)
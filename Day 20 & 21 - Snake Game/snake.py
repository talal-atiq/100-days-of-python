from turtle import Turtle
SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.initial_snake = []
        self.create_snake()
    
    def create_snake(self):
        for position in SNAKE_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self, position):
        snake = Turtle()
        snake.color("blue")
        snake.shape("square")
        snake.penup()
        snake.goto(position)
        self.initial_snake.append(snake)
        
    
    def extend_snake(self):
        self.add_segment(self.initial_snake[-1].position())


    def move(self):
        for snake_segment in range(len(self.initial_snake) - 1, 0, -1):
            new_x = self.initial_snake[snake_segment - 1].xcor()
            new_y = self.initial_snake[snake_segment - 1].ycor()
            self.initial_snake[snake_segment].goto(new_x, new_y)
        self.initial_snake[0].forward(20)
    
    def move_up(self):
        if self.initial_snake[0].heading() != 270:
            self.initial_snake[0].setheading(90)           
    
    def move_down(self):
        if self.initial_snake[0].heading() != 90:
            self.initial_snake[0].setheading(270)
        
    def move_right(self):
        if self.initial_snake[0].heading() != 180:
            self.initial_snake[0].setheading(0)

    def move_left(self):
        if self.initial_snake[0].heading() != 0:
            self.initial_snake[0].setheading(180)

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from tkinter import PhotoImage

import time

screen = Screen()
screen.setup(width=600, height=600)
# screen.bgcolor("black")
screen.bgpic("background.gif")
screen.title("Snake Game")
icon = PhotoImage(file='snake-game.png')  # Use a .png and convert it if needed
screen._root.iconphoto(False, icon)
screen.tracer(0)

snake = Snake()
food = Food()
scores = Scoreboard()

# Binding Keys:
screen.listen()    
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detecting Collisons with the food:
    if snake.initial_snake[0].distance(food) < 15:
        print("HIT")
        food.refresh_food()
        snake.extend_snake()
        scores.increase_score()
    
    # Detecting collisons with the wall:
    if snake.initial_snake[0].xcor() > 280 or snake.initial_snake[0].xcor() < -280 or snake.initial_snake[0].ycor() > 280 or snake.initial_snake[0].ycor() < -280:
        game_on = False
        scores.game_over()
    
    # Detecting collisons with the tail:
    for snake_segments in snake.initial_snake[1:]:
        if snake.initial_snake[0].distance(snake_segments) < 10:
            game_on = False
            scores.game_over()

screen.exitonclick()
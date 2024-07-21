from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.title("Ping Pong")
screen.tracer(0)
screen.bgpic("bg.gif")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scores = Scoreboard()



# Paddle Controls:
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    # Detecting collisons w the wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting collisons with the paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # Detecting the ball miss:
    # If ball misses the right paddle:
    if ball.xcor() > 380:
       ball.reset_ball()
       scores.l_point()
    
    # Misses the left paddle
    if ball.xcor()< -380:
        ball.reset_ball()
        scores.r_point()   
    
screen.exitonclick()
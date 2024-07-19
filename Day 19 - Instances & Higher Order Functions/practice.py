from turtle import Turtle, Screen

tim = Turtle()
tim.color("red")

# function for our key binder:
def move_fd():
    tim.fd(15)
    
def move_bd():
    tim.backward(15)

screen = Screen()

screen.listen()

screen.onkey(move_fd, "d") # When we use functions as argumnets, we don't actually use parenthesis
screen.onkey(move_bd, "a")

screen.exitonclick()

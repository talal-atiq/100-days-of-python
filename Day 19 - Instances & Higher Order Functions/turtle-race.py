from turtle import Turtle, Screen
import random

racing_board = Screen()
racing_board.setup(width=520, height=435)

# Creating turtles and adding them to the list:
turtles = []
for turtle in range(5):
    t = Turtle()
    t.shape("turtle")
    turtles.append(t)

# Assigning turtles the colors:
colors = ["red", "blue", "green", "orange", "purple"]
for i in range(5):    
    turtles[i].color(colors[i])


def starting_position(turtles):
    temp = -200
    for t in turtles:
        t.penup()
        t.goto(x = -250, y = temp)
        temp = temp + 100
        t.pendown()
    
starting_position(turtles)
user_bet = racing_board.textinput(title="Make your bet!", prompt="Color of the turtle you want to bet on: ")

movements = [0, 3, 5, 7, 10, 12, 15]

flag = True
while flag:
    for turtle in turtles:
        turtle.forward(random.choice(movements))
        if turtle.position()[0] >= 240:
            winner = turtle.pencolor()
            flag = False

# Bet Check:
if user_bet != winner:
    print(f"You lost the bet! The winner was {winner}. ggs =)")
else:
    print(f"Your bet {user_bet} won by finishing first! Congrats!")    

racing_board.exitonclick()
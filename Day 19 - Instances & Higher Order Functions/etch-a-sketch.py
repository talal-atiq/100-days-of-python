from turtle import Turtle, Screen

sketch = Turtle()
whiteboard = Screen()
sketch.speed("fastest")


whiteboard.listen()

def move_fd():
    sketch.fd(10)

def move_bd():
    sketch.backward(10)
    
def rotate_left():
    sketch.left(5)

def rotate_right():
    sketch.right(5)

def reset():
    sketch.clear()
    sketch.home()
    
# Key Bindings:
whiteboard.onkey(move_fd, "w")
whiteboard.onkey(move_bd, "s")
whiteboard.onkey(rotate_left, "a")
whiteboard.onkey(rotate_right, "d")
whiteboard.onkey(reset, "c")

whiteboard.exitonclick()

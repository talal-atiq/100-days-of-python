from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # wood_color = (139/255, 69/255, 19/255)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.update_scoreboard()        
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()        
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier", 23, "bold"))
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=("Courier", 23, "bold"))

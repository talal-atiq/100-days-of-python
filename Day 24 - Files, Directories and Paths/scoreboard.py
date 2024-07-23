from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.update_scoreboard()        
        
    def high_score(self):
        with open("highscore.txt", mode="r") as file:
            self.highscore = int(file.read())
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()        
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center", font=("Courier", 23, "bold"))
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over!", align="center", font=("Courier", 23, "bold"))
    
    def reset_scores(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

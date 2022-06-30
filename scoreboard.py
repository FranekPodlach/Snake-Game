from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.score_tracker()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, "center", ("Courier", 20, "normal"))

    def score_tracker(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "center", ("Courier", 15, "normal"))

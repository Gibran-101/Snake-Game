from turtle import Turtle
FONT = ("Courier", 14, "normal")
ALIGNMENT = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("green")
        self.penup()
        self.hideturtle()
        self.goto(0, 276)
        self.display_scoreboard()

    def display_scoreboard(self):
        self.write(arg= f"SCORE: {self.score}", move= False, align= ALIGNMENT, font= FONT)

    def increment_scoreboard(self):
        self.clear()
        self.score += 1
        self.display_scoreboard()

    def leader_board(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file="data.txt", mode='w') as data:
                data.write(f"{self.high_score}")
            self.clear()
            self.display_scoreboard()
        self.score = 0

    def game_over(self):
        self.goto(0,0)
        self.write(arg= "GAME OVER", move= False, align= ALIGNMENT, font= ("Courier", 30, "normal"))



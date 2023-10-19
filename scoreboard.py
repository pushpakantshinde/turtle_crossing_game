from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(0, 275)
        self.color("black")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER !", align=ALIGNMENT, font=FONT)
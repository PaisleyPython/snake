# scoreboard

from turtle import Turtle
from food import Food
# SCOREBOARD = [(0, 0), (-20, 0), (-40, 0)]

ALIGNMENT = "center"
FONT = ("courier", 24, "normal")


class Scoreboard(Turtle):
    """Keeps score when snake eats food"""

    def __init__(self):
        super().__init__()
        # self.highscore = 0
        self.hideturtle()
        with open("data.txt", mode="r") as data:
            self.highscore = int(data.read())
        self.score = 0
        self.penup()
        self.setposition(0, 270)
        self.color("white")
        self.update_scoreboard()

    def increment_score(self):
        self.score += 1
        self.update_scoreboard()

# This method is being written to allow for a high score.
    # def game_over(self):
    #     self.hideturtle()
    #     self.penup()
    #     self.setposition(0, 0)
    #     self.color("white")
    #     self.write("GAME OVER!", move=False, align="center", font=FONT)

# DONE Write high score to data.txt
# DONE Read data.txt and use it's result as an integer for highscore.
# TODO why is scoreboard dissapearing after gameover.

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score} - HIGH SCORE: {self.highscore}", move=False, align=ALIGNMENT,
                   font=FONT)

    def reset(Self):
        if Self.score > Self.highscore:
            Self.highscore = Self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{Self.score}")
        Self.score = 0
        Self.update_scoreboard()

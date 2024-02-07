# food class

from turtle import Turtle
import random


class Food(Turtle):  # Adding the superclass

    def __init__(self):
        super().__init__()  # Calling the turtles init method.
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.4, stretch_wid=0.4)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, +280)
        random_y = random.randint(-280, +280)
        self.goto(random_x, random_y)

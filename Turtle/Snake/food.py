from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.speed("fastest")
        self.shapesize(0.7, 0.7)    # reducing the 20 by 20 food shape
        self.reposition()

    def reposition(self):
        xpos = random.randint(-280, 280)
        ypos = random.randint(-280, 280)
        self.goto((xpos, ypos))
from turtle import Turtle

MOVE_SPEED = 15

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)    #increase the size of the paddle
        self.goto(position)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_SPEED)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_SPEED)


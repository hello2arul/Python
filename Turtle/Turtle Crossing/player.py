from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.go_to_start()        

    def go_to_start(self):
        self.goto(STARTING_POSITION)    

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE) # or self.forward(MOVE_DISTANCE)

    def has_reached_finish_line(self):
        return self.ycor() > FINISH_LINE_Y



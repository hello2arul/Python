import turtle


STARTING_POSTIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # creates 3 snake segments
    def create_snake(self):
        for position in STARTING_POSTIONS:
            self.add_segment(position)
        
    def add_segment(self, position):
        snake_segment = turtle.Turtle("square")
        snake_segment.penup()
        snake_segment.color("white")
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def reset(self):
        # removing the old snake off the screen
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.__init__()

    def grow(self):
        self.add_segment(self.segments[-1].position())
    
    # like fibonacci a,b,c
    def move(self):
        for idx in range(len(self.segments) - 1, 0, -1):
            prev_x = self.segments[idx - 1].xcor()
            prev_y = self.segments[idx - 1].ycor()
            self.segments[idx].goto(prev_x, prev_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def is_colliding(self):
        # eating itself
        for segment in self.segments:
            if segment != self.head:
                if self.head.distance(segment) < 10:
                    return True
        # wall collision
        return self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280
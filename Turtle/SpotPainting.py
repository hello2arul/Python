import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()
screen = turtle.Screen()


# setting the turtle at bottom left
tim.penup()
tim.setheading(225)
tim.forward(325)
tim.setheading(0)
num_of_dots = 100

def getRandomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for dot in range(1, num_of_dots + 1):
    tim.dot(20, getRandomColor()) # draw dot
    tim.forward(50) # move right

    if dot % 10 == 0: # when hit right border
        tim.setheading(90) # look up
        tim.forward(50) # move to the next row
        tim.setheading(180) # point to the left
        tim.forward(500) # move to the left border without drawing
        tim.setheading(0) #reset pointer to right



screen.exitonclick()
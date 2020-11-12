import turtle 
import random

turtle.colormode(255) # default black, changing to rgb
tim = turtle.Turtle()
screen = turtle.Screen()

def getRandomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)



def drawSpirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        tim.speed("fastest")
        tim.color(getRandomColor())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap) #Set the orientation of the turtle to to_angle.


drawSpirograph(5)
screen.exitonclick()





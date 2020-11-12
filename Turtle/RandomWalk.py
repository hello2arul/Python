import turtle 
from turtle import Screen
import random

turtle.colormode(255) # default black, changing to rgb
tim = turtle.Turtle()

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fast")

def getRandomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for _ in range(200):
    tim.color(getRandomColor())
    tim.forward(30)
    tim.setheading(random.choice(directions))


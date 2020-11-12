import turtle
import time
import random
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0) # try commenting this line


alive = True
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
time.sleep(1)

while alive:
    screen.update() # update the screen once all the pieces have moved
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.reposition()   
        snake.grow()
        scoreboard.update_score()  

    if snake.is_colliding():
        scoreboard.reset()   
        snake.reset()

screen.exitonclick()
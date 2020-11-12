from turtle import Screen, xcor
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)    # turn on auto animation
screen.listen()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()     # manually animate
    ball.move()

    # top and bottom collision
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    # paddle-ball collision - additional checks to check ball hitting the paddle edge
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.update_lpoint()

    # left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.update_rpoint()

screen.exitonclick()
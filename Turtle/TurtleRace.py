import turtle
import random

screen = turtle.Screen()
screen.title("Turtle Race")
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win?, pick a color: ")
colors = ["blue", "green", "yellow", "red", "orange", "violet"]
x_pos, y_pos = -230, -70    # mid point is (0, 0)
all_turtles = []
has_race_started = False

for idx in range(len(colors)):
    tim = turtle.Turtle(shape="turtle")
    tim.color(colors[idx])
    tim.penup()
    tim.goto(x_pos, y_pos)
    all_turtles.append(tim)
    y_pos += 30

if user_bet:
    has_race_started = True

while has_race_started:

    for tim in all_turtles:
        tim.forward(random.randint(0, 10))

        if tim.xcor() >= 230:   # size of turtle = 40 by 40
            has_race_started = False
            winner_color = tim.color()[0] # returns a tuple(pen_color, fill_color)

            if winner_color == user_bet:
                print("you won")
            else:
                print(f"you lose, {winner_color} is the winner")
            break

screen.exitonclick()


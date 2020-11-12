import turtle
import pandas

screen = turtle.Screen()
screen.title("US states")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
total_states = len(all_states)
correct_guesses = 0
guessed_states = set()

while correct_guesses != total_states:
    user_answer = screen.textinput(title=f"{correct_guesses}/{total_states} correct", prompt="Enter a valid state").title() 

    if user_answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    
    if user_answer in all_states and user_answer not in guessed_states:
        guessed_states.add(user_answer)
        correct_guesses += 1
        tim = turtle.Turtle()
        tim.penup()
        state_data = data[data.state == user_answer]    
        tim.goto(int(state_data.x), int(state_data.y)) 
        tim.write(user_answer)


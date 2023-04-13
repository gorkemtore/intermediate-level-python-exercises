import turtle
import pandas

screen = turtle.Screen()
image = "./us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./us-states-game/50_states.csv")
all_states = data.state.tolist()

guessed_states = []
while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missed_states = []
        for state in all_states:
             if state not in guessed_states:
                  missed_states.append(state)
                  
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("./us-states-game/states-to-learn.csv")
        break

    if answer_state in all_states:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            #t.write(state_data.state.item())
            t.write(answer_state)
            guessed_states.append(answer_state)
 

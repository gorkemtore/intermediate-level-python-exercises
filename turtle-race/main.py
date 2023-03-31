from turtle import Turtle, Screen
import random

is_race_on = False


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_axis = -70

all_turtles = []

for color_turtle in colors:

    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color_turtle)
    new_turtle.goto(-230, y_axis)
    y_axis += 30
    all_turtles.append(new_turtle)

if user_bet: # There exists
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color.upper() == user_bet.upper():
                print(f"Congratulations! Winner color: {winning_color.title()}")
            else:
                print(f"Sorry, you lost! Winner color: {winning_color.title()}, but your bet: {user_bet.title()}")

            is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()

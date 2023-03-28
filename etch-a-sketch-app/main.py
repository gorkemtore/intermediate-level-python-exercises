from turtle import Turtle, Screen

tom = Turtle()


def move_forward():
    tom.forward(10)


def turn_left_side():
    tom.setheading(tom.heading()+10)


def turn_right_side():
    tom.setheading(tom.heading()-10)


def move_back():
    tom.backward(10)


def clear_screen():
    tom.clear()


def exit_game():
    exit()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left_side)
screen.onkey(key="d", fun=turn_right_side)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="e", fun=exit_game)
screen.exitonclick()

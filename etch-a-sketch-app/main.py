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
screen.onkey(move_forward, "w")
screen.onkey(turn_left_side, "a")
screen.onkey(turn_right_side, "d")
screen.onkey(move_back, "s")
screen.onkey(clear_screen, "c")
screen.onkey(exit_game, "e")
screen.exitonclick()

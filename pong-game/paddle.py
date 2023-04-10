from turtle import Turtle, Screen

POSITION = (350, 0)

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
            current_y = self.ycor()
            self.goto(self.xcor(), current_y + 20)

    def go_down(self):
        current_y = self.ycor()
        self.goto(self.xcor(), current_y - 20)    
    
    



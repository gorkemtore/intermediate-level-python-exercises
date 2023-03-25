# import colorgram
#
# colors = colorgram.extract("hirst-painting.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, b, b))
#
# print(rgb_colors)
import random
import turtle
from turtle import Turtle, Screen

colors = [(43, 176, 176), (79, 174, 174), (226, 109, 109),
          (230, 253, 253), (160, 82, 82), (4, 101, 101), (3, 64, 64), (246, 127, 127), (109, 247, 247), (252, 53, 53),
          (184, 251, 251), (211, 5, 5), (35, 252, 252), (177, 248, 248), (139, 0, 0), (252, 35, 35), (50, 56, 56),
          (216, 171, 171), (16, 144, 144), (85, 252, 252), (188, 109, 109), (23, 107, 107), (8, 215, 215),
          (99, 50, 50), (231, 205, 205), (204, 35, 35), (112, 4, 4)]

turtle.colormode(255)

mike = Turtle()
mike.hideturtle()
mike.penup()
mike.setx(-225)
mike.sety(-275)
mike.speed("fastest")

for i in range(100):
    mike.color(random.choice(colors))
    if i % 10 == 0:
        mike.sety(mike.ycor() + 50)
        mike.setx(-225)
    mike.dot(20)
    mike.forward(50)

screen = Screen()
screen.exitonclick()

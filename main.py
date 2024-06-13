import colorgram
import turtle as turtle_module
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

color_list = [(2, 13, 31), (52, 25, 17), (219, 127, 106), (10, 105, 159), (241, 213, 69), (149, 83, 39), (214, 87, 64),
              (164, 162, 33), (157, 7, 24), (156, 63, 102), (97, 6, 19), (11, 63, 32), (206, 74, 104), (11, 96, 57),
              (172, 135, 161), (1, 63, 145), (8, 173, 216), (156, 34, 24), (5, 212, 207), (8, 139, 86), (146, 227, 216),
              (122, 193, 148), (101, 219, 229), (221, 178, 216), (80, 135, 179), (253, 196, 0)]

turtle_module.colormode(255)

tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()

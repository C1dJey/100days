# modules, package

import turtle as t
import random as r
tu = t.Turtle()
def random_color():
    red = r.randint(0,255)
    green = r.randint(0,255)
    blue = r.randint(0,255)
    color = (red, green, blue)
    return color

t.colormode(255)
tu.speed("fastest")

## Challenge 3
# num_size = 3
# for i in range(5):
#     for _ in range(num_size):
#         angle = 360/num_size
#         tu.forward(100)
#         tu.right(angle)
#     num_size += 1
    
## Challenge 4 - random walk
# directions = [0, 90, 180, 270]
# t.colormode(255)


# tu.pensize(15)
# for _ in range(200):
#     tu.color(random_color())
#     tu.forward(30)
#     tu.setheading(r.choice(directions))

## Challenge 5


def draw_spirograpth(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tu.color(random_color())
        tu.circle(100)
        tu.setheading(tu.heading() +size_of_gap)



screen = t.Screen()
screen.exitonclick()
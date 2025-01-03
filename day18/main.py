# import colorgram as c

# colors = c.extract("image.jpg", 80)
# rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_rgb = (r,g,b)
#     rgb.append(new_rgb)

# print(rgb)
import random as r
import turtle as t
color_list = [(199, 162, 100), (62, 91, 128), (140, 170, 192), (139, 90, 48), (219, 206, 119), (135, 27, 52), (32, 41, 67), (78, 16, 36), (149, 59, 85), (167, 154, 49), (187, 143, 162), (134, 183, 
147), (46, 55, 100), (181, 95, 107), (56, 39, 27), (96, 118, 167), (80, 150, 159), (89, 152, 92), (71, 118, 93), (220, 175, 187), (169, 207, 163), (161, 202, 215), (192, 95, 74), (178, 187, 213), (46, 73, 75), (76, 69, 44), (132, 41, 33), (36, 57, 57), (221, 177, 170), (46, 77, 66)]

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_dots = 100
for dot in range(1,number_dots +1):
    tim.pendown()
    tim.dot(20, r.choice(color_list))
    tim.penup()
    tim.forward(50)

    if dot % 10 == 0:
        tim.penup()
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
    
    
    
screen = t.Screen()
screen.exitonclick()
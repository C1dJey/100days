from turtle import Turtle,Screen

tu = Turtle()
tu.shape("circle")
tu.color("red")
for _ in range(4):
    tu.forward(100)
    tu.left(90)



screen = Screen()
screen.exitonclick()
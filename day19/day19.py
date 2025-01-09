import turtle as t
tim = t.Turtle()
screen = t.Screen()

def move():
    tim.forward(10)
def move_back():
    tim.backward(10)
def turn_left():
    new = tim.heading()+10
    tim.setheading(new)
def turn_right():
    new = tim.heading()-10
    tim.setheading(new)
def clean():
    tim.clear()
    tim.penup
    tim.home()
    tim.pendown

screen.listen()

screen.onkey(key="w", fun=move)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clean)

screen.exitonclick()

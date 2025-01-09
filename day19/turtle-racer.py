from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Wich turtle will win ? enter a color: ")
colors = ["red","orange","yellow", "green", "blue", "purple"]
y_pos = [-70,-40,-10,20,50,80]
turtles = []


for tur_i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[tur_i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_pos[tur_i])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won, winner is {winner}")
            else:
                print(f"You've Lost, winner is {winner}")
            
        distance = random.randint(0,10)
        turtle.forward(distance)


screen.exitonclick()
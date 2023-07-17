from turtle import Turtle, Screen
import random

colours = ['gold', 'hotpink', 'orchid1', 'yellow', 'springgreen3', 'cornflowerblue', 'slateblue3', 'purple4']
angles = [0, 90, 180, 270]
tim = Turtle()
tim.speed('fastest')
tim.pensize(3)

for _ in range(250):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.right(random.choice(angles))




screen = Screen()
screen.screensize(100,100)
screen.exitonclick()
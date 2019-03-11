import turtle
import random

turtles = []


def setup():
    global turtles
    startline = -480

    turtle_ycor = [-40, -20, 0, 20, 40]
    turtle_color = ['red', 'yellow', 'green', 'bleu', 'pink']

    for i in range(len(turtle_ycor)):
        new_turtle = turtle.Turtle()
        new_turtle.shape('turtle')
        new_turtle.color(turtle_color[i])
        new_turtle.setpos(startline, turtle_ycor[i])
        turtles.append(new_turtle)


setup()
turtle.mainloop

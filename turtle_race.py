import turtle
import random

turtles = []


def setup():
    global turtles
    startline = -620
    screen = turtle.Screen()
    screen.setup(1290,720)
    # the above setup had seemed to be too much repetation
    # which is not true coz there are two setups to do with Screen
    # btw tried to append the dots together like
    # turtle.Screen.setup(1290, 720)
    # AttributeError: 'function' object has no attribute 'setup'
    screen.bgpic('pavement.gif')

    turtle_ycor = [160, 80, 0, -80, -160]
    turtle_color = ['red', 'orange', 'green', 'blue', 'pink']

    for i in range(len(turtle_ycor)):
        new_turtle = turtle.Turtle()
        new_turtle.shape('turtle')
        new_turtle.color(turtle_color[i])
        new_turtle.penup()
        new_turtle.setpos(startline, turtle_ycor[i])
        new_turtle.pendown()
        turtles.append(new_turtle)


setup()


# when using turtle.mainloop()
# window closes as soon as prog complets
# found the following on Stackoverlow
# another prob:
# window smaller that display orange
# if dragged to appropriated width
# comes back to defaut next time
turtle.getscreen()._root.mainloop()

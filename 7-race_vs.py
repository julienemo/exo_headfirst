import turtle
import random

turtles = []


def setup():
    global turtles
    startline = -620
    screen = turtle.Screen()
    screen.setup(1290, 720)
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


def race():
    global turtles
    winner = False
    finishline = 590

    while not winner:
        for current_turtle in turtles:
            move = random.randint(5, 20)
            current_turtle.forward(move)
            xcor = current_turtle.xcor()
            if (xcor >= finishline):
                winner = True
                winner_color = current_turtle.color()
                print('The winner is', winner_color[0], 'turtle!')
                # winner_color[0] clearly is the first item in a list
                # turtle.color is by def a list of 2 items
                # the first being the color of turtle
                # the second the color of trace
                # it takes two arguments
                # if only one is given, by defaut the other is set to same


setup()
race()

# when using turtle.mainloop()
# window closes as soon as prog complets
# found the following on Stackoverlow
# another prob:
# window smaller that display orange
# if dragged to appropriated width
# comes back to defaut next time
turtle.getscreen()._root.mainloop()

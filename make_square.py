"""This turtle module makes a square.
"""

import turtle
stinky = turtle.Turtle()
stinky.shape('turtle')
stinky.color('green')

bateau = turtle.Turtle()
bateau.shape('turtle')
bateau.color('brown')


def square(turtle_name, length):
    for i in range(4):
        turtle_name.forward(length)
        turtle_name.right(90)


def spiral(turtle_name, length, turn_time):
    turn_angle = 360 / turn_time
    for i in range(turn_time):
        square(turtle_name, length)
        turtle_name.right(turn_angle)
        # I tried * n but error:
        # unsupported operand type(s) for *: 'NoneType' and 'int'


def shape(turtle_name, length, turn_time):
    turn_angle = 360 / turn_time
    for i in range(turn_time):
        turtle_name.forward(length)
        turtle_name.right(turn_angle)

# spiral(stinky, 100, 36)
# bateau.right(4)
# shape(bateau, 100, 36)


shape(bateau, 100, 3)
shape(bateau, 70, 18)
# mainloop is kinda like the end of everything
# don't put it in a def
# it'll just stop everything
# put it at the real end

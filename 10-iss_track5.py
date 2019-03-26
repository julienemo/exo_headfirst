import requests
import json
import turtle


def get_reponse():
    url = 'http://api.open-notify.org/iss-now.json'
    reponse = requests.get(url)
    if (reponse.status_code) == 200:
        return json.loads(reponse.text)
    else:
        return reponse.status_code


def set_cord(longi, lat):
    screen = turtle.Screen()
    screen.setup(1000, 500)
    screen.bgpic('earth.gif')
    screen.setworldcoordinates(-180, -90, 180, 90)
    iss = turtle.Turtle()
    turtle.register_shape('iss.gif')
    iss.shape('iss.gif')
    iss.hideturtle()
    iss.penup()
    iss.goto(longi, lat)
    iss.pendown()
    iss.showturtle()


def print_reponse():
    content = get_reponse()
    if isinstance(content, int):
        print("Oups, Huston, we have a problem,", get_reponse())
    else:
        content = get_reponse()
        lat = round(float(content['iss_position']['latitude']), 2)
        longi = round(float(content['iss_position']['longitude']), 2)
        set_cord(longi, lat)
        print('')
        print('-----ISS POSITION-----')
        print(longi, lat)
    widget = turtle.getcanvas()
    widget.after(5000, print_reponse)


print_reponse()
turtle.mainloop()

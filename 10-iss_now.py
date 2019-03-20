import requests
import json
import turtle
import time


def get_reponse():
    url = 'http://api.open-notify.org/iss-now.json'
    reponse = requests.get(url)
    if (reponse.status_code) == 200:
        return json.loads(reponse.text)
    else:
        return reponse.status_code


def set_cord():
    screen = turtle.Screen()
    screen.setup(1000, 500)
    screen.bgpic('earth.gif')
    screen.setworldcoordinates(-180, -90, 180, 90)
    iss = turtle.Turtle()
    turtle.register_shape('iss.gif')
    iss.shape('iss.gif')
    content = get_reponse()
    lat = float(content['iss_position']['latitude'])
    longi = float(content['iss_position']['longitude'])
    iss.penup()
    iss.goto(longi, lat)
    iss.pendown()


def print_reponse():
    start = time.time()
    content = get_reponse()
    t1 = time.time()
    set_cord()
    t2 = time.time()
    if isinstance(content, int):
        print('Oups Huston, we have a problem,', content)
    else:
        print('')
        print('-----ISS POSITION-----')
        print(content['iss_position']['latitude'], ',', content['iss_position']['longitude'])
    end = time.time()
    print('')
    print('-----CHRONO-----')
    print("Reaching station :", round((t1-start), 2), 'secs')
    print("Moving station icon :", round((t2-t1), 2), 'secs')
    print('Total calculation time:', round((end-start), 2), 'secs')


try:
    print_reponse()
except:
    print("Oups, something happend. Couldn't reach the station")
turtle.mainloop()

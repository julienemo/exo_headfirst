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


def set_cord(longi, lat):
    screen = turtle.Screen()
    screen.setup(1000, 500)
    screen.bgpic('earth.gif')
    screen.setworldcoordinates(-180, -90, 180, 90)
    iss = turtle.Turtle()
    turtle.register_shape('iss.gif')
    iss.shape('iss.gif')
    iss.penup()
    iss.goto(longi, lat)
    iss.pendown()


def print_reponse():
    start = time.time()
    content = get_reponse()
    t1 = time.time()
    if isinstance(content, int):
        print("Oups, Huston, we have a problem,", get_reponse())
    else:
        content = get_reponse()
        lat = round(float(content['iss_position']['latitude']), 2)
        longi = round(float(content['iss_position']['longitude']), 2)
        set_cord(longi, lat)
        t2 = time.time()
        print('')
        print('-----ISS POSITION-----')
        print(longi, lat)
    end = time.time()
    print('')
    print('-----CHRONO-----')
    print("Contacting station :", round((t1-start), 2), 'secs')
    try:
        print("Moving station icon :", round((t2-t1), 2), 'secs')
    except:
        print("Failed to get ISS cord ")
    print('Total calculation time:', round((end-start), 2), 'secs')


print_reponse()
turtle.mainloop()

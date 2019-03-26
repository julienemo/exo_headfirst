import requests
import json
import random
import turtle
import time


def get_player_choice():
    prompt = 'Please randomly choose a character from n.1 to n.88   '
    n = input(prompt)
    while True:
        try:
            while (int(n-1) < 0) or (int(n-1) > 87):
                n = input(prompt)
            break
        except:
            n = input(prompt)
    print(int(n))


def get_pc_choice():
    n = random.randint(0, 87)
    while n == get_player_choice():
        n = random.randint(0, 87)
    print(n)


get_pc_choice()




def get_reponse(n):
    string = "https://swapi.co/api/people/"+str(n)+"/"
    url = string
    reponse = requests.get(url)
    if (reponse.status_code) == 200:
        return json.loads(reponse.text)
    else:
        return reponse.status_code

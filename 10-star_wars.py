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
            while (int(n)-1 < 0) or (int(n)-1 > 87):
                n = input(prompt)
            break
        except:
            n = input(prompt)
    return n


def get_pc_choice(m):
    n = random.randint(0, 87)
    while n == m:
        n = random.randint(0, 87)
    return str(n)


def get_url(n):
    pre = "https://swapi.co/api/people/"
    nb = str(n)
    url = pre+nb+"/"
    return url


def get_reponse(n):
    reponse = requests.get(n)
    if (reponse.status_code) == 200:
        return json.loads(reponse.text)
    else:
        return reponse.status_code


player_choice = get_player_choice()
pc_choice = get_pc_choice(player_choice)
player_url = get_url(player_choice)
pc_url = get_url(pc_choice)
player_char = get_reponse(player_url)
pc_char = get_reponse(pc_url)
print('-----')

print('-----')
print('YOUR CHARACATER')
print('NAME :',)

print("-----")

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


def get_films(n):
    films = []
    for i in range(len(n)):
        films.append(get_reponse(n[i])['title'])
    return films


def print_films(n):
    for i in n:
        print('--'+i)


def count_common(n, m):
    common = []
    for i in n:
        if i in m:
            common.append(i)
    if len(common) > 1:
        string = 'appeared together in ' + str(len(common))+' films.'
    elif len(common) == 1:
        string = 'appeared together once in', common[0]
    else:
        string = "don't have common movie appearance."
    return string


player_choice = get_player_choice()
pc_choice = get_pc_choice(player_choice)
player_url = get_url(player_choice)
pc_url = get_url(pc_choice)
player_char = get_reponse(player_url)
pc_char = get_reponse(pc_url)
player_char_hw = get_reponse(player_char['homeworld'])
pc_char_hw = get_reponse(pc_char['homeworld'])
player_char_fm = player_char['films']
pc_char_fm = pc_char['films']
string_to_print = count_common(get_films(player_char_fm), get_films(pc_char_fm))

print('-----')
print('---YOUR CHARACTER---')
print('CHARACTER N.', player_choice)
print('NAME:', player_char['name'])
print('BIRTH YEAR:', player_char['birth_year'])
print('HOMEWORLD:', player_char_hw['name'])
print('HEIGHT:', player_char['height'])
print('MOVIE APPREARANCE:')
print_films(get_films(player_char_fm))

print('')
print('---PC CHARACATER---')
print('CHARACTER N.', pc_choice)
print('NAME:', pc_char['name'])
print('BIRTH YEAR:', pc_char['birth_year'])
print('HOMEWORLD:', pc_char_hw['name'])
print('HEIGHT:', pc_char['height'])
print('MOVIE APPREARANCE:')
print_films(get_films(pc_char_fm))
print("")
print("-----")
print(player_char['name'], 'and', pc_char['name'])
print(string_to_print)

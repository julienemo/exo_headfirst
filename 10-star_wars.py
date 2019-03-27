import requests
import json
import random
# import turtle
import time


def get_player_choice():
    prompt = 'Please randomly choose a character from n.1 to n.88   '
    n = input(prompt)
    while True:
        try:
            while (int(n) < 1) or (int(n) > 88):
                n = input(prompt)
            break
        except:
            n = input(prompt)
    return n


def get_pc_choice(m):
    n = random.randint(1, 87)
    if n >= int(m):
        n = n + 1
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
        print(n)
        print('Error', reponse.status_code)
        print(reponse.text)


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
        string = 'appeared together once in ' + common[0]
    else:
        string = "don't have common movie appearance."
    return string


t0 = time.time()
player_choice = get_player_choice()
pc_choice = get_pc_choice(player_choice)
t1 = time.time()
player_url = get_url(player_choice)
pc_url = get_url(pc_choice)
t2 = time.time()
player_char = get_reponse(player_url)
#time.sleep(2)
pc_char = get_reponse(pc_url)
t3 = time.time()
player_char_hw = get_reponse(player_char['homeworld'])
pc_char_hw = get_reponse(pc_char['homeworld'])
t4 = time.time()
player_char_fm_content = player_char['films']
pc_char_fm_content = pc_char['films']
player_fm_name_list = get_films(player_char_fm_content)
pc_fm_name_list = get_films(pc_char_fm_content)

t6 = time.time()
print('-----')
print('---YOUR CHARACTER---')
print('CHARACTER N.', player_choice)
print('NAME:', player_char['name'])
print('BIRTH YEAR:', player_char['birth_year'])
print('HOMEWORLD:', player_char_hw['name'])
print('HEIGHT:', player_char['height'])
t7 = time.time()
print('MOVIE APPREARANCE:', len(player_fm_name_list))
print_films(player_fm_name_list)
t8 = time.time()

print('')
print('---PC CHARACATER---')
print('CHARACTER N.', pc_choice)
print('NAME:', pc_char['name'])
print('BIRTH YEAR:', pc_char['birth_year'])
print('HOMEWORLD:', pc_char_hw['name'])
print('HEIGHT:', pc_char['height'])
t9 = time.time()
print('MOVIE APPREARANCE:', len(pc_fm_name_list))
print_films(pc_fm_name_list)
t10 = time.time()
print("")
print("-----")
print(player_char['name'], 'and', pc_char['name'])
print(count_common(player_fm_name_list, pc_fm_name_list))
t12 = time.time()
print('')
print('---CHRONO---')
print('Getting choices:', str(round((t1-t0), 4)) + 'sec')
print('Composing URLs:', str(round((t2-t1), 4)) + 'sec')
print('Reaching API for characters:', str(round((t3-t2), 4)) + 'sec')
print('Printing character info:', str(round((t7+t9-t6-t8), 4)) + 'sec')
print('Reaching API for homeworlds:', str(round((t4-t3), 4)) + 'sec')
print('Reaching API for movies:', str(round((t6-t4), 4)) + 'sec')
print('Printing movies lists:', str(round((t6+t8+t10-t4-t7-t9), 4)) + 'sec')
print('Comparing movie lists:', str(round((t7-t6), 4)) + 'sec')
print('Total time:', str(round((t7-t0), 4)) + 'sec')

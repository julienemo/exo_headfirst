# a dictionnary of dictionnaries as a table
users = {}
users['Kim'] = {
  'email': 'kim@reilly.com',
  'gender': 'F', 'age': 27, 'friends': ['John', 'Josh']}
users['John'] = {
  'email': 'john@abc.com',
  'gender': 'M', 'age': 24, 'friends': ['Kim', 'Josh']}
users['Josh'] = {
  'email': 'josh@wickedlysmart.com',
  'gender': 'M', 'age': 32, 'friends': ['Kim']}


# for user in users:
#    print(user)
#    print(users[user]['friends'])


def get_fr_list(user):
    return(users[user]['friends'])


def chq_age_moyen(user):
    fr_age = []
    for n in get_fr_list(user):
        fr_age.append(users[n]['age'])
        age_moyen = sum(fr_age) / len(fr_age)
        # PY has no built-in average func
    return age_moyen


def calc_age_moyen():
    for user in users:
        print('Average age of', user + "'s friends:", chq_age_moyen(user))


def antisocial():
    min = 19999999999
    for user in users:
        name = user
        nb_fr = len(users[user]['friends'])
        if nb_fr < min:
            min = nb_fr
            antisocial = name
    print('The antisocial is', antisocial, 'with', min, 'friend(s).')


calc_age_moyen()
antisocial()

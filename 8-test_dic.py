# first impression on dictionnary
# 1, dictionnaries use square brackets instead of round brackests for keys
# 2, lists can't be keys
# 3, a dictionnary prints like this
# {'couleur': ['noir', 'blanc'], 'type': 'chat', 'name': 'Bateau', 'poid': 6.5}

mydict = {}
mydict['name'] = 'Bateau'
mydict['type'] = 'chat'
mydict['couleur'] = ['noir', 'blanc']
mydict['poid'] = 6.5

# print('a dictionnary prints like this:')
# print(mydict)

# if 'Bateau' in mydict:
#    print('OK to use value with IN operator.')
# else:
#    print('Only key can be used for IN operator, but not value.')

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
  'gender': 'M', 'age': 32, 'friends': ['John', 'Kim']}

print(users)

# for user in users:
#    print(user)
#    print(users[user]['friends'])


for user in users:
    print(user)
    print(users[user]['age'])

import requests

url = 'http://api.cinepass.de/v3'
reponse = requests.get(url)
if (reponse.status_code) == 200:
    print(reponse.text)
else:
    print('Huston, we have a problem.', reponse.status_code)

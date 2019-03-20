import requests
import json

url = 'http://api.open-notify.org/iss-now.json'
reponse = requests.get(url)
if (reponse.status_code) == 200:
    content = json.loads(reponse.text)
    print('International Space Station position :')
    print(content['iss_position']['latitude'], ',', content['iss_position']['longitude'])
else:
    print('Oups Huston, we have a problem,', reponse.status_code)

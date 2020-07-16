import requests
import json
from user import lfUser
url = 'https://foreninglet.dk/api/memberlogin?version=1'
user_json_object = json.dumps({
  "credentials": {
    "username": "carsten.skov@gmail.com",
    "password": "4A51B",
    "field": "email"
  }
})

data = {
  "credentials": {
    "username": "carsten.skov@gmail.com",
    "password": "4A51B",
    "field": "email"
  }
}
apiUser = '3196'
apiPass = '8b4a33e86d'
try:
    r = requests.post(url, auth=(apiUser,apiPass),json=data, headers={'Content-Type': 'application/json'})
    print(r.request.body)
    print(r.request.headers)
    print(r)
    print(r.json())
    userData = r.json()
    
except requests.exceptions.RequestException as e:
    print(r)
    raise SystemExit(e)

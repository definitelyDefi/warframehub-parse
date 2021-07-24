import requests
from requests.api import get
import json

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36' }

def get_cambion(url):
    response = requests.get(url, headers=headers)
    jsonData = json.dumps(response.json())
    dictData = json.loads(jsonData)
    print('\n')
    print('Cambion -', dictData["active"])
def get_cetus(url):
    response = requests.get(url, headers=headers)
    jsonData = json.dumps(response.json())
    dictData = json.loads(jsonData)
    print('Cetus   -', dictData["state"],'    time left: ',dictData["timeLeft"])

def get_fortuna(url):
    response = requests.get(url, headers=headers)
    jsonData = json.dumps(response.json())
    dictData = json.loads(jsonData)
    if dictData["isWarm"] == True:
        print('Vallis  - warm','   time left: ',dictData["timeLeft"])
    elif dictData["isWarm"] == False:
        print('Vallis  - cold','   time left: ',dictData["timeLeft"])

def get_earth(url):
    response = requests.get(url, headers=headers)
    jsonData = json.dumps(response.json())
    dictData = json.loads(jsonData)
    if dictData["isDay"] == True:
        print('Earth  - day','  time left: ',dictData["timeLeft"])
    elif dictData["isDay"] == False:
        print('Earth   - night','  time left: ',dictData["timeLeft"])
def get_darwo(url):
    response = requests.get(url, headers=headers)
    
    jsonData = json.dumps(response.json()[0])
    dictData = json.loads(jsonData)
    print('Darwo: Item -',dictData["item"], ',original price -',dictData["originalPrice"],',sale price -', dictData["salePrice"],',discount -',dictData["discount"],'%',',expiry -',dictData["expiry"])


get_cambion("https://api.warframestat.us/pc/cambionCycle")
get_cetus("https://api.warframestat.us/pc/cetusCycle")
get_fortuna("https://api.warframestat.us/pc/vallisCycle")
get_earth("https://api.warframestat.us/pc/earthCycle")
get_darwo("https://api.warframestat.us/pc/dailyDeals")


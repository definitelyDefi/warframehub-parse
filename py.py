import requests, json, sys
from requests.api import get
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow



headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36' }


def get_cambion(url):
    global cambion_status
    response = requests.get(url, headers=headers)
    jsonData = json.dumps(response.json())
    dictData = json.loads(jsonData)
    #print('\n')
    cambion_status = 'Cambion - '+dictData["active"]
    
def get_cetus(url):
    global cetus_status
    response = requests.get(url, headers=headers)
    jsonData = json.dumps(response.json())
    dictData = json.loads(jsonData)
    cetus_status = 'Cetus   - '+dictData["state"]+'    time left: '+ dictData["timeLeft"]
    
def get_fortuna(url):
    global vallis_status
    response = requests.get(url, headers=headers)
    jsonData = json.dumps(response.json())
    dictData = json.loads(jsonData)
    if dictData["isWarm"] == True:
        vallis_status = 'Vallis  - warm'+'   time left: '+dictData["timeLeft"]
    elif dictData["isWarm"] == False:
        vallis_status = 'Vallis  - cold'+'   time left: '+dictData["timeLeft"]
        
def get_earth(url):
    global earth_status
    response = requests.get(url, headers=headers)
    jsonData = json.dumps(response.json())
    dictData = json.loads(jsonData)
    if dictData["isDay"] == True:
        earth_status = 'Earth  - day'+'  time left: '+dictData["timeLeft"]
        
    elif dictData["isDay"] == False:
        earth_status = 'Earth   - night'+'  time left: '+dictData["timeLeft"]
        
def get_darwo(url):
    global darwo
    response = requests.get(url, headers=headers)
    jsonData = json.dumps(response.json()[0])
    dictData = json.loads(jsonData)
    darwo = 'Darwo: Item - '+ dictData["item"]+' , original price - '+str(dictData["originalPrice"])+' ,sale price - '+str(dictData["salePrice"])+' ,discount - '+str(dictData["discount"])+'%'+' ,expiry - '+str(dictData["expiry"])
    
def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Warframe Hub Parser")
    window.setGeometry(500, 300, 700, 200)

    cambion_text = QtWidgets.QLabel(window)
    cambion_text.setText(cambion_status)
    cambion_text.move(50,50)
    cambion_text.adjustSize()

    cetus_text = QtWidgets.QLabel(window)
    cetus_text.setText(cetus_status)
    cetus_text.move(50,70)
    cetus_text.adjustSize()

    vallis_text = QtWidgets.QLabel(window)
    vallis_text.setText(vallis_status)
    vallis_text.move(50,90)
    vallis_text.adjustSize()

    earth_text = QtWidgets.QLabel(window)
    earth_text.setText(earth_status)
    earth_text.move(50,110)
    earth_text.adjustSize()

    darwo_text = QtWidgets.QLabel(window)
    darwo_text.setText(darwo)
    darwo_text.move(50,130)
    darwo_text.adjustSize()


    window.show()
    sys.exit(app.exec_())

    

get_cambion("https://api.warframestat.us/pc/cambionCycle")
get_cetus("https://api.warframestat.us/pc/cetusCycle")
get_fortuna("https://api.warframestat.us/pc/vallisCycle")
get_earth("https://api.warframestat.us/pc/earthCycle")
get_darwo("https://api.warframestat.us/pc/dailyDeals")
application()


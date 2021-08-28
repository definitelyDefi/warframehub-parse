import sys
from requests.api import get
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import aiohttp
import asyncio
import json


async def get_cambion(url):
    global cambion_status
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dictData = await resp.json()
            cambion_status = 'Cambion - '+dictData["active"]
            

# def get_cambion(url):                                            
#     global cambion_status
#     response = requests.get(url, headers=headers)
#     jsonData = json.dumps(response.json())                            <-- old example
#     dictData = json.loads(jsonData)
#     #print('\n')
#     cambion_status = 'Cambion - '+dictData["active"]
    
async def get_cetus(url):
    global cetus_status
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dictData = await resp.json()
            cetus_status = 'Cetus   - '+dictData["state"]+'    time left: '+ dictData["timeLeft"]
            
async def get_fortuna(url):
    global vallis_status
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dictData = await resp.json()

            if dictData["isWarm"] == True:
                vallis_status = 'Vallis  - warm'+'   time left: '+dictData["timeLeft"]
            elif dictData["isWarm"] == False:
                vallis_status = 'Vallis  - cold'+'   time left: '+dictData["timeLeft"]
            
async def get_earth(url):
    global earth_status
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dictData = await resp.json()
            if dictData["isDay"] == True:
                earth_status = 'Earth  - day'+'  time left: '+dictData["timeLeft"]
        
            elif dictData["isDay"] == False:
                earth_status = 'Earth   - night'+'  time left: '+dictData["timeLeft"]
                  
async def get_darwo(url):
    global darwo_status
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:

            dictdata = await resp.json()
            dictData = dictdata[0]
            
            darwo_status = 'Darwo: Item - '+ dictData["item"]+' , original price - '+str(dictData["originalPrice"])+' ,sale price - '+str(dictData["salePrice"])+' ,discount - '+str(dictData["discount"])+'%'+' ,expiry - '+str(dictData["expiry"])
                
# def exit_app():
#     sys.exit()
    
# def application():
#     app = QApplication(sys.argv)
#     window = QMainWindow()

#     window.setWindowTitle("Warframe Hub Parser")
#     window.setGeometry(500, 300, 700, 200)

#     cambion_text = QtWidgets.QLabel(window)
#     cambion_text.setText(cambion_status)
#     cambion_text.move(50,50)
#     cambion_text.adjustSize()

#     cetus_text = QtWidgets.QLabel(window)
#     cetus_text.setText(cetus_status)
#     cetus_text.move(50,70)
#     cetus_text.adjustSize()

#     vallis_text = QtWidgets.QLabel(window)
#     vallis_text.setText(vallis_status)
#     vallis_text.move(50,90)
#     vallis_text.adjustSize()

#     earth_text = QtWidgets.QLabel(window)
#     earth_text.setText(earth_status)
#     earth_text.move(50,110)
#     earth_text.adjustSize()

#     darwo_text = QtWidgets.QLabel(window)
#     darwo_text.setText(darwo_status)
#     darwo_text.move(50,130)
#     darwo_text.adjustSize()

#     button1 = QtWidgets.QPushButton(window)
#     button1.move(250,150)
#     button1.setText('ОК')
#     button1.adjustSize()
#     button1.clicked.connect(exit_app)
    


#     window.show()
#     sys.exit(app.exec_())




def main():
    loop = asyncio.get_event_loop()
    cambion = asyncio.gather(get_cambion("https://api.warframestat.us/pc/cambionCycle"))
    cetus = asyncio.gather(get_cetus("https://api.warframestat.us/pc/cetusCycle"))
    vallis = asyncio.gather(get_fortuna("https://api.warframestat.us/pc/vallisCycle"))
    earth = asyncio.gather(get_earth("https://api.warframestat.us/pc/earthCycle"))
    darwo = asyncio.gather(get_darwo("https://api.warframestat.us/pc/dailyDeals"))
    all = asyncio.gather(cambion, cetus, vallis, earth,darwo)
    loop.run_until_complete(all)
    dict_of_data = {
        'cambion' : cambion_status,
        'cetus'   : cetus_status,
        'vallis'  : vallis_status,
        'earth'   : earth_status,
        'darwo'   : darwo_status
    }

    with open('output.json', 'w+') as f:
        json.dump(dict_of_data, f)



    





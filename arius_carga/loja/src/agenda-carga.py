import pyautogui
import time
import schedule
import yaml
import os

def start():
    with open('C:\\arius-play\\arius_carga\\loja\\config\\agenda-carga.yaml','r', encoding="utf-8") as config:
            cfg = yaml.safe_load(config) 
    
    os.system(cfg["agenda_carga"])    

with open('C:\\arius-play\\arius_carga\\loja\\config\\agenda-carga.yaml','r', encoding="utf-8") as config:
            cfg = yaml.safe_load(config) 
schedule.every().day.at(cfg["hora"]).do(start)

while 1:
    schedule.run_pending()
    time.sleep(1)

#pyinstaller --noconsole --onefile --icon=C:\arius-play\arius_carga\icon\kw.ico C:\arius-play\arius_carga\loja\src\agenda-carga.py
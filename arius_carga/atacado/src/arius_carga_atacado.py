import pyautogui
import time
import schedule
import yaml

def start():
    with open('C:\\Users\\EXPECTRO\\Documents\\arius_play\\arius_carga\\loja\\config\\config.yaml','r', encoding="utf-8") as config:
        cfg = yaml.safe_load(config) 
    pyautogui.keyDown('win')
    pyautogui.press(['r'])
    pyautogui.keyUp('win')
    time.sleep(3)
    pyautogui.write(cfg["arius_carga"])
    time.sleep(3)
    pyautogui.press(['return'])

schedule.every().wednesday.at("05:00").do(start)
schedule.every().sunday.at("05:00").do(start)
while 1:
    schedule.run_pending()
    time.sleep(1)

#pyinstaller --noconsole --onefile --icon=C:\Users\EXPECTRO\Documents\arius_play\arius_carga\icon\gestao.ico C:\Users\EXPECTRO\Documents\arius_play\arius_carga\atacado\src\arius_carga_atacado.py
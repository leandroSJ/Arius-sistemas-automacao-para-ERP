from unicodedata import name
import pyautogui
from datetime import date, timedelta, datetime
import time
import yaml

def gerar_carga():
    with open('C:\\arius-play\\arius_carga\\atacado\\config\\config.yaml','r', encoding="utf-8") as config:
            cfg = yaml.safe_load(config)
    #open arius
    pyautogui.keyDown('win')
    pyautogui.press(['r'])
    pyautogui.keyUp('win')
    time.sleep(1)
    pyautogui.write(cfg["erp_arius"])
    time.sleep(1)
    pyautogui.press(['return'])    
    time.sleep(5)#15

    #user
    pyautogui.write(cfg["login_erp"])
    time.sleep(2)
    pyautogui.press(['return']) 

    #password
    pyautogui.write(cfg["senha_erp"])
    time.sleep(2)
    pyautogui.press(['return'])
    pyautogui.press(['return'])
    pyautogui.press(['return'])
    time.sleep(5)    
    pyautogui.click(cfg["mudar_empresa_erp"])
    time.sleep(1)
    pyautogui.press(['up'])
    pyautogui.press(['return'])
    time.sleep(1)
    pyautogui.press(['return'])
    pyautogui.press(['return'])
    time.sleep(5)

    #click cadastro de produtos    
    pyautogui.doubleClick(cfg["cadastro_de_produtos"])
    time.sleep(1)

    #pressiona sim
    pyautogui.press(['tab'])
    pyautogui.press(['return'])
    time.sleep(1)

    #pressiona sim
    pyautogui.press(['tab'])
    pyautogui.press(['return'])
    time.sleep(60)  #120
    pyautogui.press(['return','return'])  

    #exit erp
    pyautogui.keyDown('alt')
    pyautogui.press(['f4'])
    pyautogui.keyUp('alt')
    time.sleep(5)
    
    #open kw
    pyautogui.keyDown('win')
    pyautogui.press(['r'])
    pyautogui.keyUp('win')
    time.sleep(2)
    pyautogui.write(cfg["kw"])
    pyautogui.press(['return'])
    time.sleep(30)
    pyautogui.write(cfg["login_kw"])
    pyautogui.press(['tab'])
    pyautogui.write(cfg["senha_kw"])
    pyautogui.press(['return'])
    time.sleep(5)
    # select empresa-2 kw
    pyautogui.click(cfg["mudar_empresa_kw"])
    pyautogui.press(['down'])
    pyautogui.press(['return'])
    time.sleep(5)
    #import files
    pyautogui.click(cfg["processos"])
    time.sleep(2)
    pyautogui.click(cfg["importacao"])
    time.sleep(2)
    pyautogui.click(cfg["importar"])
    time.sleep(60)#90
    #get table    
    pyautogui.click(cfg["gerar_tabelas"])
    time.sleep(3)
    pyautogui.click(cfg["todos"])
    pyautogui.click(cfg["gerar"])
    time.sleep(60)#90
    pyautogui.keyDown('alt')
    pyautogui.press(['f4'])
    pyautogui.keyUp('alt')
    time.sleep(2)
    
def log_carga():
    with open('C:\\Users\\EXPECTRO\\Documents\\arius_play\\arius_carga\\atacado\\config\\config.yaml','r', encoding="utf-8") as config:
        cfg = yaml.safe_load(config)
    data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')     
    
    file = open(cfg["log_carga"], 'a')
    file.write(f'CARGA NO ATACADO [OK] - {data}\n\n')
    file.close()
    pyautogui.alert('CARGA NO ATACADO EFETUADA')

    
gerar_carga()
log_carga()
#pyinstaller --noconsole --onefile --icon=C:\Users\EXPECTRO\Documents\arius_play\arius_carga\icon\kw.ico C:\Users\EXPECTRO\Documents\arius_play\arius_carga\atacado\src\carga_atacado.py
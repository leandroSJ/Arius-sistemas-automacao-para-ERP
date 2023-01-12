import pyautogui
from datetime import date, timedelta, datetime
import time
import yaml

def gerar_carga():
    
    with open('C:\\arius-play\\arius_carga\\loja\\config\\config.yaml','r', encoding="utf-8") as config:
            cfg = yaml.safe_load(config)     
    #open arius
    pyautogui.keyDown('win')
    pyautogui.press(['r'])
    pyautogui.keyUp('win')
    time.sleep(3)
    pyautogui.write(cfg["abrir_erp_arius"])
    time.sleep(3)
    pyautogui.press(['return']) 
    time.sleep(7)

    #user
    pyautogui.write(cfg["usuario"])
    time.sleep(2)
    pyautogui.press(['return']) 

    #password
    pyautogui.write(cfg["senha"])
    time.sleep(2)
    pyautogui.press(['return'])
    pyautogui.press(['return'])
    pyautogui.press(['return'])
    time.sleep(5)    
    pyautogui.press(['return'])
    time.sleep(3)
    pyautogui.press(['return'])
    time.sleep(1)
    pyautogui.press(['return'])
    pyautogui.press(['return'])
    time.sleep(15)
    
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
    time.sleep(120)  
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
    time.sleep(3)
    pyautogui.write(cfg["kw"])
    pyautogui.press(['return'])
    time.sleep(10)
    pyautogui.write(cfg["usuario-kw"])
    pyautogui.press(['tab'])
    pyautogui.write(cfg["senha-kw"])
    time.sleep(1)
    pyautogui.press(['return'])
    
    time.sleep(10)
    pyautogui.click(cfg["processos"])
    time.sleep(3)
    pyautogui.click(cfg["importacao"])
    time.sleep(5)
    pyautogui.click(cfg["importar"])
    time.sleep(90)         
    #get table    
    pyautogui.click(cfg["gerar_tabelas"])
    time.sleep(3)
    pyautogui.click(cfg["todos"])    
    pyautogui.click(cfg["gerar"])
    time.sleep(60)#70
    pyautogui.keyDown('alt')
    pyautogui.press(['f4'])
    pyautogui.keyUp('alt')
    time.sleep(2)
    
def log_carga():
    with open('C:\\arius-play\\arius_carga\\loja\\config\\config.yaml','r', encoding="utf-8") as config:
            cfg = yaml.safe_load(config) 

    data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')         
    file = open(cfg["log_carga"], 'a')
    file.write(f'CARGA NA LOJA [OK] - {data}\n\n')
    file.close()
    pyautogui.alert('CARGA NA LOJA EFETUADA')
                    
gerar_carga()
log_carga()

#pyinstaller --noconsole --onefile --icon=C:\arius-play\arius_carga\icon\kw.ico C:\arius-play\arius_carga\loja\src\carga_loja.py
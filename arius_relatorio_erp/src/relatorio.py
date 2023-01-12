from unicodedata import name
import pyautogui
import time
import yaml
from tkinter import *

def entra_sistema():
    with open('C:\\arius-play\\arius_relatorio_erp\\config\\config.yml','r', encoding="utf-8") as config:
            cfg = yaml.safe_load(config)
    #abrir erp
    data = box_chaveAcesso.get()    
    pyautogui.keyDown('win')
    pyautogui.press(['r'])
    pyautogui.keyUp('win')
    pyautogui.write('C:\\gestao\\arius.exe')
    pyautogui.press(['enter'])
    time.sleep(3)
    #user
    pyautogui.write(cfg["login"]) 
    pyautogui.press(['return']) 
    time.sleep(2)
    #password
    pyautogui.write(cfg["senha"])
    pyautogui.press(['return'])
    pyautogui.press(['return'])
    time.sleep(4)       
    pyautogui.press(['return'])
    time.sleep(5)
    #abrir relatórios do sistema
    pyautogui.click(cfg["relatorio_sistema"])
    time.sleep(2)
    pyautogui.click(cfg["usuarios"])
    time.sleep(2)
    pyautogui.click(cfg["compras"])
    time.sleep(2)
    pyautogui.press(['end'])
    time.sleep(2)
    pyautogui.click(cfg["preco"])
    time.sleep(2)
    #selecionar empresa 1
    pyautogui.click(cfg["empresa"])
    time.sleep(2)
    pyautogui.click(cfg["seta"])
    time.sleep(2)
    pyautogui.press(['down','down'])
    time.sleep(1)
    pyautogui.press(['enter','enter'])
    #coloca a data
    pyautogui.write(f'{data}')
    time.sleep(1)
    pyautogui.press(['enter'])
    pyautogui.write(f'{data}')
    pyautogui.press(['enter','enter'])

def relatorio_matriz():
    with open('C:\\arius-play\\arius_relatorio_erp\\config\\config.yml','r', encoding="utf-8") as config:
            cfg = yaml.safe_load(config)
    time.sleep(5)
    lancamento = open('C:\\arius-play\\arius_relatorio_erp\\lancamento.txt', 'r')
    for line in lancamento:        
        n_lancamento = line
        
        pyautogui.write(f'{n_lancamento}')
        pyautogui.press(['f8'])
        time.sleep(1)        
        pyautogui.click(cfg["n_lancamento"])      

def relatorio_filial():
    with open('C:\\arius-play\\arius_relatorio_erp\\config\\config.yml','r', encoding="utf-8") as config:
            cfg = yaml.safe_load(config)
     #selecionar empresa 2
    time.sleep(5)
    pyautogui.click(cfg["empresa_2"])
    time.sleep(2)
    pyautogui.click(cfg["seta"])
    time.sleep(2)
    pyautogui.press(['up'])
    time.sleep(1)
    pyautogui.press(['enter','enter','enter','enter','enter'])    
    time.sleep(2)
    lancamento = open('C:\\arius-play\\arius_relatorio_erp\\lancamento-filial.txt', 'r')
    for line in lancamento:        
        n_lancamento = line
        
        pyautogui.write(f'{n_lancamento}')
        pyautogui.press(['f8'])
        time.sleep(1)        
        pyautogui.click('C:\\arius-play\\arius_relatorio_erp\\img\\n_lancamento.PNG')        
    
def start():    
    entra_sistema()
    relatorio_matriz()
    relatorio_filial()
# INTERFACE
windown = Tk()
windown.iconbitmap('C:\\arius-play\\arius_relatorio_erp\\icon\\dev-icon.ico')
windown.title('RELATORIO-DE-NOTAS')
#windown.configure(background="#7289d9")
windown.geometry('320x100')

#CAIXA DE TEXTO
box_chaveAcesso = Entry(windown, background='#f3f3f3')
box_chaveAcesso.place(x=10, y=5, width=80, height=34)

v2 = Button(windown, text='INICIAR', foreground='#00CED1', command=start)
v2.place(x=132.50, y=55, width=55, height=40) 

windown.mainloop()
#pyinstaller --noconsole --onefile --icon=C:\arius-play\arius_relatorio_erp\icon\dev-icon.ico C:\arius-play\arius_relatorio_erp\src\lancamento.py

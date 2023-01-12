import pyautogui
from datetime import date, timedelta
import time
from tkinter import *
import yaml

with open('C:\\arius_play\\ivis\\config\\config.yml','r', encoding="utf-8") as config:
            cfg = yaml.safe_load(config)
def velocidade_1():        
    contador = 0   
    opcao  = box_pedido.get()
    opcao = int(opcao)
    with open('C:\\arius_play\\ivis\\config\\config.yml','r', encoding="utf-8") as config:
            cfg = yaml.safe_load(config)
    while contador < opcao:        
        contador += 1

        time.sleep(1)
        #pyautogui.click(x=1290, y=100)
        pyautogui.click(cfg["exportarPedido"])        
        time.sleep(4)
        pyautogui.press(['space'])
        time.sleep(3)
        pyautogui.press(['f6'])
        time.sleep(3)
        pyautogui.press(['space'])
        time.sleep(3)
        pyautogui.press(['space'])
        time.sleep(3)
        pyautogui.click(cfg["finalizar"])
        if contador == opcao:          
            #os.system('cls')            
            pyautogui.alert('(◑‿◐) OK')
def velocidade_2():
    contador = 0   
    opcao  = box_pedido.get()
    opcao = int(opcao) 
    with open('C:\\arius_play\\ivis\\config\\config.yml','r', encoding="utf-8") as config:
            cfg = yaml.safe_load(config)   
    while contador < opcao:        
        contador += 1

        time.sleep(1)
        #pyautogui.click(x=1290, y=100)
        pyautogui.click(cfg["exportarPedido"])       
        time.sleep(3)
        pyautogui.press(['space'])
        time.sleep(2)
        pyautogui.press(['f6'])
        time.sleep(2)
        pyautogui.press(['space'])
        time.sleep(2)
        pyautogui.press(['space'])
        time.sleep(2)
        pyautogui.click(cfg["finalizar"])
        if contador == opcao:          
            #os.system('cls')            
            pyautogui.alert('(◑‿◐) OK')
            
def velocidade_3():
    contador = 0   
    opcao  = box_pedido.get()
    opcao = int(opcao)  
    with open('C:\\arius_play\\ivis\\config\\config.yml','r', encoding="utf-8") as config:
            cfg = yaml.safe_load(config)  
    while contador < opcao:        
        contador += 1

        time.sleep(1)
        #pyautogui.click(x=1290, y=100)
        pyautogui.click(cfg["exportarPedido"])       
        time.sleep(1)
        pyautogui.press(['space'])
        time.sleep(1)
        pyautogui.press(['f6'])
        time.sleep(1)
        pyautogui.press(['space'])
        time.sleep(1)
        pyautogui.press(['space'])
        time.sleep(1)
        pyautogui.click(cfg["finalizar"])
        if contador == opcao:          
            #os.system('cls')            
            pyautogui.alert('(◑‿◐) OK')

# JANELA DO PROGRAMA - INTERFACE
windown = Tk()
windown.iconbitmap(cfg["icon"])
windown.title('I\'VIS')
windown.configure(background="#f6efe9")
windown.geometry('200x155')

bg = PhotoImage(file=cfg["bg_img"])

# Show image using label
label1 = Label(windown, image=bg)
label1.place(x=0, y=0)

#CAIXA DE TEXTO
box_pedido = Entry(windown, background='#f3f3f3')
box_pedido.place(x=70, y=15, width=50, height=30)

# VELOCIDADE
v1 = Button(windown, text='1 x', foreground='#7389dc', command=velocidade_1)
v1.place(x=25, y=50, width=40, height=40) 

v2 = Button(windown, text='2 x', foreground='#7389dc', command=velocidade_2)
v2.place(x=75, y=50, width=40, height=40) 

v3 = Button(windown, text='3 x', foreground='#7389dc', command=velocidade_3)
v3.place(x=125, y=50, width=40, height=40) 


windown.mainloop()

#pyinstaller --onefile --noconsole --icon=C:\arius-play\ivis\icon\among-us.ico C:\arius-play\ivis\src\ivis.py

import os
import pyautogui
from datetime import date, timedelta
import time
from tkinter import *
import yaml

def encerrada():   
    with open('C:\\arius-play\\ivis\\config\\config_planilha.yml','r', encoding="utf-8") as config:
            cfg = yaml.safe_load(config)     
    contador = 0
    opcao = text_area.get()
    opcao = int(opcao)    
    time.sleep(1)

    pyautogui.keyDown('alt')
    pyautogui.press(['tab'])
    pyautogui.keyUp('alt')
    time.sleep(1)
    pyautogui.keyDown('ctrl')
    pyautogui.press(['c'])
    pyautogui.keyUp('ctrl')

    pyautogui.keyDown('alt')
    pyautogui.press(['tab', 'tab'])
    pyautogui.keyUp('alt')

        #Cola e pesquisa        
    pyautogui.keyDown('ctrl')
    pyautogui.press(['v'])
    pyautogui.keyUp('ctrl')
    #time.sleep(2)
    pyautogui.press(['f5'])

    try:
        #Verifica se o status é <encerrada>
        time.sleep(1)
        pyautogui.click(cfg["nota_encerrada"])
        #Volta para pesquisa
        time.sleep(1)
        pyautogui.click(cfg["parametros"])
        #Seleciona o campo de busca novamente
        #FAST
        pyautogui.click(cfg["TESTE"])
        pyautogui.press(['tab', 'tab'])
        time.sleep(1)                    
        pyautogui.keyDown('alt')
        pyautogui.press(['tab'])
        pyautogui.keyUp('alt')
        time.sleep(2) 
        #Seleciona cor de fundo
        pyautogui.keyDown('alt')          
        time.sleep(1)
        pyautogui.press(['c'])
        time.sleep(1)
        pyautogui.press(['r'])
        pyautogui.keyUp('alt')
        pyautogui.press(['Down','Down','Down','Down'])
        pyautogui.press(['return'])
        time.sleep(1)
        pyautogui.press(['Down'])

    except Exception as e:        
        time.sleep(2)
        pyautogui.click(cfg["parametros"])            
        time.sleep(2)
        #FAST
        pyautogui.click(cfg["TESTE"])
        pyautogui.press(['tab', 'tab'])
                    
        time.sleep(1)                    
        pyautogui.keyDown('alt')
        pyautogui.press(['tab'])
        pyautogui.keyUp('alt')
        time.sleep(2) 
        pyautogui.press(['esc'])
        pyautogui.press(['Down'])
    while contador <= opcao:
        contador += 1        
        #Copia a área selecionada
        pyautogui.keyDown('ctrl')
        pyautogui.press(['c'])
        pyautogui.keyUp('ctrl')

        #Muda para janela do Arius Web                
        pyautogui.keyDown('alt')
        pyautogui.press(['tab'])
        pyautogui.keyUp('alt')
        time.sleep(2) 

        #Cola e pesquisa        
        pyautogui.keyDown('ctrl')
        pyautogui.press(['v'])
        pyautogui.keyUp('ctrl')
        #time.sleep(2)
        pyautogui.press(['f5'])

        try:
            #Verifica se o status é <encerrada>
            time.sleep(1)
            pyautogui.click(cfg["nota_encerrada"])
            #Volta para pesquisa
            time.sleep(1)
            pyautogui.click(cfg["parametros"])
            #Seleciona o campo de busca novamente
            #FAST
            pyautogui.click(cfg["TESTE"])
            pyautogui.press(['tab', 'tab'])
            time.sleep(1)                    
            pyautogui.keyDown('alt')
            pyautogui.press(['tab'])
            pyautogui.keyUp('alt')
            time.sleep(2) 
            #Seleciona cor de fundo
            pyautogui.keyDown('alt')          
            time.sleep(1)
            pyautogui.press(['c'])
            time.sleep(1)
            pyautogui.press(['r'])
            pyautogui.keyUp('alt')
            pyautogui.press(['Down','Down','Down','Down'])
            pyautogui.press(['return'])
            time.sleep(1)
            pyautogui.press(['Down'])

        except Exception as e:        
            time.sleep(2)
            pyautogui.click(cfg["parametros"])            
            time.sleep(2)
            #FAST
            pyautogui.click(cfg["TESTE"])
            pyautogui.press(['tab', 'tab'])
                      
            time.sleep(1)                    
            pyautogui.keyDown('alt')
            pyautogui.press(['tab'])
            pyautogui.keyUp('alt')
            time.sleep(2) 
            pyautogui.press(['esc'])
            pyautogui.press(['Down'])       

# JANELA DO PROGRAMA - INTERFACE
windown = Tk()
windown.iconbitmap('C:\\arius-play\\ivis\\icon\\dev-icon.ico')
windown.title('Atualiza Planilha SEFAZ')
windown.configure(background="#f6efe9")
windown.geometry('300x150')
#número de linhas
n_pedido = Label(windown, text='Nº LINHAS', background='#f6efe9', foreground='#6001d2', anchor=N)
n_pedido.place(x=50, y=10, width=80, height=20)
#CAIXA DE TEXTO
text_area = Entry(windown, background='#ffffff', foreground='#6001d2')
text_area.place(x=20, y=10, width=40, height=30,)
# Verificar
verificarNFE = Button(windown, text='INICIAR', background='#ffffff',foreground='#6001d2', command=encerrada)
verificarNFE.place(x=100, y=100, width=100, height=40) 

windown.mainloop()
#pyinstaller --onefile --noconsole --icon=C:\arius-play\ivis\icon\dev-icon.ico C:\arius-play\ivis\src\atualiza_planilha_sefaz.py

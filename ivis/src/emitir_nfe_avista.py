from logging import exception
import pyautogui
from tkinter import *
import sys
from datetime import datetime
import time

def buscaFinalizaPedido():     
    pyautogui.alert('Se você não estiver logado na empresa 2, Mude para empresa 2 e em seguida presione OK')
    data = datetime.now().strftime('%d/%m/%y') 
    time.sleep(2)
    numero_pedido  = box_numero_pedido.get()
    numero_cliente = box_cod_cliente.get()
    
    #Abrir processo de entrada e saída
    pyautogui.click('C:\\arius_play\\ivis\\img\\notaFiscal\\recebimento.PNG')   
    time.sleep(2)                     
    pyautogui.press(['down','down', 'right', 'down','down','down','down','down','enter'])
    time.sleep(5)
    
    #dados
    pyautogui.click('C:\\arius_play\\ivis\\img\\notaFiscal\\dados.PNG')
    time.sleep(1)
    pyautogui.press(['tab','tab','tab'])
    
    #coloca o COI de isento como padrao
    pyautogui.write('1211')
    pyautogui.press(['enter','enter','enter'])
    pyautogui.write(numero_cliente)
    pyautogui.press(['enter','enter'])
    time.sleep(3)
    try:        
        pyautogui.click('C:\\arius_play\\ivis\\img\\notaFiscal\\isento.PNG')
        pyautogui.press(['tab'])
        time.sleep(1)
        pyautogui.press(['tab'])
        time.sleep(1)
        pyautogui.press(['tab'])
        time.sleep(1)
        pyautogui.press(['tab'])
        time.sleep(1)
        pyautogui.press(['tab'])
        time.sleep(1)
        pyautogui.press(['tab'])
        time.sleep(1)
        pyautogui.press(['tab'])
        time.sleep(1)
        pyautogui.press(['tab'])
    except:
        pyautogui.click('C:\\arius_play\\ivis\\img\\notaFiscal\\dados.PNG')
        time.sleep(1)
        pyautogui.press(['tab','tab'])
        pyautogui.write('1212')                        
        pyautogui.press(['enter','enter','enter'])
        pyautogui.write(numero_cliente)
        pyautogui.press(['enter','enter'])

    
    pyautogui.write(data)
    pyautogui.press(['enter','enter'])
    time.sleep(2)    
    pyautogui.write(data)
    pyautogui.press(['enter','enter'])
    time.sleep(2)
    pyautogui.press(['f2'])
    time.sleep(2)
    pyautogui.press(['space'])
    time.sleep(2)
    pyautogui.click('C:\\arius_play\\ivis\\img\\notaFiscal\\produtos.PNG')
    time.sleep(2)    
    
    pyautogui.click('C:\\arius_play\\ivis\\img\\notaFiscal\\venda_balcao.PNG')
    pyautogui.press(['tab','tab','tab','tab','tab'])
    time.sleep(2)    
    pyautogui.write(numero_pedido)
    pyautogui.press(['tab','tab','tab','space'])
    time.sleep(2)    
    pyautogui.keyDown('shift')
    pyautogui.press(['tab'])
    pyautogui.keyUp('shift')
    time.sleep(2)    
    pyautogui.click('C:\\arius_play\\ivis\\img\\notaFiscal\\clique_pedido.PNG')
    pyautogui.press(['f2'])
    time.sleep(5)
    pyautogui.click('C:\\arius_play\\ivis\\img\\notaFiscal\\totais.PNG')
    time.sleep(6)    
    pyautogui.click('C:\\arius_play\\ivis\\img\\notaFiscal\\encerrar_processo.PNG')
    time.sleep(5)    
    pyautogui.press(['space'])
    time.sleep(5)        
    pyautogui.press(['space'])    
    time.sleep(3)                   

    #EmitirNFE
    pyautogui.doubleClick(x=80, y=265)
    
    time.sleep(10)
    pyautogui.click('C:\\arius_play\\ivis\\img\\notaFiscal\\cobranca.PNG')
    time.sleep(5)      
    pyautogui.keyDown('shift')
    pyautogui.press(['tab'])
    pyautogui.keyUp('shift')
    time.sleep(1)
    pyautogui.press(['down'])

    time.sleep(1)
    pyautogui.press(['tab'])
    pyautogui.press(['down'])

    time.sleep(1)
    pyautogui.press(['tab'])
    pyautogui.press(['down'])

    pyautogui.click('C:\\arius_play\\ivis\\img\\notaFiscal\\gerar_parcelas.PNG')
    time.sleep(10)
    pyautogui.press(['f2'])
    time.sleep(5)
    
    pyautogui.click('C:\\arius_play\\ivis\\img\\notaFiscal\\info_adicionais.PNG')
    
    time.sleep(10)
    pyautogui.click('C:\\arius_play\\ivis\\img\\notaFiscal\\info_notaFiscal.PNG')  
    time.sleep(1)
    
    pyautogui.press(['tab'])
    time.sleep(1)

    #add redução 41,176%
    pyautogui.press(['space'])
    pyautogui.write("1")
    pyautogui.press(['enter'])
    
    #salva
    pyautogui.keyDown('shift')
    pyautogui.press(['tab'])
    time.sleep(1)
    pyautogui.press(['tab'])
    time.sleep(1)
    pyautogui.press(['tab'])
    pyautogui.keyUp('shift')
    time.sleep(1)
    pyautogui.press(['space'])

    #add emissor IVIS
    pyautogui.keyDown('shift')
    pyautogui.press(['tab'])
    time.sleep(1)
    pyautogui.press(['tab'])
    time.sleep(1)
    pyautogui.press(['tab'])
    pyautogui.keyUp('shift')
    time.sleep(1)
    pyautogui.press(['space'])  
    time.sleep(1)  
    pyautogui.write("92")
    time.sleep(1)
    pyautogui.press(['enter'])
    
    #save emissor
    pyautogui.keyDown('shift')
    pyautogui.press(['tab'])
    time.sleep(1)
    pyautogui.press(['tab'])
    time.sleep(1)
    pyautogui.press(['tab'])
    time.sleep(1)
    pyautogui.press(['tab'])
    time.sleep(1)
    pyautogui.press(['tab'])
    time.sleep(1)
    pyautogui.press(['tab'])
    time.sleep(1)
    pyautogui.keyUp('shift')
    pyautogui.press(['space'])
            
    pyautogui.press(['f7'])

    time.sleep(20)
    pyautogui.press(['space'])

    time.sleep(5)    

    #imprimir
    pyautogui.keyDown('ctrl')
    pyautogui.press(['p'])
    pyautogui.keyUp('ctrl')

    time.sleep(2)
    pyautogui.alert('NFE emitida, Selecione a impressora e imprima! (◑‿◐)') 
    
# INTERFACE
windown = Tk()
windown.iconbitmap(r'C:\\arius_play\\ivis\\icon\\among-us.ico')
windown.title(' \'IVIS NFE')
windown.configure(background="#f4686f")
windown.geometry('250x150')

#CAIXA DE TEXTO
numero_pedido = Label(windown, text='N PEDIDO', foreground='#f3f3f3', background='#f4686f')
numero_pedido.place(x=35, y=5)
box_numero_pedido = Entry(windown, background='#f3f3f3')
box_numero_pedido.place(x=40, y=30, width=55, height=34)

cod_cliente = Label(windown, text='COD CLIENTE', foreground='#f3f3f3', background='#f4686f')
cod_cliente.place(x=150, y=5)
box_cod_cliente = Entry(windown, background='#f3f3f3')
box_cod_cliente.place(x=165, y=30, width=45, height=34)

v2 = Button(windown, text='EMITIR NOTA', foreground='#f3f3f3',background='#f4686f' ,activebackground='#f4686f',activeforeground='#f3f3f3', command=buscaFinalizaPedido)
v2.place(x=80, y=90, width=90, height=40) 

windown.mainloop()
#pyinstaller --onefile --noconsole --icon=C:\arius_play\ivis\icon\among-us.ico C:\arius_play\ivis\src\emitir_nfe_avista.py
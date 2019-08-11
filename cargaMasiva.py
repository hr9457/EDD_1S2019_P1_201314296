import csv
#from listaCirular import *#importo todo lo de mi modulo de lista circulas 
import curses #import the curses library
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library

def lecturaArchivo(listaCDE):
    lecturas = []
    with open('usuarios.csv',newline = '') as File:
        reader = csv.reader(File)
        for row in reader:
            if row == "usuario":
                pass 
            else:
                lecturas.append(row)
                listaCDE.addLCDE(row)


def ventanaCargaMasiva(listaCDE):
    lecturaArchivo(listaCDE)
    usuarios = listaCDE.cabezaLista
    index = 1
    screen = curses.initscr()
    numFilas , numColum = screen.getmaxyx()
    Y = numFilas//2 -5
    X = numColum//2 -5
    posNombresUsuarios = X - 6
    ventana = curses.newwin(numFilas, numColum, 0, 0)
    ventana.border(0)
    ventana.keypad(True)
    centroX = int(numColum / 2)
    ventana.addstr(0,X," Users ")
    ventana.refresh()
    ventana.timeout(-1) # mantiene la ventan indefinidadmente mientra se utilize el comando getch() para una entrada en pantalls
 
    #matiene abierto mientras teclas sean diferentes a la teclas esc
    teclado = ventana.getch()
    while teclado !=27: 
        if teclado == 260:
            ventana.clear()
            ventana.border(0)
            ventana.addstr(0,X," Users ")
            usuarios = usuarios.anteriorLCDE
            valor = str(usuarios.nombreUsuario).replace("['","")
            ventana.addstr(Y,posNombresUsuarios," <--- " +valor.replace("']","")+" ---> " )
            ventana.addstr(Y+2,X-6," Selecionar (Enter) ")
            ventana.addstr(Y+3,X-3," Salir (Esc) ")
            ventana.refresh()
        elif teclado == 261:
            ventana.clear()
            ventana.border(0)
            ventana.addstr(0,X," Users ")
            usuarios = usuarios.siguienteLCDE
            valor = str(usuarios.nombreUsuario).replace("['","")
            ventana.addstr(Y,posNombresUsuarios," <--- " +valor.replace("']","")+" ---> " )
            ventana.addstr(Y+2,X-6," Selecionar (Enter) ")
            ventana.addstr(Y+3,X-3," Salir (Esc) ")
            ventana.refresh()
        elif teclado == 10:
            pass
        
        teclado = ventana.getch()
        telado = -1
        ventana.refresh()

    curses.endwin()


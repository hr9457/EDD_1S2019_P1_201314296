import csv
#from listaCirular import *#importo todo lo de mi modulo de lista circulas 
import curses #import the curses library
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library

def listadoDeRecords(ventana,X,cola):
    Y = 5
    # variable temporal
    usuarios = cola.primeroCola 
    tamanioCola = cola.getSizeCola()
    ventana.addstr(3,X,"NAME            SCORE")
    if tamanioCola == 0:
        ventana.addstr(Y,X,"No hay usuarios registrados con un record")
    else:
        while tamanioCola > 0:
            ventana.addstr(Y,X,""+str(usuarios.nombreUsuario)+"         "+str(usuarios.score))
            Y += 1
            tamanioCola -= 1


def reportes(cola):
    screen = curses.initscr()
    numFilas , numColum = screen.getmaxyx()
    Y = numFilas//2 
    X = numColum//2 -15
    ventana = curses.newwin(numFilas, numColum, 0, 0)
    ventana.border(0)
    ventana.keypad(True)
    ventana.addstr(0,X," SCOREBOARD ")
    ventana.refresh()
    ventana.timeout(10) # mantiene la ventan indefinidadmente mientra se utilize el comando getch() para una entrada en pantalls
    listadoDeRecords(ventana,X,cola)
    #matiene abierto mientras teclas sean diferentes a la teclas esc
    teclado = ventana.getch()
    while teclado !=27:
        teclado = ventana.getch()
        telado = -1
        ventana.refresh()
    curses.endwin()

import csv
#from listaCirular import *#importo todo lo de mi modulo de lista circulas 
import curses #import the curses library
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library

def menuReportes(ventana,X):
    ventana.addstr(5,X,"1. Reporte Sanke")
    ventana.addstr(7,X,"2. Score (Pila)")
    ventana.addstr(9,X,"3. Scoreboard (Cola)")
    ventana.addstr(11,X,"4. User (Lista Circular)")
    ventana.addstr(13,x,"5. Salir (Esc)")


def reportes(listaDE,Pila,listaCDE):
    screen = curses.initscr()
    numFilas , numColum = screen.getmaxyx()
    Y = numFilas//2 
    X = numColum//2 -10
    ventana = curses.newwin(numFilas, numColum, 0, 0)
    ventana.border(0)
    ventana.keypad(True)
    ventana.addstr(0,X," Reports ")
    ventana.refresh()
    ventana.timeout(-1) # mantiene la ventan indefinidadmente mientra se utilize el comando getch() para una entrada en pantalls
 
    menuReportes(ventana,X)
    #matiene abierto mientras teclas sean diferentes a la teclas esc
    teclado = ventana.getch()
    while teclado !=27:
        #opcion uno de reportes
        if teclado == 49:
            listaDE.imagenDot()

        elif teclado == 50:
            Pila.imagenDot()

        elif teclado == 51:
            pass

        elif teclado == 52:
            listaCDE.imagenDot()


        teclado = ventana.getch()
        telado = -1
        ventana.refresh()

    curses.endwin()

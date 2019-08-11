import curses#importacion de la libreria curses
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #impotaciones espaciales para leer el teclado
import subprocess
import os

def dibujoSnake(ventana,usuario,numFilas,numColum):
    #creacion de la ventana
    #ventana = curses.newwin(numFilas, numColum, 0, 0)
    curses.curs_set(0)
    ventana.clear()
    ventana.border(0)
    ventana.addstr(0,5,"Score :")
    ventana.addstr(0,40,"SNAKE RELOADED")
    ventana.addstr(0, 70, "User : "+str(usuario))
    ventana.refresh()
    ventana.timeout(-1)
    teclado = ventana.getch()
    while teclado !=27:
        teclado = ventana.getch()
        telado = -1
        ventana.refresh()
    curses.endwin()

def inicioSnake(usuario):
    if usuario == "":
        screen = curses.initscr()
        curses.noecho()
        curses.curs_set(1)
        #screen.addstr("ingrse su nombre de usuario : ")
        numFilas , numColum = screen.getmaxyx()
        #usuario = screen.getstr()
        ventana = curses.newwin(numFilas, numColum, 0, 0)
        ventana.addstr(1,1,"Ingreses nombre de usuario : ")
        ventana.keypad(1)
        usuario = ventana.getstr()
        dibujoSnake(ventana,usuario,numFilas,numColum)

    else:
        numFilas , numColum = screen.getmaxyx()
        usuario = screen.getstr()


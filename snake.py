import curses#importacion de la libreria curses
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #impotaciones espaciales para leer el teclado
import subprocess
import os

def creacionVentana(usuario,numFilas,numColum):
        #creacion de la ventana
        ventana = curses.newwin(numFilas, numColum, 0, 0)
        ventana.border(0)
        ventana.addstr(0,5,"Score :")
        ventana.addstr(0,40,"SNAKE RELOADED")
        ventana.addstr(0, 70, "User : "+str(usuario))
        ventana.refresh()
        curses.napms(5000)
        curses.endwin()

def inicioMenu(usuario):
        if usuario == "":
                screen = curses.initscr()
                screen.addstr("ingrse su nombre de usuario : ")
                numFilas , numColum = screen.getmaxyx()
                usuario = screen.getstr()
                creacionVentana(usuario,numFilas,numColum)
        
        else:
                numFilas , numColum = screen.getmaxyx()
                usuario = screen.getstr()
                creacionVentana(usuario,numFilas,numColum)
        


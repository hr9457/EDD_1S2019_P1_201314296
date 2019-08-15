import csv
#from listaCirular import *#importo todo lo de mi modulo de lista circulas 
import curses #import the curses library
import curses.textpad
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library
import os

def lecturaArchivo(ventana,nombreArchivo):
    archivo = str(nombreArchivo).replace("b'","")
    try:
        f = open(""+archivo.replace("'","")+".csv","r")
        ventana.addstr(10,10,"archivo cargado")
    except:
        ventana.addstr(10,10,"el archvio no exite : "+str(archivo).replace("'",""))
    ventana.refresh()

def carga():
    screen = curses.initscr()
    curses.echo()#habila la escritura en la pantalla
    curses.curs_set(1)
    numFilas , numColum = screen.getmaxyx()
    #usuario = screen.getstr()
    ventana = curses.newwin(numFilas, numColum, 0, 0)
    ventana.addstr(5,5,"Ingres nombre del archivo : ")
    ventana.keypad(1)
    nombreArchivo = ventana.getstr()
    curses.noecho()#desabilito la entrada por pantalla
    curses.curs_set(0)
    lecturaArchivo(ventana,nombreArchivo)
    curses.napms(2000)
    curses.endwin()
import csv
#from listaCirular import *#importo todo lo de mi modulo de lista circulas 
import curses #import the curses library
import curses.textpad
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library

def carga():
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    numFilas , numColum = screen.getmaxyx()
    ventana = curses.newwin(numFilas, numColum, 0, 0)
    ventana.border(0)
    ventana.keypad(True)
    ventana.addstr(5,5," ingreses nombre del archivo para cargar:  ")
    tb = curses.textpad.Textbox(ventana, insert_mode=True)
    text = tb.edit()
    #text = ventana.edit()
    #tb = curses.textpad.Textbox(ventana)
    #text = tb.edit()
    curses.beep()
    ventana.keypad(1)
    ventana.refresh()
    ventana.timeout(-1) # mantiene la ventan indefinidadmente mientra se utilize el comando getch() para una entrada en pantalls
 
    #matiene abierto mientras teclas sean diferentes a la teclas esc
    #teclado = ventana.getch()
    teclado = int(text)
    while teclado !=27:
        text = tb.edit()
        teclado = int(text)
        #teclado = ventana.getch()
        #teclado = -1
        #teclado.refresh()

    curses.endwin()
import curses #import the curses library
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library
import snake
import ventanUltimosRecord
import subprocess
import os 
import cargaMasiva
import ventanaReportes
import cargaArchivo
from listaCircular import listaCircularDoblementeEnlazada #para el uso de la carga masiva
from listaDoblementeEnlazada import listaDobleEnlazada #par el reporte de las posicion del snake
from pila import pila #para el score del snake
from Cola import Cola #para mostra las primeras 10 puntuaciones




def paint_menu(win):
    paint_title(win,' MAIN MENU ')          #paint title
    win.addstr(7,50, '1. Play')             #paint option 1
    win.addstr(8,50, '2. Scoreboard')       #paint option 2
    win.addstr(9,50, '3. Carga de archivo')   #paint option 3
    win.addstr(10,50, '4. Reports')         #paint option 4
    win.addstr(11,50, '5. Select user')    #paint option 5
    win.addstr(12,50, '6. Exit')            #paint option 6
    win.timeout(-1)                         #espera una entrada por consola

def paint_title(win,var):
    win.clear() #refresca la pantalla                         
    win.border(0) #dibuja un borde en la pantalla
    win.addstr(0,50,var)#paint the title on the screen

def wait_esc(win):
    key = window.getch()
    while key!=27:
        key = window.getch()


stdscr = curses.initscr() #initialize console
tamanioY , tamanioX = stdscr.getmaxyx()
window = curses.newwin(tamanioY,tamanioX,0,0) #create a new curses window
window.keypad(True)     #enable Keypad mode
curses.noecho()         #prevent input from displaying in the screen
curses.curs_set(0)      #cursor invisible (0)
paint_menu(window)      #paint menu



cola = Cola()
usuario = ""
keystroke = -1
while(keystroke==-1):
     
    keystroke = window.getch()  #get current key being pressed

    #------------------------------ingreso al snake----------------------
    if(keystroke==49):
        listaDE = listaDobleEnlazada()
        Pila = pila()
        window.refresh()
        snake.inicioSnake(usuario,listaDE,Pila,cola)
        paint_menu(window)
        keystroke=-1
        #-------------------------Fin snake-----------------------------


    #------------------------------RECORDS-------------------------------
    elif(keystroke==50):
        window.refresh()
        ventanUltimosRecord.reportes(cola)
        paint_menu(window)
        keystroke=-1
    #--------------------------------------------------------------------

    #--------------------------------------------------------------------
    elif(keystroke==51):
        window.refresh()
        cargaArchivo.carga()
        paint_menu(window)
        keystroke=-1
    #--------------------------------------------------------------------


    #----------------------------Reportes-----------------------------
    elif(keystroke==52):
        listaDE = listaDobleEnlazada()
        Pila = pila()
        listaCDE = listaCircularDoblementeEnlazada()
        window.clear()
        window.refresh()
        ventanaReportes.reportes(listaDE,Pila,listaCDE)
        paint_menu(window)
        keystroke=-1
    #--------------------------------------------------------------------


    elif(keystroke==53):
        #--------------------Muestra usuarios de una lista circular---------------------------
        listaCDE = listaCircularDoblementeEnlazada()
        window.clear()
        window.refresh()
        usuario = cargaMasiva.ventanaCargaMasiva(listaCDE)
        paint_menu(window)
        keystroke=-1
        #----------------------Fin Carga Masiva-----------------------------------------------
    
    elif(keystroke==54):
        pass
    else:
        keystroke=-1

curses.endwin() #return terminal to previous state




        

    
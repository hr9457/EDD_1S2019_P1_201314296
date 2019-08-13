import curses #import the curses library
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library
import snake
import subprocess
import os 
import cargaMasiva
from listaCircular import listaCircularDoblementeEnlazada #para el uso de la carga masiva
from listaDoblementeEnlazada import listaDobleEnlazada #par el reporte de las posicion del snake
from pila import pila #para el score del snake
from Cola import Cola #para mostra las primeras 10 puntuaciones

def paint_menu(win):
    paint_title(win,' MAIN MENU ')          #paint title
    win.addstr(7,50, '1. Play')             #paint option 1
    win.addstr(8,50, '2. Scoreboard')       #paint option 2
    win.addstr(9,50, '3. User Selection')   #paint option 3
    win.addstr(10,50, '4. Reports')         #paint option 4
    win.addstr(11,50, '5. Bulk Loading')    #paint option 5
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




keystroke = -1
while(keystroke==-1):
    keystroke = window.getch()  #get current key being pressed
    if(keystroke==49):
        #---------------ingreso al snake----------------------
        ScorePila = pila()
        listaDE = listaDobleEnlazada()
        usuario = ""
        window.refresh()
        snake.inicioSnake(usuario,listaDE,ScorePila)
        paint_menu(window)
        keystroke=-1
        #----------------Fin snake-----------------------------
    elif(keystroke==50):
        paint_title(window, ' SCOREBOARD ')
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==51):
        paint_title(window, ' USER SELECTION ')
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==52):
        paint_title(window, ' REPORTS ')
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==53):
        #--------------------Carga masiva---------------------------
        listaCDE = listaCircularDoblementeEnlazada()
        window.clear()
        window.refresh()
        cargaMasiva.ventanaCargaMasiva(listaCDE)
        paint_menu(window)
        keystroke=-1
        #----------------Fin Carga Masiva----------------------------
    elif(keystroke==54):
        pass
    else:
        keystroke=-1

curses.endwin() #return terminal to previous state




        

    
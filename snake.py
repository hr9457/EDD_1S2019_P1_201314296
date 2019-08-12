import curses#importacion de la libreria curses
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #impotaciones espaciales para leer el teclado
import subprocess
import os

def dibujoSnake(ventana,usuario,numFilas,numColum,listaDE):
    direccionSnake = -1
    while direccionSnake !=27:
        #creacion de la ventana
        #lista inicial del snake
        score = 0 #va midiendo el puntuaje en el juego
        curses.curs_set(0)
        ventana.clear()
        ventana.border(0)
        ventana.addstr(0,5," Score : "+str(score)+" ")
        ventana.addstr(0,40," SNAKE RELOADED ")
        nombre = str(usuario).replace("b'","")
        ventana.addstr(0, 70, " User : "+nombre.replace("'","")+" ")
        ventana.refresh()
        ventana.timeout(-1)

        #pintado del snake desde la cola hacia la cabeza de la lista
        sizeTemporal = listaDE.getSizeLista()
        temporal = listaDE.cabezaLista
        while sizeTemporal >= 1:
            sizeTemporal -= 1
            posicionEnY = temporal.posX
            posicionEnX = temporal.posY
            ventana.addstr(posicionEnY,posicionEnX,"#")
            temporal = temporal.anterior
        
        #opciones de entrdad por el  teclado
        #direccionSnake = ventana.getch()
        #--------------------Movimiento hacia la Derecha--------------------
        if direccionSnake == 261:
            head = listaDE.cabezaLista
            headY = head.posX
            headX = (head.posY) +1
            ventana.addstr(headY,headX,"#")
            listaDE.addFinal(headY,headX)
            ultimoEliminar = listaDE.colaLista
            ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
            listaDE.deletFinal()
        #--------------------Movimiento hacia la Izquierda--------------------
        elif direccionSnake == 260:
            head = listaDE.cabezaLista
            headY = head.posX
            headX = (head.posY)-1
            ventana.addstr(headY,headX,"#")
            listaDE.addFinal(headY,headX)
            ultimoEliminar = listaDE.colaLista
            ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
            listaDE.deletFinal()
        #--------------------Movimiento hacia la arriba--------------------
        elif direccionSnake == 259:
            head = listaDE.cabezaLista
            headY = (head.posX)-1
            headX = head.posY
            ventana.addstr(headY,headX,"#")
            listaDE.addFinal(headY,headX)
            ultimoEliminar = listaDE.colaLista
            ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
            listaDE.deletFinal()
        #--------------------Movimiento hacia la Abajo--------------------
        elif direccionSnake == 258:
            head = listaDE.cabezaLista
            headY = (head.posX)+1
            headX = head.posY
            ventana.addstr(headY,headX,"#")
            listaDE.addFinal(headY,headX)
            ultimoEliminar = listaDE.colaLista
            ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
            listaDE.deletFinal()

        direccionSnake = -1
        direccionSnake = ventana.getch()
        ventana.refresh()

    curses.endwin()




def inicioSnake(usuario,listaDE):
    listaDE.addHead(10,40)
    listaDE.addHead(10,39)
    listaDE.addHead(10,38)
    
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
        dibujoSnake(ventana,usuario,numFilas,numColum,listaDE)
        

    else:
        numFilas , numColum = screen.getmaxyx()
        usuario = screen.getstr()


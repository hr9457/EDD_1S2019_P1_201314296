import curses#importacion de la libreria curses
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #impotaciones espaciales para leer el teclado
import subprocess
import os
import random #librearia para genera numeros random


def ComidaRandom(numFilas,numColum,ventana):
    posicionYRandom = random.randint(2,numFilas-2)
    posicionXRandom = random.randint(2,numColum-2)
    fooRandom = random.choice("++*++*++")
    ventana.addstr(posicionYRandom,posicionXRandom,""+fooRandom)
    if fooRandom == "+":
        tipoFood = 1 #para + el cual produce un push en la pila
        return posicionYRandom ,posicionXRandom, tipoFood
    else:
        tipoFood = 0 #para * el que produce un por en la pila
        return posicionYRandom ,posicionXRandom, tipoFood


def pintadoTituloVentana(ventana,score,usuario):
    ventana.clear()
    ventana.border(0)
    ventana.addstr(0,5," Score : "+str(score)+" ")
    ventana.addstr(0,40," SNAKE RELOADED ")
    nombre = str(usuario).replace("b'","")
    ventana.addstr(0, 70, " User : "+nombre.replace("'","")+" ")
    

def dibujoSnake(ventana,usuario,numFilas,numColum,listaDE,scoreSnake,tamanioInicialSanke):
    direccionSnake = -1
    fooRandom = ""
    tipoFood = ""
    posicionXRandom = 0
    posicionYRandom = 0
    #lista inicial del snake
    score = 0 #va midiendo el puntuaje en el juegor
    curses.curs_set(0)

    #codigo anterio pintadoTituloVentana - repinta el titulo por algun cambie en el score
    pintadoTituloVentana(ventana,score,usuario)

    #codigo anteriorcomidaRandom - para genera la comida aletroriamente en la pantalla
    posicionYRandom , posicionXRandom, tipoFood = ComidaRandom(numFilas,numColum,ventana)
    ventana.timeout(-1)#tiempor actualizacion me puede servir para los niveles en el snake

    while direccionSnake !=27:

        #pintado del snake desde la cola hacia la cabeza de la lista - actualizacion de la pintado
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
        #-------------------------------------------------------Movimiento hacia la Derecha--------------------
        if direccionSnake == 261:
            head = listaDE.cabezaLista
            headY = head.posX
            headX = head.posY
            #revisa que lo que halla enfrente no sea el borde
            if headX+1 != numColum:
                
                #si el snake come un punto correcto
                if headY == posicionYRandom and headX+1 == posicionXRandom and tipoFood==1: 
                    score +=1
                    ventana.addstr(headY,headX+1,"#")
                    listaDE.addFinal(headY,headX+1)
                    ultimoEliminar = listaDE.colaLista
                    ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                    #codigo anterio pintadoTituloVentana - repinta el titulo por algun cambie en el score
                    pintadoTituloVentana(ventana,score,usuario)
                    #codigo anteriorcomidaRandom - para genera la comida aletroriamente en la pantalla
                    posicionYRandom , posicionXRandom, tipoFood = ComidaRandom(numFilas,numColum,ventana)

                #si el snake come un punto icorrecto
                elif headY == posicionYRandom and headX+1 == posicionXRandom and tipoFood==0:
                    score -=1
                    ventana.addstr(headY,headX+1,"#")
                    listaDE.addFinal(headY,headX+1)
                    ultimoEliminar = listaDE.colaLista
                    ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                    listaDE.deletFinal()
                    listaDE.deletFinal()
                    #codigo anterio pintadoTituloVentana - repinta el titulo por algun cambie en el score
                    pintadoTituloVentana(ventana,score,usuario)
                    #codigo anteriorcomidaRandom - para genera la comida aletroriamente en la pantalla
                    posicionYRandom , posicionXRandom, tipoFood = ComidaRandom(numFilas,numColum,ventana)
                
                #si no hay nada por delante que siga
                else:
                    ventana.addstr(headY,headX+1,"#")
                    listaDE.addFinal(headY,headX+1)
                    ultimoEliminar = listaDE.colaLista
                    ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                    listaDE.deletFinal()


            #revisa que lo que halla enfrente sea el borde - lo pinta al otro lado 
            elif headX+1 == numColum:
                ventana.addstr(headY,1,"#")
                listaDE.addFinal(headY,1)
                ultimoEliminar = listaDE.colaLista
                ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                listaDE.deletFinal()
            

        #--------------------Movimiento hacia la Izquierda--------------------
        elif direccionSnake == 260:
            head = listaDE.cabezaLista
            headY = head.posX
            headX = head.posY#aqui es -1

            #revisa si hacia la izquierda sea diferente a el borde
            if headX-1 != 1:
                #si el snake come un punto correcto
                if headY == posicionYRandom and headX-1 == posicionXRandom and tipoFood==1: 
                    score +=1
                    ventana.addstr(headY,headX-1,"#")
                    listaDE.addFinal(headY,headX-1)
                    ultimoEliminar = listaDE.colaLista
                    ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                    #codigo anterio pintadoTituloVentana - repinta el titulo por algun cambie en el score
                    pintadoTituloVentana(ventana,score,usuario)
                    #codigo anteriorcomidaRandom - para genera la comida aletroriamente en la pantalla
                    posicionYRandom , posicionXRandom, tipoFood = ComidaRandom(numFilas,numColum,ventana)

                #si el snake come un punto icorrecto
                elif headY == posicionYRandom and headX-1 == posicionXRandom and tipoFood==0:
                    score -=1
                    ventana.addstr(headY,headX-1,"#")
                    listaDE.addFinal(headY,headX-1)
                    ultimoEliminar = listaDE.colaLista
                    ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                    listaDE.deletFinal()
                    listaDE.deletFinal()
                    #codigo anterio pintadoTituloVentana - repinta el titulo por algun cambie en el score
                    pintadoTituloVentana(ventana,score,usuario)
                    #codigo anteriorcomidaRandom - para genera la comida aletroriamente en la pantalla
                    posicionYRandom , posicionXRandom, tipoFood = ComidaRandom(numFilas,numColum,ventana)
                
                #si no hay nada por delante que siga
                else:
                    ventana.addstr(headY,headX-1,"#")
                    listaDE.addFinal(headY,headX-1)
                    ultimoEliminar = listaDE.colaLista
                    ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                    listaDE.deletFinal()

            #revisa si hacia la izquierda ya llego al borde
            else:
                ventana.addstr(headY,numColum-1,"#")
                listaDE.addFinal(headY,numColum-1)
                ultimoEliminar = listaDE.colaLista
                ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                listaDE.deletFinal()


        #--------------------Movimiento hacia la arriba--------------------
        elif direccionSnake == 259:
            head = listaDE.cabezaLista
            headY = head.posX
            headX = head.posY

            #revisa si hacia arriba sea diferente a el borde
            if headY-1 != 1:
                #si el snake come un punto correcto
                if headY-1 == posicionYRandom and headX == posicionXRandom and tipoFood==1: 
                    score +=1
                    ventana.addstr(headY-1,headX,"#")
                    listaDE.addFinal(headY-1,headX)
                    ultimoEliminar = listaDE.colaLista
                    ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                    #codigo anterio pintadoTituloVentana - repinta el titulo por algun cambie en el score
                    pintadoTituloVentana(ventana,score,usuario)
                    #codigo anteriorcomidaRandom - para genera la comida aletroriamente en la pantalla
                    posicionYRandom , posicionXRandom, tipoFood = ComidaRandom(numFilas,numColum,ventana)

                #si el snake come un punto icorrecto
                elif headY-1 == posicionYRandom and headX == posicionXRandom and tipoFood==0:
                    score -=1
                    ventana.addstr(headY-1,headX,"#")
                    listaDE.addFinal(headY-1,headX)
                    ultimoEliminar = listaDE.colaLista
                    ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                    listaDE.deletFinal()
                    listaDE.deletFinal()
                    #codigo anterio pintadoTituloVentana - repinta el titulo por algun cambie en el score
                    pintadoTituloVentana(ventana,score,usuario)
                    #codigo anteriorcomidaRandom - para genera la comida aletroriamente en la pantalla
                    posicionYRandom , posicionXRandom, tipoFood = ComidaRandom(numFilas,numColum,ventana)
                
                #si no hay nada por delante que siga
                else:
                    ventana.addstr(headY-1,headX,"#")
                    listaDE.addFinal(headY-1,headX)
                    ultimoEliminar = listaDE.colaLista
                    ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                    listaDE.deletFinal()

            #revisa si hacia la izquierda ya llego al borde
            elif headY-1 == 1:
                ventana.addstr(numFilas-2,headX,"#")
                listaDE.addFinal(numFilas-2,headX)
                ultimoEliminar = listaDE.colaLista
                ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                listaDE.deletFinal()
                

        #--------------------Movimiento hacia la Abajo--------------------
        elif direccionSnake == 258:
            head = listaDE.cabezaLista
            headY = head.posX#aca es +1
            headX = head.posY
            #revisa si hacia arriba sea diferente a el borde
            if headY+1 != numFilas:

                #si el snake come un punto correcto
                if headY+1 == posicionYRandom and headX == posicionXRandom and tipoFood==1: 
                    score +=1
                    ventana.addstr(headY+1,headX,"#")
                    listaDE.addFinal(headY+1,headX)
                    ultimoEliminar = listaDE.colaLista
                    ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                    #codigo anterio pintadoTituloVentana - repinta el titulo por algun cambie en el score
                    pintadoTituloVentana(ventana,score,usuario)
                    #codigo anteriorcomidaRandom - para genera la comida aletroriamente en la pantalla
                    posicionYRandom , posicionXRandom, tipoFood = ComidaRandom(numFilas,numColum,ventana)

                #si el snake come un punto icorrecto
                elif headY+1 == posicionYRandom and headX == posicionXRandom and tipoFood==0:
                    score -=1
                    ventana.addstr(headY+1,headX,"#")
                    listaDE.addFinal(headY+1,headX)
                    ultimoEliminar = listaDE.colaLista
                    ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                    listaDE.deletFinal()
                    listaDE.deletFinal()
                    #codigo anterio pintadoTituloVentana - repinta el titulo por algun cambie en el score
                    pintadoTituloVentana(ventana,score,usuario)
                    #codigo anteriorcomidaRandom - para genera la comida aletroriamente en la pantalla
                    posicionYRandom , posicionXRandom, tipoFood = ComidaRandom(numFilas,numColum,ventana)
                
                #si no hay nada por delante que siga
                else:
                    ventana.addstr(headY+1,headX,"#")
                    listaDE.addFinal(headY+1,headX)
                    ultimoEliminar = listaDE.colaLista
                    ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                    listaDE.deletFinal()

            #revisa si hacia la izquierda ya llego al borde
            elif headY+1 == numFilas:
                ventana.addstr(1,headX,"#")
                listaDE.addFinal(1,headX)
                ultimoEliminar = listaDE.colaLista
                ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                listaDE.deletFinal()


        #---------------------Pausa en el juego-----------------------------
        #-----------------------letar p = 112---------------------------------
        elif direccionSnake == 112:
            direccionSnake = -1
            #generacion de reporte actual
            listaDE.GraListasDobleEnlazada()
            listaDE.imagenDot()

        
        
        direccionSnake = -1
        direccionSnake = ventana.getch()
        ventana.refresh()

    curses.endwin()
#-------------------------------fin del juego-----------------------------------------------------------



def inicioSnake(usuario,listaDE,ScorePila):
    listaDE.addHead(10,40)
    listaDE.addHead(10,39)
    listaDE.addHead(10,38)
    tamanioInicialSanke = 3
    if usuario == "":
        screen = curses.initscr()
        curses.noecho()
        curses.curs_set(1)
        numFilas , numColum = screen.getmaxyx()
        #usuario = screen.getstr()
        ventana = curses.newwin(numFilas, numColum, 0, 0)
        ventana.addstr(1,1,"Ingreses nombre de usuario : ")
        ventana.keypad(1)
        usuario = ventana.getstr()
        dibujoSnake(ventana,usuario,numFilas,numColum,listaDE,ScorePila,tamanioInicialSanke)
        

    else:
        numFilas , numColum = screen.getmaxyx()
        usuario = screen.getstr()


import curses#importacion de la libreria curses
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #impotaciones espaciales para leer el teclado
import subprocess
import os
import random #librearia para genera numeros random

#------------Generador de comida random en la pantalla--------------------------------------------------------
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
#-------------------------------------------------------------------------------------------------------------



#--------pintuado del borde con titulos para el usuario--------------------------------------------------------
def pintadoTituloVentana(ventana,score,usuario):
    ventana.clear()
    ventana.border(0)
    ventana.addstr(0,5," Score : "+str(score)+" ")
    ventana.addstr(0,40," SNAKE RELOADED ")
    nombre = str(usuario).replace("b'","")
    ventana.addstr(0, 70, " User : "+nombre.replace("'","")+" ")
    return nombre
#-------------------------------------------------------------------------------------------------------------
    


#--------pintado del snake y jugabilidad ----------------------------------------------------------------------
def dibujoSnake(ventana,usuario,numFilas,numColum,listaDE,Pila,tamanioInicialSanke,puntuacionMaxLevel,velocidadSanke,cola):
    direccionSnake = -1
    fooRandom = ""
    tipoFood = ""
    posicionXRandom = 0
    posicionYRandom = 0
    #lista inicial del snake
    score = 0 #va midiendo el puntuaje en el juegor
    curses.curs_set(0)

    #codigo anterio pintadoTituloVentana - repinta el titulo por algun cambie en el score
    nombreJugador = pintadoTituloVentana(ventana,score,usuario)

    #codigo anteriorcomidaRandom - para genera la comida aletroriamente en la pantalla
    
    posicionYRandom , posicionXRandom, tipoFood = ComidaRandom(numFilas,numColum,ventana)
    #ventana.timeout(velocidadSanke)#tiempor actualizacion me puede servir para los niveles en el snake

    
    direccionSnake = 261
    #ciclo que mantiene jugando al snake mientra sea diferente de esc=27 
    while direccionSnake !=27:
        #----------Velocidad en en el tiempo de refresh() en lapantalla - velocidad snake
        ventana.timeout(velocidadSanke)
        
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
        #direccionSnake = 261
        #-------------------------------------------------------Movimiento hacia la Derecha--------------------
        if direccionSnake == 261:
            head = listaDE.cabezaLista
            headY = head.posX
            headX = head.posY
            #revisa que lo que halla enfrente no sea el borde
            if headX+1 != numColum:
                
                #si el snake come un punto correcto
                if headY == posicionYRandom and headX+1 == posicionXRandom and tipoFood==1: 
                    score +=1#puntuacion actual
                    tamanioInicialSanke +=1#tamnio acutal del snake para ver si perdio
                    puntuacionMaxLevel +=1 #aumenta la puntacion para el siguiente nivel

                    ventana.addstr(headY,headX+1,"#")
                    listaDE.addFinal(headY,headX+1)
                    ultimoEliminar = listaDE.colaLista

                    #ingreso la comida # a la pila
                    Pila.Push(posicionYRandom,posicionXRandom)

                    ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                    #codigo anterio pintadoTituloVentana - repinta el titulo por algun cambie en el score
                    nombreJugador = pintadoTituloVentana(ventana,score,usuario)
                    #codigo anteriorcomidaRandom - para genera la comida aletroriamente en la pantalla
                    posicionYRandom , posicionXRandom, tipoFood = ComidaRandom(numFilas,numColum,ventana)

                    

                #si el snake come un punto icorrecto
                elif headY == posicionYRandom and headX+1 == posicionXRandom and tipoFood==0:
                    score -=1
                    tamanioInicialSanke -=1#tamnio acutal del snake para ver si perdio
                    puntuacionMaxLevel -=1 #aumenta la puntacion para el siguiente nivel

                    ventana.addstr(headY,headX+1,"#")
                    listaDE.addFinal(headY,headX+1)
                    ultimoEliminar = listaDE.colaLista

                    #saco el ultimo elemento bueno que comio antes
                    Pila.Pop()

                    ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                    listaDE.deletFinal()
                    listaDE.deletFinal()
                    #codigo anterio pintadoTituloVentana - repinta el titulo por algun cambie en el score
                    nombreJugador = pintadoTituloVentana(ventana,score,usuario)
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
                    score +=1#puntuacion actual
                    tamanioInicialSanke +=1#tamnio acutal del snake para ver si perdio
                    puntuacionMaxLevel +=1 #aumenta la puntacion para el siguiente nivel
                    
                    ventana.addstr(headY,headX-1,"#")
                    listaDE.addFinal(headY,headX-1)
                    ultimoEliminar = listaDE.colaLista

                    #ingreso la comida # a la pila
                    Pila.Push(posicionYRandom,posicionXRandom)

                    ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                    #codigo anterio pintadoTituloVentana - repinta el titulo por algun cambie en el score
                    nombreJugador = pintadoTituloVentana(ventana,score,usuario)
                    #codigo anteriorcomidaRandom - para genera la comida aletroriamente en la pantalla
                    posicionYRandom , posicionXRandom, tipoFood = ComidaRandom(numFilas,numColum,ventana)

                #si el snake come un punto icorrecto
                elif headY == posicionYRandom and headX-1 == posicionXRandom and tipoFood==0:
                    score -=1#puntuacion actual
                    tamanioInicialSanke -=1#tamnio acutal del snake para ver si perdio
                    puntuacionMaxLevel -=1 #aumenta la puntacion para el siguiente nivel
                    
                    ventana.addstr(headY,headX-1,"#")
                    listaDE.addFinal(headY,headX-1)
                    ultimoEliminar = listaDE.colaLista

                    #saco el ultimo elemento bueno que comio antes
                    Pila.Pop()

                    ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                    listaDE.deletFinal()
                    listaDE.deletFinal()
                    #codigo anterio pintadoTituloVentana - repinta el titulo por algun cambie en el score
                    nombreJugador = pintadoTituloVentana(ventana,score,usuario)
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
                    tamanioInicialSanke +=1#tamnio acutal del snake para ver si perdio
                    puntuacionMaxLevel +=1 #aumenta la puntacion para el siguiente nivel

                    
                    ventana.addstr(headY-1,headX,"#")
                    listaDE.addFinal(headY-1,headX)
                    ultimoEliminar = listaDE.colaLista
                    
                    #ingreso la comida # a la pila
                    Pila.Push(posicionYRandom,posicionXRandom)

                    ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                    #codigo anterio pintadoTituloVentana - repinta el titulo por algun cambie en el score
                    nombreJugador = pintadoTituloVentana(ventana,score,usuario)
                    #codigo anteriorcomidaRandom - para genera la comida aletroriamente en la pantalla
                    posicionYRandom , posicionXRandom, tipoFood = ComidaRandom(numFilas,numColum,ventana)

                #si el snake come un punto icorrecto
                elif headY-1 == posicionYRandom and headX == posicionXRandom and tipoFood==0:
                    score -=1#record acutal
                    tamanioInicialSanke -=1#tamnio acutal del snake para ver si perdio
                    puntuacionMaxLevel -=1 #aumenta la puntacion para el siguiente nivel

                    
                    ventana.addstr(headY-1,headX,"#")
                    listaDE.addFinal(headY-1,headX)
                    ultimoEliminar = listaDE.colaLista

                    #saco el ultimo elemento bueno que comio antes
                    Pila.Pop()

                    ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                    listaDE.deletFinal()
                    listaDE.deletFinal()
                    #codigo anterio pintadoTituloVentana - repinta el titulo por algun cambie en el score
                    nombreJugador = pintadoTituloVentana(ventana,score,usuario)
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
                    score +=1#record actual
                    tamanioInicialSanke +=1#tamnio acutal del snake para ver si perdio
                    
                    ventana.addstr(headY+1,headX,"#")
                    listaDE.addFinal(headY+1,headX)
                    ultimoEliminar = listaDE.colaLista
                    
                    #ingreso la comida # a la pila
                    Pila.Push(posicionYRandom,posicionXRandom)

                    ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                    #codigo anterio pintadoTituloVentana - repinta el titulo por algun cambie en el score
                    nombreJugador = pintadoTituloVentana(ventana,score,usuario)
                    #codigo anteriorcomidaRandom - para genera la comida aletroriamente en la pantalla
                    posicionYRandom , posicionXRandom, tipoFood = ComidaRandom(numFilas,numColum,ventana)

                #si el snake come un punto icorrecto
                elif headY+1 == posicionYRandom and headX == posicionXRandom and tipoFood==0:
                    score -=1#recrod actual
                    tamanioInicialSanke -=1#tamnio acutal del snake para ver si perdio
                    
                    ventana.addstr(headY+1,headX,"#")
                    listaDE.addFinal(headY+1,headX)
                    ultimoEliminar = listaDE.colaLista
                                        
                    #saco el ultimo elemento bueno que comio antes
                    Pila.Pop()

                    ventana.addstr(ultimoEliminar.posX,ultimoEliminar.posY," ")
                    listaDE.deletFinal()
                    listaDE.deletFinal()
                    #codigo anterio pintadoTituloVentana - repinta el titulo por algun cambie en el score
                    nombreJugador = pintadoTituloVentana(ventana,score,usuario)
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

        if tamanioInicialSanke==2:
            break
        

        #mantiene a la escucha del algun cambio desde el teclado para cambio de direccion
        # salir o pusa
        cambioSnake = ventana.getch()
        if cambioSnake==258 or cambioSnake==259 or cambioSnake==260 or cambioSnake==261 or cambioSnake ==27 or cambioSnake==112:
            direccionSnake = cambioSnake

        #------------Para el aumento de niveles - aumenta el tiempo de respuesta del snake
        if puntuacionMaxLevel == 15:
            puntuacionMaxLevel = 0
            vaciadoPila = 14
            while vaciadoPila >= 1:
                vaciadoPila -=1
                Pila.Pop()
            #cambio en la velocidad del snake    
            velocidadSanke = velocidadSanke - 20
            
            
        #velocidadSanke +=100
        #refresca la pantalla para los cambios que se realizaron
        ventana.refresh()


    
    curses.endwin()#termina el proces de l ventana de snake
    #generacion de escritura para genera los reportes
    listaDE.GraListasDobleEnlazada()
    Pila.GraPila()
    tamanioCola = cola.sizeCola
    if tamanioCola < 10:
        cola.addCola(nombreJugador,score)
    elif tamanioCola >=10:
        cola.addCola(nombreJugador,score)
        cola.unqueued()
        
#-------------------------------fin del juego-----------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------




#--------------------------Ventana de arranque - verificacion de usuario---------------------------------------
def inicioSnake(usuario,listaDE,Pila,cola):
    #----------Posiciones inciales del snake al comienzo de un juego-------------
    listaDE.addHead(10,40)
    listaDE.addHead(10,39)
    listaDE.addHead(10,38)
    #----------------------------------------------------------------------------
    tamanioInicialSanke = 3
    puntuacionMaxLevel = 0
    velocidadSanke = 100
    if usuario == "":
        screen = curses.initscr()
        curses.echo()#habila la escritura en la pantalla
        curses.curs_set(1)
        numFilas , numColum = screen.getmaxyx()
        #usuario = screen.getstr()
        ventana = curses.newwin(numFilas, numColum, 0, 0)
        ventana.addstr(1,1,"Ingreses nombre de usuario : ")
        ventana.keypad(1)
        usuario = ventana.getstr()
        curses.noecho()#desabilito la entrada por pantalla
        dibujoSnake(ventana,usuario,numFilas,numColum,listaDE,Pila,tamanioInicialSanke,puntuacionMaxLevel,velocidadSanke,cola)
        

    else:
        screen = curses.initscr()
        curses.echo()#desabilita la escritura en pantalla
        curses.curs_set(1)
        numFilas , numColum = screen.getmaxyx()
        ventana = curses.newwin(numFilas, numColum, 0, 0)
        ventana.keypad(1)
        dibujoSnake(ventana,usuario,numFilas,numColum,listaDE,Pila,tamanioInicialSanke,puntuacionMaxLevel,velocidadSanke,cola)
#-------------------------------------------------------------------------------------------------------------


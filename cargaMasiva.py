import csv
#from listaCirular import *#importo todo lo de mi modulo de lista circulas 
import curses #import the curses library
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library

def lecturaArchivo(ventana,nombreArchivo,listaCDE):
    archivo = str(nombreArchivo).replace("b'","")
    #--------------------Comprueba la existencia del archivo
    try:
        f = open(""+archivo.replace("'","")+".csv","r")
        ventana.addstr(10,10,"archivo cargado")
        lecturas = []
        with open(""+archivo.replace("'","")+".csv",newline = '') as File:
            reader = csv.reader(File)
            for row in reader:
                if row == "usuario":
                    pass 
                else:
                    lecturas.append(row)
                    listaCDE.addLCDE(row)
    except:
        ventana.addstr(10,10,"el archvio no exite : "+str(archivo).replace("'",""))
        return 27
    ventana.refresh()

    


def ventanaCargaMasiva(listaCDE):
    
    #index = 1
    screen = curses.initscr()
    curses.echo()#habila la escritura en la pantalla
    numFilas , numColum = screen.getmaxyx()
    Y = numFilas//2 -5
    X = numColum//2 -5
    posNombresUsuarios = X - 6
    ventana = curses.newwin(numFilas, numColum, 0, 0)

    #------------ingreso del nombre del archivo---------------------------
    ventana = curses.newwin(numFilas, numColum, 0, 0)
    ventana.addstr(5,5,"Ingres nombre del archivo : ")
    ventana.keypad(1)
    nombreArchivo = ventana.getstr()
    curses.noecho()#desabilito la entrada por pantalla
    curses.curs_set(0)
    #---------------ingreso para la busqueda del archivo-------------------
    teclado = lecturaArchivo(ventana,nombreArchivo,listaCDE)
    #----------------------------------------------------------------------
    ventana.clear()
    ventana.border(0)
    ventana.keypad(True)
    centroX = int(numColum / 2)
    ventana.addstr(0,X," Users ")
    ventana.refresh()
    ventana.timeout(-1) # mantiene la ventan indefinidadmente mientra se utilize el comando getch() para una entrada en pantalls
 
    #matiene abierto mientras teclas sean diferentes a la teclas esc
    if teclado == 27:
        teclado = 27
    else:
        usuarios = listaCDE.cabezaLista
        teclado = ventana.getch()

    while teclado !=27: 

        if teclado == 260:
            ventana.clear()
            ventana.border(0)
            ventana.addstr(0,X," Users ")
            usuarios = usuarios.anteriorLCDE
            valor = str(usuarios.nombreUsuario).replace("['","")
            ventana.addstr(Y,posNombresUsuarios," <--- " +valor.replace("']","")+" ---> " )
            ventana.addstr(Y+3,X-3," Salir (Esc) ")
            ventana.refresh()

        elif teclado == 261:
            ventana.clear()
            ventana.border(0)
            ventana.addstr(0,X," Users ")
            usuarios = usuarios.siguienteLCDE
            valor = str(usuarios.nombreUsuario).replace("['","")
            ventana.addstr(Y,posNombresUsuarios," <--- " +valor.replace("']","")+" ---> " )
            ventana.addstr(Y+3,X-3," Salir (Esc) ")
            ventana.refresh()
            
        elif teclado == 10:
            return valor
            pass
        
        teclado = ventana.getch()
        if teclado ==10:
            break
            listaCDE.GraCircular()

        telado = -1
        ventana.refresh()

    curses.endwin()
    return ""
    listaCDE.GraCircular()


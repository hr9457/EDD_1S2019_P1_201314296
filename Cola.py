import os
# importaciones
# importacion para lectura y escritura de un archivo
from io import *

# clase nodo
# estructura del nodo
class Nodo:
    # metodo contructor
    def __init__(self,nombreUsuario,score):
        self.nombreUsuario = nombreUsuario
        self.score = score
        self.siguienteCola = None
#-------------------------------------------------------------------------------------------------

# estructura de la cola
# clase cola
class Cola:
    # metodo contructor
    def __init__(self):
        self.primeroCola = None
        self.ultimoCola = None
        self.sizeCola = 0
    #-------------------------------------------------------------------------------------------------

    # metodo para agregar en la cola
    def addCola(self,nombreUsuario,score):
        if self.primeroCola == None and self.ultimoCola==None:
            # creacion de un nuevo nodo
            nuevoNodo = Nodo(nombreUsuario,score)
            self.primeroCola = nuevoNodo
            self.ultimoCola = nuevoNodo
            self.sizeCola += 1
        else:
            # creacion de un nuevo nodo
            nuevoNodo = Nodo(nombreUsuario,score)
            self.ultimoCola.siguienteCola = nuevoNodo
            self.ultimoCola = nuevoNodo
            self.sizeCola += 1
    #-------------------------------------------------------------------------------------------------


    # metodo para elminar de la cola
    def unqueued(self):
        if self.primeroCola == None and self.ultimoCola == None:
            print("la cola esta vacia")
        elif self.primeroCola == self.ultimoCola:
            self.primeroCola = None
            self.ultimoCola = None
            self.sizeCola -= 1
        else:
            temporal = self.primeroCola
            self.primeroCola = self.primeroCola.siguienteCola
            temporal = None
            self.sizeCola -= 1
    #-------------------------------------------------------------------------------------------------


    #  get tamaniio de la cola actual
    def getSizeCola(self):
        return self.sizeCola
    #-------------------------------------------------------------------------------------------------


    # metodo para imprimir la cola
    def printCola(self):
        # variable temporal
        primeroTemporal = self.primeroCola
        # tamanio acutal de la cola
        temporalSize = self.sizeCola
        while temporalSize > 0:
            print(primeroTemporal.nombreUsuario)
            primeroTemporal = primeroTemporal.siguienteCola
            temporalSize -= 1
    #-------------------------------------------------------------------------------------------------



    #---------------Escritura del reporte de la cola--------------------------------------
    def GraCola(self):
        #-----------------------------------------------------------------------------------------------------
        #lectura del archivo y limpiado del archivo
        archivo_texto = open("Cola.txt","r")
        lineas = archivo_texto.readlines()
        archivo_texto.close()
        #vaciado del archivo 
        archivo_texto = open("Cola.txt","w")
        for lineas in lineas:
            archivo_texto.write("")
        archivo_texto.close()
        #------------------------------------------------------------------------------------------------------
        
        #sobre-escritura  para genera graphviz
        archivo_texto = open("Cola.txt","w")
        archivo_texto.write("digraph{\n")#encabezado
        archivo_texto.write("rankdir=LR;\n")#direccion 
        archivo_texto.write("subgraph cluster_0{color = lightgrey; node[shape=record]\n")#poscion del titulo
        #recorrimiento de la lista
        # variable temporal
        primeroTemporal = self.primeroCola
        # tamanio acutal de la cola
        temporalSize = self.sizeCola
        numeroDeNodo = 0 # variable para enumerar los nodos
        while temporalSize > 0:
            archivo_texto.write("Nodo"+str(numeroDeNodo)+"[label=\" { "+str(primeroTemporal.nombreUsuario)+","+ str(primeroTemporal.score)+ " | } \"];\n" )
            primeroTemporal = primeroTemporal.siguienteCola
            numeroDeNodo += 1 #aumenta el numero del nodo
            temporalSize -= 1 #disminue el numero para recorrer la lista
            #para la union de nodos
            if temporalSize <= 0:
                numeroDeNodo = numeroDeNodo - 1 # variable para enumerar los nodos
                while temporalSize +1   < self.sizeCola:
                    archivo_texto.write("Nodo"+str(numeroDeNodo)+"->Nodo"+str(numeroDeNodo-1)+"\n")
                    numeroDeNodo -= 1
                    temporalSize += 1
                break
        #fin del ciclo while
        archivo_texto.write("Nodo"+str(numeroDeNodo)+"->Null\n")
        #fin del recorrido de la cola    
        archivo_texto.write("label = \" Cola \";\n")#titulo del grafo
        archivo_texto.write("}\n")#
        archivo_texto.write("}\n")#
        archivo_texto.close()#cierre del archivo
    #-------------------------------------------------------------------------------------------------



    #-----------apertura del reporte que se genero------------------------------------------------------------
    def imagenDot(self):
        #creacon de la imagen dot
        os.system("dot -Tpng  C:\\Users\\HECTOR\\Documents\\EDD\\EDD_1S2019_P1_201314296\\Cola.txt -o C:\\Users\\HECTOR\\Documents\\EDD\\EDD_1S2019_P1_201314296\\Cola.png ")
        #apertura de la imagen dot
        os.system("C:\\Users\\HECTOR\\Documents\\EDD\\EDD_1S2019_P1_201314296\\Cola.png" )
    #-------------------------------------------------------------------------------------------------




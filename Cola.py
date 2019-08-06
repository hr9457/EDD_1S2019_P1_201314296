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

# estructura de la cola
# clase cola
class Cola:
    # metodo contructor
    def __init__(self):
        self.primeroCola = None
        self.ultimoCola = None
        self.sizeCola = 0

    # metodo para agregar en la cola
    def addCola(self,nombreUsuario,score):
        if self.primeroCola == None and self.ultimoCola == None:
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


    # metodo para elminar de la cola
    def unqueued(self):
        if self.primeroCola == None and self.ultimoCola == None:
            print("la cola esta vacia")
        elif self.primeroCola == self.ultimoCola:
            self.primeroCola = None
            self.ultimoCola = None
            self.sizeCola -= 1
        else:
            self.primeroCola = self.primeroCola.siguienteCola
            self.sizeCola -= 1




    #  get tamaniio de la cola actual
    def getSizeCola(self):
        return self.sizeCola


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


    def GraCola(self):
        #lectura del archivo
        archivo_texto = open("Cola.txt","r")
        lineas = archivo_texto.readlines()
        archivo_texto.close()
        #vaciado del archivo 
        archivo_texto = open("Cola.txt","w")
        for lineas in lineas:
            archivo_texto.write("")
        archivo_texto.close()
        #escritura  para genera graphviz
        archivo_texto = open("Cola.txt","w")
        archivo_texto.write("digraph{\n")#encabezado
        archivo_texto.write("rankdir=LR;\n")#direccion 
        archivo_texto.write("subgraph cluster_0{color = lightgrey; node[shape=rectangle]\n")#poscion del titulo
        #recorrimiento de la lista
        # variable temporal
        primeroTemporal = self.primeroCola
        # tamanio acutal de la cola
        temporalSize = self.sizeCola
        numeroDeNodo = 0 # variable para enumerar los nodos
        while temporalSize > 0:
            archivo_texto.write("Nodo"+str(numeroDeNodo)+"[label=\" "+str(primeroTemporal.nombreUsuario)+"\"];\n")
            primeroTemporal = primeroTemporal.siguienteCola
            numeroDeNodo += 1 #aumenta el numero del nodo
            temporalSize -= 1 #disminue el numero para recorrer la lista
            if temporalSize <= 0:
                numeroDeNodo = 0 # variable para enumerar los nodos
                while numeroDeNodo + 1  < self.sizeCola:
                    archivo_texto.write("Nodo"+str(numeroDeNodo)+"->Nodo"+str(numeroDeNodo+1)+"\n")
                    numeroDeNodo += 1
        #fin del ciclo while
        archivo_texto.write("Nodo"+str(numeroDeNodo)+"->Null\n")
        #fin del recorrido de la cola    
        archivo_texto.write("label = \"Lista enlazada simple\";\n")#
        archivo_texto.write("}\n")#
        archivo_texto.write("}\n")#
        archivo_texto.close()#cierre del archivo




if __name__ == "__main__":
    c = Cola()
    c.addCola("hector","1")
    c.addCola("josue","2")
    c.addCola("orozco","3")
    print("el tamanio de la cola es: " + str( c.getSizeCola()) )
    c.printCola()
    #c.unqueued()
    #print("el tamanio de la cola es: " + str( c.getSizeCola()) )
    #c.printCola()
    c.GraCola()

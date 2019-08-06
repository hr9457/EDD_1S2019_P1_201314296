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



""""
if __name__ == "__main__":
    c = Cola()
    c.addCola("hector","1")
    c.addCola("josue","2")
    c.addCola("orozco","3")
    print("el tamanio de la cola es: " + str( c.getSizeCola()) )
    c.printCola()
    c.unqueued()
    print("el tamanio de la cola es: " + str( c.getSizeCola()) )
    c.printCola()
"""""
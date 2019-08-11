#clase nodo
#estructru del nodo
class Nodo:

    # metoodo contructor
    # lCDE = lista circula doblemente enlazada
    def __init__(self,nombreUsuario):
        self.nombreUsuario = nombreUsuario
        self.siguienteLCDE = None
        self.anteriorLCDE = None

    # metodos para obetner los valores de cada nodo 
    # si fueran neseario 
    def getNombreUsuario(self):
        return self.nombreUsuario

    def getSiguienteLCDE(self):
        return self.siguienteLCDE

    def getAnteriorLCDE(self):
        return self.anteriorLCDE


# clase lista
# es una lista circular doblemente enlzada
# estructura de la lista
class listaCircularDoblementeEnlazada:
    # metodo contructor
    def __init__(self):
        self.cabezaLista = None
        self.colaLista = None
        self.sizeLCDE = 0
        self.inicio = None

    # metodo para agregar a la lista
    def addLCDE(self,nombreUsuario):
        if  self.colaLista == None:
            nuevoNodo = Nodo(nombreUsuario)
            self.cabezaLista = nuevoNodo
            self.colaLista = nuevoNodo
            nuevoNodo.siguienteLCDE = self.colaLista
            nuevoNodo.anteriorLCDE = self.cabezaLista
            self.sizeLCDE += 1
        else:
            nuevoNodo = Nodo(nombreUsuario)
            nuevoNodo.anteriorLCDE = self.colaLista
            self.colaLista.siguienteLCDE = nuevoNodo
            self.colaLista = nuevoNodo
            self.colaLista.siguienteLCDE = self.cabezaLista
            self.cabezaLista.anteriorLCDE = self.colaLista
            self.sizeLCDE += 1

    def printLCDE(self):
        temporal = self.cabezaLista
        print(temporal.nombreUsuario)
        temporal = temporal.siguienteLCDE
        print(temporal.nombreUsuario)
        temporal = temporal.siguienteLCDE
        print(temporal.nombreUsuario)


    def siguiente():
        actual = self.cabezaLista
        print (actual)

    # metodo para devolver el tamanio de la lista
    def getSizeLCDE(self):
        return self.sizeLCDE

    def getCabeza(self):
        return self.cabezaLista

    def getCola(self):
        return self.colaLista

    def getInicio(self):
        return self.inicio

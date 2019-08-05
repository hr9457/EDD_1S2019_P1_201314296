#clase nodo
#estructra del nodo 
class Nodo:
    # metodo contructor
    def __init__(self,posX,posY):
        self.posX = posX #posicion en x del snake
        self.posY = posY #poisicon en y del snake
        self.siguiente = None #enlaze al siguiente elemento
        self.anterior = None #enlaze al anteririo elemento

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY


#clase lista 
#lista doblemente enlazada
class listaDobleEnlazada:
    # metodo contructor
    def __init__(self):
        self.cabezaLista = None
        self.colaLista = None
        self.sizeListaDoble = 0

    # metodo para devolver el tamanio de la lista
    def getSizeLista(self):
        return self.sizeListaDoble
        
    # metodo cuando en el snake come por la head 
    def addHead(self,posX,posY):
        # si la lista se encuentra vacias
        if self.cabezaLista == None and self.colaLista == None:
            nuevoNodo = Nodo(posX,posY)
            self.cabezaLista = nuevoNodo
            self.colaLista = nuevoNodo
            self.sizeListaDoble += 1
        else:
            nuevoNodo = Nodo(posX,posY)
            nuevoNodo.siguiente = self.colaLista
            self.colaLista.anterior = nuevoNodo
            self.colaLista = nuevoNodo
            self.sizeListaDoble += 1
    
    # metodo 
    def addFinal(self,posX,posY):
        # si la lista se encuentra vacia
        if self.cabezaLista == None and self.colaLista == None:
            nuevoNodo = Nodo(posX,posY)
            self.cabezaLista = nuevoNodo
            self.colaLista = nuevoNodo
            self.sizeListaDoble += 1
        else:
            nuevoNodo = Nodo(posX,posY)
            nuevoNodo.anterior = self.cabezaLista
            self.cabezaLista.siguiente = nuevoNodo
            self.cabezaLista = nuevoNodo
            self.sizeListaDoble += 1

    # metodo para imprimir la lista enlzada doble
    def printLista(self):
        nodoTemporal = self.colaLista
        sizeTemporal = self.sizeListaDoble
        while sizeTemporal >= 1:
            sizeTemporal -= 1
            print(nodoTemporal.posY)
            nodoTemporal = nodoTemporal.siguiente
            #self.colaLista = nodoTemporal.siguiente
        #retablezco valores

    def prubaPrint(self):
        print(self.colaLista.getPosY())
            

    

'''
if __name__ == "__main__":
    lsDoble = listaDobleEnlazada()
    lsDoble.addHead(0,0)
    lsDoble.addHead(0,1)
    lsDoble.addHead(0,2)
    print("tamanio de la lista: " + str(lsDoble.getSizeLista()) )
    lsDoble.printLista()
    lsDoble.addFinal(0,3)
    print("tamanio de la lista: " + str(lsDoble.getSizeLista()) )
    lsDoble.printLista()
'''
   
# clase nodo
# estructura del nodo
class NodoPila:
    # metodo contructor
    def __init__(self,posX,posY):
        self.posX = posX
        self.posY = posY
        self.siguientePila = None

# clase pila
# estrucura como se guardar los datos - pila
class pila:
    # metodo contructo
    def __init__(self):
        self.primeroPila = None
        self.ultimoPila = None
        self.sizePila = 1

    # metodo para insertar en la pila
    def Pop(self,posX,posY):
        if self.ultimoPila == None:
            nuevoNodo = NodoPila(posX,posY)
            self.primeroPila = nuevoNodo
            self.ultimoPila = nuevoNodo
            self.sizePila += 1
        else:
            nuevoNodo = NodoPila(posX,posY)
            nuevoNodo.siguientePila = self.primeroPila
            self.primeroPila = nuevoNodo
            self.sizePila += 1

    # metodo para retornar el tamanio de la pila
    def getSizePila(self):
        return self.sizePila

    def printPila(self):
        temporalSize = self.sizePila
        primerElemento = self.primeroPila
        while temporalSize > 1:
            temporalSize -= 1
            print(primerElemento.posY)
            primerElemento = primerElemento.siguientePila
        
            


# clse de arranque
# prueba de pila
if __name__ == "__main__":
    p = pila()
    
    p.Pop(1,1)
    p.Pop(1,2)
    p.Pop(1,3)
    print("elementos en la pila: "+  str(p.getSizePila())  )
    p.printPila()




        

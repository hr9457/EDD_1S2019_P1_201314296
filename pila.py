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
    def Push(self,posX,posY):
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

    # metodo para eliminar al principio de la pila
    def Pop(self):
        if self.primeroPila == None:
            print("la pila no contiene elemento ")
        elif self.primeroPila == self.ultimoPila:
            self.primerElemento = None
            self.ultimoPila = None
            self.sizePila -= 1
        else:
            temporal = self.primeroPila
            self.primeroPila = self.primeroPila.siguientePila
            temporal = None
            self.sizePila -= 1
            


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
    
    p.Push(1,1)
    p.Push(1,2)
    p.Push(1,3)
    print("elementos en la pila: "+  str(p.getSizePila())  )
    p.printPila()
    p.Pop()
    print("elementos en la pila: "+  str(p.getSizePila())  )
    p.printPila()




        

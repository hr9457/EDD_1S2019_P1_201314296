import os
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
    
    # metodo cuando come al final agrega a la cabeza de la lista
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

    #elemento para elminar al final de la lista
    def deletFinal(self):
        if self.colaLista == None:
            pass
        elif self.colaLista == self.cabezaLista:
            self.colaLista = None
            self.cabezaLista = None
            self.sizeListaDoble -= 1
        else:
            temporal = self.colaLista
            self.colaLista = self.colaLista.siguiente
            self.colaLista.anterior = None
            temporal = None
            self.sizeListaDoble -= 1

    #metodo para eliminar un elemento al frente de la lista
    def deletHead(self):
        if self.cabezaLista == None:
            pass
        elif self.cabezaLista == self.colaLista:
            self.cabezaLista = None
            self.colaLista = None
            self.sizeListaDoble -= 1
        else:
            temporal = self.cabezaLista
            self.cabezaLista = self.cabezaLista.anterior
            self.cabezaLista.siguiente = None
            temporal = None
            self.sizeListaDoble -= 1

    def buscar(self,y,x):
        aux = self.cabezaLista
        while aux != None:
            if aux.posX==y and aux.posY==x:
                return True
            aux = aux.siguiente
        return False



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


    # metodo para genera el reporte de la lista
    def GraListasDobleEnlazada(self):
        #-----------------------------------------------------------------------------------------------------
        #lectura del archivo y limpiado del archivo
        #LDE - LISTA DOBLEMENTE ENLAZADA 
        archivo_texto = open("LDE.txt","r")
        lineas = archivo_texto.readlines()
        archivo_texto.close()
        #vaciado del archivo 
        archivo_texto = open("LDE.txt","w")
        for lineas in lineas:
            archivo_texto.write("")
        archivo_texto.close()
        #------------------------------------------------------------------------------------------------------

        #sobre-escritura  para genera graphviz
        archivo_texto = open("LDE.txt","w")
        archivo_texto.write("digraph{\n")#encabezado
        archivo_texto.write("rankdir=LR;\n")#direccion 
        archivo_texto.write("subgraph cluster_0{node[shape=record]\n")#poscion del titulo
        archivo_texto.write(" NodoNull[ label = \" {null} \" ]; \n")#nodo por defecto para apuntar a null al principio de la lista
        #ciclo para la impresion de los elementos en la lista

        # variable para enumerar los nodos
        numeroNodo = 0
        # variable temporal para saber el tamanio de la lista
        sizeTemporal = self.sizeListaDoble
        # nodo temporal obtener la informacion desde la cola de la lista
        nodoTemporal = self.colaLista
        while  sizeTemporal >= 1:
            sizeTemporal -= 1
            archivo_texto.write(" Nodo" + str(numeroNodo) + " [label= \" {| " + str(nodoTemporal.posX) 
                                + "," + str(nodoTemporal.posY) + " |} \" ];\n" )
            nodoTemporal = nodoTemporal.siguiente 
            numeroNodo += 1
            if sizeTemporal <= 0:
                archivo_texto.write(" NodoNull->Nodo0 \n")
                archivo_texto.write(" Nodo0->NodoNull \n")
                #ciclo para hacer los apuntadores
                numeroNodo = 0
                while sizeTemporal+1 < self.sizeListaDoble:
                    archivo_texto.write(" Nodo"+str(numeroNodo)+"-> Nodo"+str(numeroNodo+1)+"\n" )
                    archivo_texto.write(" Nodo"+str(numeroNodo+1)+"->Nodo"+str(numeroNodo)+"\n" )
                    numeroNodo += 1
                    sizeTemporal += 1
                    #fin del ciclo while    
                break # break cierre del if               
        # fin del primer ciclo while
        #union del ultimo nodo a null
        archivo_texto.write(" Nodo"+str(numeroNodo)+"->Null\n")
        archivo_texto.write("label = \"Lista Doblemente Enlazada\";\n")#titulo del grap lista
        archivo_texto.write("}\n")#
        archivo_texto.write("}\n")#
        archivo_texto.close()#cierre del archivo


    def imagenDot(self):
        #creacon de la imagen dot
        os.system("dot -Tpng  C:\\Users\\HECTOR\\Documents\\EDD\\EDD_1S2019_P1_201314296\\LDE.txt -o C:\\Users\\HECTOR\\Documents\\EDD\\EDD_1S2019_P1_201314296\\LDE.png ")
        #apertura de la imagen dot
        os.system("C:\\Users\\HECTOR\\Documents\\EDD\\EDD_1S2019_P1_201314296\\LDE.png" )

       
            

#if __name__ == "__main__":
    #l = listaDobleEnlazada()
    #l.addHead(10,10)
    #l.addHead(10,11)
    #l.addHead(10,12)
    #l.printLista()
    #l.deletFinal()
    #l.printLista()
    #l.GraListasDobleEnlazada()
    #l.imagenDot()

   
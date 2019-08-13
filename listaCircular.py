import os
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

    def GraCircular(self):
        #-----------------------------------------------------------------------------------------------------
        #lectura del archivo y limpiado del archivo
        #LDE - LISTA DOBLEMENTE ENLAZADA 
        archivo_texto = open("Circular.txt","r")
        lineas = archivo_texto.readlines()
        archivo_texto.close()
        #vaciado del archivo 
        archivo_texto = open("Circular.txt","w")
        for lineas in lineas:
            archivo_texto.write("")
        archivo_texto.close()
        #------------------------------------------------------------------------------------------------------
        archivo_texto = open("Circular.txt","w")
        archivo_texto.write("digraph{\n")#encabezado
        archivo_texto.write("rankdir=LR;\n")#direccion 
        archivo_texto.write("subgraph cluster_0{node[shape=record]\n")#poscion del titulo
        #archivo_texto.write(" NodoNull[ label = \" {null} \" ]; \n")#nodo por defecto para apuntar a null al principio de la lista
        #ciclo para la impresion de los elementos en la lista

        # variable para enumerar los nodos
        numeroNodo = 0
        # variable temporal para saber el tamanio de la lista
        sizeTemporal = self.sizeLCDE
        # nodo temporal obtener la informacion desde la cola de la lista
        nodoTemporal = self.colaLista
        while  sizeTemporal >= 1:
            sizeTemporal -= 1
            archivo_texto.write(" Nodo" + str(numeroNodo) + " [label= \" {<ant>| " + str(nodoTemporal.nombreUsuario) + " |<next>} \" ];\n" )
            nodoTemporal = nodoTemporal.siguienteLCDE
            numeroNodo += 1
            if sizeTemporal <= 0:
                #archivo_texto.write(" NodoNull->Nodo0 \n")
                #archivo_texto.write(" Nodo0->NodoNull \n")
                #ciclo para hacer los apuntadores
                numeroNodo = 0
                while sizeTemporal+1 < self.sizeLCDE:
                    archivo_texto.write(" Nodo"+str(numeroNodo)+"-> Nodo"+str(numeroNodo+1)+"\n" )
                    archivo_texto.write(" Nodo"+str(numeroNodo+1)+"->Nodo"+str(numeroNodo)+"\n" )
                    numeroNodo += 1
                    sizeTemporal += 1
                    #fin del ciclo while    
                break # break cierre del if               
        # fin del primer ciclo while
        archivo_texto.write(" Nodo0 -> Nodo"+str(sizeTemporal)+"\n")
        archivo_texto.write("Nodo"+str(sizeTemporal)+" -> Nodo0\n")
        archivo_texto.write("label = \"Lista Cirular\";\n")#titulo del grap lista
        archivo_texto.write("}\n")#
        archivo_texto.write("}\n")#
        archivo_texto.close()#cierre del archivo


    def imagenDot(self):
        #creacon de la imagen dot
        os.system("dot -Tpng  C:\\Users\\HECTOR\\Documents\\EDD\\EDD_1S2019_P1_201314296\\Circular.txt -o C:\\Users\\HECTOR\\Documents\\EDD\\EDD_1S2019_P1_201314296\\Circular.png ")
        #apertura de la imagen dot
        os.system("C:\\Users\\HECTOR\\Documents\\EDD\\EDD_1S2019_P1_201314296\\Circular.png" )



    # metodo para devolver el tamanio de la lista
    def getSizeLCDE(self):
        return self.sizeLCDE

    def getCabeza(self):
        return self.cabezaLista

    def getCola(self):
        return self.colaLista

    def getInicio(self):
        return self.inicio

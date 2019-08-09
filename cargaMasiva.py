import csv
from listaCirular import *#importo todo lo de mi modulo de lista circulas 


def lecturaArchivo():
    lecturas = []
    with open('usuarios.csv',newline = '') as File:
        reader = csv.reader(File)
        for row in reader:
            lecturas.append(row)

    print (lecturas[0])
    
def pintadoVentana(ventana):
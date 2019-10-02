import numpy as np
import copy
import linkedlist
import math
class tablero:
    # Ej Tablero [0,1,2,3,4,5,6,7]
    def __init__(self, arreglo):
        self.arreglo = arreglo
        self.maximo = len(self.arreglo) - 1
        self.menor = math.factorial(len(arreglo))
        self.heuristica = self.calculoH(self.arreglo)
        # Agregamos las reinas en el tablero
        self.ponerReinas(self.arreglo)
        self.pares = {}
        for i in range(0, len(arreglo)):
            self.pares[i] = linkedlist.LinkedList()

        self.printTablero()
        print("H principal = " , self.calculoH(self.arreglo))
        self.calculoHs(self.arreglo)

        #self.printTablero()
    def ponerReinas(self,arreglo):
        self.tablero = np.zeros((len(arreglo), len(arreglo)))
        for i in range(0, len(arreglo)):
            self.tablero[arreglo[i]][i] = -1
    # [4,5,6,3,4,5,6,5]
    # [0,5,6,3,4,5,6,5]
    def calculoHs(self,arreglo):
        seEncontroUnMenor = False
        if (self.heuristica == 0):
            print("Se ha llegado a una solución con H = 0")
            self.printTablero()
            return
        for i in range(0,len(arreglo)):
            copia = copy.deepcopy(arreglo)
            for j in range(0,len(arreglo)):
                if (self.tablero[j][i] != -1):
                    copia[i] = j
                    self.tablero[j][i] = self.calculoH(copia)
                    if (self.tablero[j][i] < self.menor):
                        self.menor = self.tablero[j][i]
                        self.arreglo = copia
                        seEncontroUnMenor = True
                    #print("[",copia[0],",",copia[1],",",copia[2],",",copia[3],",",copia[4],",",copia[5],",",copia[6],",",copia[7],"] =", self.tablero[i][j])
        #self.printTablero()
        if (seEncontroUnMenor == False):
            self.ponerReinas(self.arreglo)
            print("Se ha llegado a un máximo local")
            self.printTablero()
            print("H = ", int(self.menor))
            return
        self.ponerReinas(self.arreglo)
        self.calculoHs(self.arreglo)

    def calculoH(self,arreglo):
        h = 0
        for x in range(0, len(arreglo)):
            h = h + self.calculoHorizontal(x, arreglo)
            h = h + self.calculoDiagonal(x, arreglo)
        return h
    def calculoHorizontal(self,k,arreglo):
        h = 0
        for i in range(k+1, len(arreglo)):
            if (arreglo[k] == arreglo[i]):
                h = h + 1
        return h
    def calculoDiagonal(self,k,arreglo):
       h = 0
       for i in range(k+1,len(arreglo)):
           if (abs(arreglo[k]-arreglo[i]) == abs(k-i)):
               h = h + 1
       return h
    def printTablero(self):
        for a in range(0, self.maximo+1):
            for b in range(0, self.maximo+1):
                if (self.tablero[a][b] == -1):
                    print("|", "♕", end=' ')
                else:
                    print("|", "%2d"%int(self.tablero[a][b]), end=' ')
            print("|")
import numpy as np
import copy
import linkedlist
import math
import random
class SimulatedAnnealing:
    # Ej Tablero [0,1,2,3,4,5,6,7]
    def __init__(self, arreglo):
        self.arreglo = arreglo
        self.maximo = len(self.arreglo) - 1
        self.menor = math.factorial(len(arreglo))
        self.heuristica = self.calculoH(self.arreglo)
        self.i = 1
        # Agregamos las reinas en el tablero
        self.ponerReinas(self.arreglo)
        self.pares = {}
        for i in range(0, len(arreglo)):
            self.pares[i] = linkedlist.LinkedList()

        self.printTablero()
        print("H principal = " , self.calculoH(self.arreglo))
        x = self.simulatedannealing()
        self.ponerReinas(x)
        self.printTablero()
        print("H = ", self.calculoH(x))
        print("Se ha resuelto el tablero en ", self.i, " pasos")
        #self.printTablero()
    def simulatedannealing(self):
        current = self.arreglo
        next = None
        while(True):
            if (self.calculoH(current) == 0):
                return current
            next = self.randomSuccesor(current)
            deltaE = self.calculoH(next) -self.calculoH(current)
            if (deltaE > 0):
                current = next
            else:
                if (math.exp(deltaE / self.i) > random.randint(0, 1)):
                    current = next
            self.i = self.i + 1
    def randomSuccesor(self,array):
        # Tomamos un indice aleatorio del arreglo
        ind = random.randint(0,len(array)-1)
        # Ahora le asignamos un valor distinto al indice
        x = array[ind]
        p = x
        while (p == x):
            p = random.randint(0, len(array)-1)
        array[ind] = p
        return array

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
                    print("\33[31m♕\033[0m", end=' ')
                elif (self.tablero[a][b] == 0 and (a+b)%2 == 0):
                    print("\033[33m⬛\033[0m", end=' ')
                elif (self.tablero[a][b] == 0 and (a+b)%2 == 1):
                    print("\033[30m⬜\033[0m", end=' ')
                else:
                    print("%2d"%int(self.tablero[a][b]), end=' ')
            print("")
import numpy as np
import copy
import linkedlist
import math
import random
class AlgoritmosGeneticos:
    # Ej Tablero [0,1,2,3,4,5,6,7]
    def __init__(self, arreglo):
        self.arreglo = arreglo
        self.maximo = len(self.arreglo) - 1
        self.menor = math.factorial(len(arreglo))
        self.heuristica = self.calculoH(self.arreglo)
        self.cantidad = 0
        self.rate = 50
        # Agregamos las reinas en el tablero
        self.ponerReinas(self.arreglo)
        self.pares = {}
        for i in range(0, len(arreglo)):
            self.pares[i] = linkedlist.LinkedList()

        self.printTablero()
        print("H principal = " , self.calculoH(self.arreglo))
        i = 0
        while (self.heuristica != 0):
            self.seleccionPorTorneos((self.maximo-(int(self.maximo/2)))**2)
            self.heuristica = self.calculoH(self.arreglo)
            print("H[", i, "] = ", self.heuristica, " ", self.arreglo)
            #print("movemos un slot")
            self.moverUno()

            i = i + 1
        self.ponerReinas(self.arreglo)
        self.printTablero()
        print(self.arreglo, " H = 0")
    def seleccion(self,arreglo):
        arreglo2 = copy.deepcopy(arreglo)
        #print("entra ",arreglo)
        for i in range(0,len(arreglo)):
            x = (self.fitnessDiagonal(arreglo,arreglo[i])+ self.fitnessHorizontal(arreglo,arreglo[i]))
            #print("x = ",x, ", self.heuristica ", self.heuristica)
            #print("rate ", self.rate)
            if (x == 0 or (x >= self.heuristica and x < (self.heuristica+1))):
                #print("entro")
                continue
            else:
                #print("asd")
                aleatorio = random.randint(0, self.maximo)
                arreglo2[i] = aleatorio
        #print("sale ", arreglo)
        return arreglo2
    def seleccionPorTorneos(self,cantidad):
        for i in range (0,cantidad):
            nuevoArreglo = self.seleccion(self.arreglo)
            #print(nuevoArreglo)
            #print("self.calculoH ", self.calculoH(nuevoArreglo), " heuristica ", self.heuristica)
            if (self.calculoH(nuevoArreglo) <= self.heuristica):
                self.arreglo = nuevoArreglo
                self.heuristica = self.calculoH(self.arreglo)
    def moverUno(self):
        copia = copy.deepcopy(self.arreglo)
        for i in range(0,len(self.arreglo)):
            if (i == len(self.arreglo)-1):
                copia[0] = self.arreglo[i]
            else:
                copia[i+1] = self.arreglo[i]
        self.arreglo = copia
    def fitnessDiagonal(self,arreglo,individuo):
        h = self.calculoDiagonal(individuo,arreglo)
        for i in range(0, individuo):
            if (abs(arreglo[i] - arreglo[individuo]) == abs(i - individuo)):
                h = h + 1
        return h
    def fitnessHorizontal(self,arreglo,individuo):
        h = self.calculoHorizontal(individuo,arreglo)
        for i in range(0, individuo):
            if (arreglo[individuo] == arreglo[i]):
                h = h + 1
        return h
    def ponerReinas(self,arreglo):
        self.tablero = np.zeros((len(arreglo), len(arreglo)))
        for i in range(0, len(arreglo)):
            self.tablero[arreglo[i]][i] = -1
    # [4,5,6,3,4,5,6,5]
    # [0,5,6,3,4,5,6,5]
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
        for a in range(0, self.maximo + 1):
            for b in range(0, self.maximo + 1):
                if (self.tablero[a][b] == -1):
                    print("\33[31m♕\033[0m", end=' ')
                elif (self.tablero[a][b] == 0 and (a + b) % 2 == 0):
                    print("\033[33m⬛\033[0m", end=' ')
                elif (self.tablero[a][b] == 0 and (a + b) % 2 == 1):
                    print("\033[30m⬜\033[0m", end=' ')
                else:
                    print("%2d" % int(self.tablero[a][b]), end=' ')
            print("")
import numpy as np
import copy
import linkedlist
import math
import time
import random
class tablero:
    # Ej Tablero [0,1,2,3,4,5,6,7]
    def __init__(self, arreglo):
        self.segundos = time.time()
        self.arreglo = arreglo
        self.maximo = len(self.arreglo) - 1
        self.menor = math.factorial(len(arreglo))
        self.heuristica = self.calculoH(self.arreglo)
        # Agregamos las reinas en el tablero
        self.ponerReinas(self.arreglo)
        self.pares = {}
        self.estados = 0
        for i in range(0, len(arreglo)):
            self.pares[i] = linkedlist.LinkedList()

        self.printTablero()
        print("H principal = " , self.calculoH(self.arreglo))
        self.calculoHs()

        #self.printTablero()
    def ponerReinas(self,arreglo):
        self.tablero = np.zeros((len(arreglo), len(arreglo)))
        for i in range(0, len(arreglo)):
            self.tablero[arreglo[i]][i] = -1
    # [4,5,6,3,4,5,6,5]
    # [0,5,6,3,4,5,6,5]
    def generarOtroArreglo(self):
        n = len(self.arreglo)
        valores = {}
        for i in range(0, n):
            aleatorio = random.randint(0, n - 1)
            if (aleatorio in valores.values()):
                while (True):
                    if (aleatorio in valores.values()):
                        aleatorio = random.randint(0, n - 1)
                    else:
                        self.arreglo[i] = aleatorio
                        valores[i] = aleatorio
                        break
            else:
                self.arreglo[i] = aleatorio
                valores[i] = aleatorio
    def calculoHs(self):
        seEncontroUnMenor = False
        anteriori = 0
        anteriorj = 0
        menor2 = self.menor
        copia2 = None
        arregloAnterior = None
        n = 0
        if (self.heuristica == 0):
            print("Se ha llegado a una solución con H = 0")
            self.printTablero()
            return
        while (self.calculoH(self.arreglo)):
            if (n == 2):
                if (arregloAnterior == self.arreglo):
                    break
                n = 0
            for i in range(0,len(self.arreglo)):
                copia = copy.deepcopy(self.arreglo)
                for j in range(0,len(self.arreglo)):
                    if (self.tablero[j][i] != -1):
                        copia[i] = j
                        self.tablero[j][i] = self.calculoH(copia)
                        if (self.tablero[j][i] < self.menor):
                                self.menor = self.tablero[j][i]
                                self.arreglo = copia
                                seEncontroUnMenor = True
                                self.estados = self.estados + 1
                        elif (self.tablero[j][i] < menor2):
                            anteriori = j
                            anteriorj = i
                            menor2 = self.tablero[j][i]
                            copia2 = copy.deepcopy(copia)
                        #print("[",copia[0],",",copia[1],",",copia[2],",",copia[3],",",copia[4],",",copia[5],",",copia[6],",",copia[7],"] =", self.tablero[i][j])
            if (seEncontroUnMenor == False):
                self.tablero[anteriori][anteriorj]
                self.menor = menor2
                self.arreglo = copia2
                self.estados = self.estados + 1


                #print("buscando otro maximo local")
                #print("menor1 = " , self.menor, " menor2 = " , menor2)
                menor2 = math.factorial(len(self.arreglo))
            arregloAnterior = self.arreglo
            seEncontroUnMenor = False
            self.ponerReinas(self.arreglo)
            #self.printTablero()
            n = n + 1
        H = self.calculoH(self.arreglo)
        self.ponerReinas(self.arreglo)
        self.calculoH(self.arreglo)
        if (H > 0):
            print("Se ha llegado a máximo local, H = ",H , "en ", time.time() - self.segundos)
            print("Estados: ", self.estados)
            self.printTablero()
        else:
            print ("Se ha llegado a un tablero solución H = 0", "en ", time.time() - self.segundos)
            print("Estados: ", self.estados)
            self.printTablero()



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
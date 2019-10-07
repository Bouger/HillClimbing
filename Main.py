import random
import AlgoritmosGeneticos
n =8
valores = {}
arreglo = [0,0,0,0,0,0,0,0]
for i in range(0,n):
    aleatorio = random.randint(0, n-1)
    if (aleatorio in valores.values()):
        while (True):
            if (aleatorio in valores.values()):
                aleatorio = random.randint(0, n-1)
            else:
                arreglo[i] = aleatorio
                valores[i] = aleatorio
                break
    else:
        arreglo[i] = aleatorio
        valores[i] = aleatorio
print("Para el arreglo: ",arreglo)
AlgoritmosGeneticos.AlgoritmosGeneticos(arreglo)
# [4,5,6,3,4,5,6,5] debería tener h = 17

'''
Hill Clambing

n = 4
valores = {}
arreglo = [0,0,0,0]
for i in range(0,n):
    aleatorio = random.randint(0, n-1)
    if (aleatorio in valores.values()):
        while (True):
            if (aleatorio in valores.values()):
                aleatorio = random.randint(0, n-1)
            else:
                arreglo[i] = aleatorio
                valores[i] = aleatorio
                break
    else:
        arreglo[i] = aleatorio
        valores[i] = aleatorio
print("Para el arreglo: ",arreglo)
Tablero.tablero(arreglo)
# [4,5,6,3,4,5,6,5] debería tener h = 17'''




'''
prueba = {}

prueba[1] = "asd"
if (1 in prueba):
    print(True)
else:
    print(False)
'''
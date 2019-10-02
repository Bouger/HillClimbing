class LinkedList:
    head = None


class Node:
    value = None
    nextNode = None


def imprimir(L):
    currentNode = L.head
    linea = "["
    while (currentNode != None):
        linea = linea + str(currentNode.value) + ","
        currentNode = currentNode.nextNode


def string(S):
    N = LinkedList()
    l = len(S)
    for i in range(0, l):
        insert(N, S[i], i)
    return N


# Agrega un elemento al comienzo de la lista
def add(lista, element):
    newNode = Node()
    newNode.value = element
    newNode.nextNode = lista.head
    lista.head = newNode


# Busca un elemento de la lista
def search(lista, element):
    aux = lista.head
    resp = None
    cont = 0
    while aux != None:
        if aux.value == element:
            resp = cont
            break
        cont = cont + 1
        aux = aux.nextNode
    return resp

def contains(lista,element):
    currentNode = lista.head
    while (currentNode != None):
        if (currentNode.value == element):
            return True
        currentNode = currentNode.nextNode
    return False
# Inserta un elemento en una posición determinada
def insert(lista, element, position):
    aux = lista.head
    resp = None
    cont = 0
    newNode = Node()
    newNode.value = element
    if position == 0:
        add(lista, element)
        #    newNode.nextNode=lista.head
        #    lista.head=newNode
        resp = position
    else:
        while aux != None:
            if cont == position - 1:
                newNode.nextNode = aux.nextNode
                aux.nextNode = newNode
                resp = position
            cont = cont + 1
            aux = aux.nextNode

    return resp


# Elimina un elemento de la lista
def delete(lista, element):
    aux = lista.head
    cont = 0
    position = search(lista, element)
    if position != None:
        if position == 0:
            lista.head = lista.head.nextNode
        else:
            while aux != None:
                if cont == position - 1:
                    aux.nextNode = aux.nextNode.nextNode
                    break
                cont = cont + 1
                aux = aux.nextNode
    return position


def length(lista):
    aux = lista.head
    cont = 0
    while aux != None:
        cont = cont + 1
        aux = aux.nextNode
    return cont


# Permite acceder a un elemento de la lista en una posición determinada
def access(lista, position):
    aux = lista.head
    resp = None
    cont = 0
    while aux != None:
        if cont == position:
            resp = aux.value
            break
        cont = cont + 1
        aux = aux.nextNode
    return resp


####Acces con Mayúscula para distinguirlo de otros access de binaryTree
# Permite acceder a un elemento de la lista en una posición determinada
def Access(lista, position):
    aux = lista.head
    resp = None
    cont = 0
    while aux != None:
        if cont == position:
            resp = aux.value
            break
        cont = cont + 1
        aux = aux.nextNode
    return resp


# permite cambiar el valor de un elemento de la lista en una posición determinada
def update(lista, element, position):
    aux = lista.head
    resp = None
    cont = 0
    while aux != None:
        if cont == position:
            aux.value = element
            resp = cont
            break
        cont = cont + 1
        aux = aux.nextNode

    return resp


# Función para imprimir lista
def imprimir(lista):
    currentNode = lista.head
    a = "["
    for i in range(0, length(lista)):
        if (currentNode.nextNode != None):
            a = a + str(currentNode.value) + ", "
        else:
            a = a + str(currentNode.value) + "]"
        currentNode = currentNode.nextNode
    print(a)


# Función para invertir el orden de una lista
def inverse(L):
    aux = L.head
    nro_elem = length(L)
    ult_pos = nro_elem - 1

    num_iter = 0
    if nro_elem % 2:
        nro_iter = int(nro_elem / 2)
    else:
        nro_iter = int((nro_elem - 1) / 2)

    for i in range(nro_iter):
        aux2 = aux.value
        aux.value = access(L, ult_pos, )
        update(L, aux2, ult_pos)
        aux = aux.nextNode
        ult_pos = ult_pos - 1
    return L


# Función para ordenar los elementos de una lista de menor a mayor
def ordenar_menor_a_mayor(lista):
    aux = lista.head
    aux1 = lista.head
    cont = 0
    menor = aux1.value
    while aux1 != None:
        if menor > aux1.value:
            menor = aux1.value
        cont = cont + 1
        aux1 = aux1.nextNode
    posic_menor = search(lista, menor)
    update(lista, aux.value, posic_menor)
    update(lista, menor, 0)
    num = length(lista)
    #  print(num)
    if num > 1:
        aux3 = lista.head
        lista.head = lista.head.nextNode
        ordenar_menor_a_mayor(lista)
        lista.head = aux3


# permite cambiar el valor de la posición de menoria de un nodo en una lista a partir de una posición determinada
def update_nextNode(lista, nextNode, position):
    aux = lista.head
    resp = None
    cont = 0
    while aux != None:
        if cont == position:
            aux.nextNode = nextNode
            resp = cont
            break
        cont = cont + 1
        aux = aux.nextNode

    return resp


# Concatenar M a L. Ingresan 2 listas. La segunda lista se agrega a la primera. Devuelve la referencia a la primer lista.
def concatenar(L, M):
    aux = L.head
    dim = length(L)

    while aux.nextNode != None:
        aux = aux.nextNode
    aux.nextNode = M.head
    return L

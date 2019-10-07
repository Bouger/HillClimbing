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


def add(lista, element):
    newNode = Node()
    newNode.value = element
    newNode.nextNode = lista.head
    lista.head = newNode


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


def tamano(lista):
    aux = lista.head
    cont = 0
    while aux != None:
        cont = cont + 1
        aux = aux.nextNode
    return cont


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


def imprimir(lista):
    currentNode = lista.head
    a = "["
    for i in range(0, tamano(lista)):
        if (currentNode.nextNode != None):
            a = a + str(currentNode.value) + ", "
        else:
            a = a + str(currentNode.value) + "]"
        currentNode = currentNode.nextNode
    print(a)


def inverse(L):
    aux = L.head
    nro_elem = tamano(L)
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
    num = tamano(lista)
    #  print(num)
    if num > 1:
        aux3 = lista.head
        lista.head = lista.head.nextNode
        ordenar_menor_a_mayor(lista)
        lista.head = aux3


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



def concatenar(L, M):
    aux = L.head
    dim = tamano(L)

    while aux.nextNode != None:
        aux = aux.nextNode
    aux.nextNode = M.head
    return L
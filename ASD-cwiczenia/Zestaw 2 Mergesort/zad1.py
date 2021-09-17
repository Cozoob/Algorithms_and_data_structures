import random
# Prosze zaimplementowac:
# 1. Scalanie dwóch posortowanych list jednokierunkowych do jednej.
# 2. Algorytm sortowania list jednokierunkowych przez scalanie serii naturalnych.
# 3. Co sie stanie, jesli w powyzszym algorytmie bedziemy łaczyc poprzednio posortowana liste z kolejna,
# zamiast łaczenia dwóch kolejnych list?

class Node():
    def __init__(self, value = None):
        self.value = value
        self.next = None

def printlist(L):
    if L != None:
        print(L.value, end='')
    else:
        print(L)
        return
    L = L.next
    while L != None:
        print(" -->", L.value, end='')
        L = L.next
    print()

def insert(L, elem):
    if L == None:
        return Node(elem)
    pointer = L
    while pointer.next != None:
        pointer = pointer.next
    pointer.next = Node(elem)
    return L

def mergingtwosortedlists(L1, L2):
    newL = Node()
    pointer = newL
    while L1 != None and L2 != None:
        while L1 != None and L1.value < L2.value:
            pointer.next = Node(L1.value)
            pointer = pointer.next
            L1 = L1.next
        while L2 != None and L1 != None and L1.value >= L2.value:
            pointer.next = Node(L2.value)
            pointer = pointer.next
            L2 = L2.next
    if L1 != None:
        pointer.next = L1
    if L2 != None:
        pointer.next = L2

    return newL.next

def cutlist(List):
    Head = List
    Tail = List.next
    while Tail != None and Head.value <= Tail.value:
        Head = Head.next
        Tail = Tail.next

    if Tail == None:
        return Head, Tail

    while Tail.next != None and Tail.value <= Tail.next.value:
        Tail = Tail.next

    return Head, Tail

def mergesortlist(List):

    # cutlist znajduje dwie kolejne serie posortowanych list
    def cutlist(List):
        Head = List
        Tail = List.next
        while Tail != None and Head.value <= Tail.value:
            Head = Head.next
            Tail = Tail.next

        if Tail == None:
            return Head, Tail

        while Tail.next != None and Tail.value <= Tail.next.value:
            Tail = Tail.next

        return Head, Tail

    head, tail = cutlist(List)
    # to oznacza ze lista jest juz posortowana
    if tail == None:
        return List

    newList = Node()
    pointer = newList
    head = head.next
    stop = head
    tail = tail.next

    while List != stop and head != tail:
        if List.value <= head.value:
            pointer.next = Node(List.value)
            List = List.next
            pointer = pointer.next

        if List.value > head.value:
            pointer.next = Node(head.value)
            head = head.next
            pointer = pointer.next

    # ewentualnie zostaly nam elementy w 1 lub 2 serii naturalnych
    while List != stop:
        pointer.next = Node(List.value)
        pointer = pointer.next
        List = List.next

    while head != tail:
        pointer.next = Node(head.value)
        head = head.next
        pointer = pointer.next

    # doczepiamy ogon
    pointer.next = tail
    return mergesortlist(newList.next)







if __name__ == '__main__':
    # print("Pierwsza lista")
    # L = insert(None, 2)
    # for i in range(3, 15):
    #     L = insert(L, i)
    # printlist(L)
    # print("Druga lista")
    # A = insert(None, 1)
    # for j in range(9, 13):
    #     A = insert(A, j)
    # printlist(A)
    # mergedL = mergingtwosortedlists(L, A)
    # print("Zmergowana lista")
    # printlist(mergedL)

    lista = insert(None, 1)
    for _ in range(8):
        lista = insert(lista, random.randint(1, 100))
    print("Randomizowana lista")
    printlist(lista)
    # mergesortlist(lista)
    lol = mergesortlist(lista)
    printlist(lol)
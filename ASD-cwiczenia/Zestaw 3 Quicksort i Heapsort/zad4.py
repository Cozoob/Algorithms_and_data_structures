# Prosze zaproponowac algorytm scalajacy k posortowanych list.
import random

class Node():

    def __init__(self, value = None):
        self.value = value
        self.next = None

def inserttolist(L, elem):
    if L == None:
        return Node(elem)
    pointer = L
    while pointer.next != None:
        pointer = pointer.next
    pointer.next = Node(elem)
    return L

def printlist(L):
    while L.next != None:
        print(L.value, end='')
        print(" --> ", end='')
        L = L.next
    print("|")
    print()

def mergelists(arr):
    # dostaje tablice ze wskaznikami na k list
    # najpierw scalam dwie pierwsze listy i
    # tworze nowa newL
    newL = arr[0]
    for i in range(1, len(arr)):
        # i-ta liste z arr scalam z newL
        L = arr[i]
        pointer = newL
        head = Node()
        tmp = head

        while pointer != None and L != None:
            if pointer.value <= L.value:
                tmp.next = Node(pointer.value)
                pointer = pointer.next
                tmp = tmp.next
            else:
                tmp.next = Node(L.value)
                tmp = tmp.next
                L = L.next
        # teraz ewentualnie dolaczam to co zostalo
        # w liscie L albo newL

        while pointer != None:
            tmp.next = Node(pointer.value)
            tmp = tmp.next
            pointer = pointer.next

        while L != None:
            tmp.next = Node(L.value)
            tmp = tmp.next
            L = L.next

        # i teraz naszym newL jest head.next
        newL = head.next

    return newL



if __name__ == '__main__':

    n = 6
    L1 = inserttolist(None, 2)
    L2 = inserttolist(None, 8)
    L3 = inserttolist(None, 12)
    for i in range(2, n + 2, 2):
        L1 = inserttolist(L1, i)
        L2 = inserttolist(L2, 9 + i)
        L3 = inserttolist(L3, 12 + i)
    printlist(L1)
    printlist(L2)
    printlist(L3)
    arr = [L1, L2, L3]
    newL = mergelists(arr)
    printlist(newL)
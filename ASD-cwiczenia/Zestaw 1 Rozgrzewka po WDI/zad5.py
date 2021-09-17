# Prosze zaimplementowac funkcje odwracajaca liste jednokierunkowa.

class Node():
    def __init__(self, value = None):
        self.value = value
        self.next = None

def insert(L, elem):
    if L == None:
        return Node(elem)
    tmp = L
    while tmp.next != None:
        tmp = tmp.next
    tmp.next = Node(elem)
    return L

def printlist(L):
    if L == None:
        print("None")
    else:
        print(L.value, end='')
        L = L.next
        while L != None:
            print("-->", end='')
            print(L.value, end='')
            L = L.next
        print()

def reverselist(L):

    def insertinfront(L,elem):
        if L == None:
            return Node(elem)
        newL = Node(elem)
        newL.next = L
        return newL

    newL = None
    while L != None:
        newL = insertinfront(newL, L.value)
        L = L.next
    return newL

if __name__ == '__main__':
    L = insert(None, 6)
    L = insert(L, 82)
    L = insert(L, 92)
    L = insert(L, 14)
    L = insert(L, 28)
    printlist(L)
    newL = reverselist(L)
    printlist(newL)
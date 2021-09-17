# Zadanie 2. (sortowanie listy jednokierunkowej) Prosze zaimplementowac algorytm sortowania listy
# jednokierunkowej. W szczególnosci nalezy:
# 1. Zdefiniowac klase w Pythonie realizujaca liste jednokierunkowa.
# 2. Zaimplementowac wstawianie do posortowanej listy.
# 3. Zaimplementowac usuwanie maksimum z listy.
# 4. Zaimplementowac sortowanie przez wstawianie lub sortowanie przez wybieranie na podstawie powyzszych
# funkcji.

class Node():
    def __init__(self, value = None):
        self.value = value
        self.next = None

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

def insert(L, elem):
    if L == None:
        return Node(elem)
    tmp = Node()
    tmp.next = L
    while tmp.next != None and tmp.next.value < elem:
        tmp = tmp.next
    if tmp.next == None:
        tmp.next = Node(elem)
    elif tmp.value == None:
        # wstawiam na sam poczatek listy
        tmp.value = elem
        return tmp
    else:
        end = tmp.next
        tmp.next = Node(elem)
        tmp = tmp.next
        tmp.next = end
    return L

def deletemaximum(L):
    # z nie posortowanej to musze znalezc najpierw element maksymalny
    value = L.value
    pointer = L
    prev_p = Node()
    prev_p.next = pointer
    w = prev_p
    while pointer != None:
        if pointer.value > value:
            value = pointer.value
            w = prev_p
        pointer = pointer.next
        prev_p = prev_p.next
    # znalezlismy najwieksze value wraz z zapisanym wskaznikiem w tuz przed nim
    if w == None:
        # czyli jesli element maksymalny jest na samym poczatku listy to return L.next po prostu
        return L.next
    else:
        # gdzies w srodku lub na koncu
        end = w.next
        end = end.next
        w.next = end
        return L

if __name__ == '__main__':
    L = insert(None, 5)
    L = insert(L, 6)
    L = insert(L, 10)
    L = insert(L, 2)
    printlist(L)
    L = deletemaximum(L)
    printlist(L)
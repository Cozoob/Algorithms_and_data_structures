from random import randint, seed


class Node:
    def __init__(self):
        self.next = None
        self.value = None


def qsort(L):
    start = Node()
    start.next = L

    def rek_qsort(prev_start, end_next):
        # funkcja otrzymuje wskaznik na element przed podzialem i zaraz po aby
        # fragment bylo mozna wpiac do listy
        while prev_start.next != end_next:
            left, right = partition(prev_start, end_next)
            rek_qsort(prev_start, left)
            # bez rekursji ogonowej
            prev_start = right
            left = end_next

    def partition(prev_start, end_next):
        pointer = prev_start.next
        # pointer wskazuje od ktorego momentu chcemy dzielic/sortowac

        # 3 nowe listy
        # wartosci wieksze od pivota
        greater_start = greater = Node()
        # wartosci mnijesze od pivota
        lesser_start = lesser = Node()
        # wartosci rowne pivotowi
        equal_start = equal = Node()

        pivot = pointer.value
        while pointer != end_next:
            if pointer.value < pivot:
                lesser.next = pointer
                lesser = lesser.next
            elif pointer.value > pivot:
                greater.next = pointer
                greater = greater.next
            else:
                equal.next = pointer
                equal = equal.next
            pointer = pointer.next

        # lacze 3 listy w jedna w odpowiedniej kolejnosci
        lesser.next = equal_start.next
        equal.next = greater_start.next

        # lacze nowa liste ze stara lista
        if equal.next == None:
            equal.next = end_next
        else:
            greater.next = end_next
        prev_start.next = lesser_start.next

        return equal_start.next, equal


    rek_qsort(start, None)

    return start.next


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


def printlist(L):
    while L != None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")


# seed(42)

n = 10
T = [randint(1, 10) for i in range(10)]
L = tab2list(T)

print("przed sortowaniem: L =", end=" ")
printlist(L)
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
    print("List jest pusta, a nie powinna!")
    exit(0)

P = L
while P.next != None:
    if P.value > P.next.value:
        print("Błąd sortowania")
        exit(0)
    P = P.next

print("OK")
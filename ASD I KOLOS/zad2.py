# Marcin Kozub

# Jesli lista jest 0-chaotyczna to jestesmy od razu zwrocic liste poniewaz jest juz posortowana
# zas jesli lista jest k-chaotyczna lista dlugosci n gdzie 0 < k < n to sortujemy quicksortem.

# Dla k = O(1) to jest n^2, dla k = O(logn) to jest nlgn, dla k = O(n) to jest nlgn

class Node:
    def __init__(self):
        self.val = None # przechowywana liczba rzeczywista
        self.next = None # odsyłacz do nastepnego elementu

def sortH(p, k):
    if k == 0:
        return p
    else:
        return qsort(p)


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
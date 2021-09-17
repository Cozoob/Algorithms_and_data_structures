# Created by Marcin "Cozoob" Kozub 25.06.2021

# Zadanie 4. Proszę zaproponować algorytm scalający k posortowanych list.

# Czy wystarczy przylaczac (tworzyc nowa liste) dwie listy?
# O(t * k) gdzie t to dlugosc najdluzszej z list.
# Czy da sie szybciej?


class Node():

    def __init__(self, value = None):
        self.value = value
        self.next = None


def print_linked_list(L):
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

def array_to_linked_list(arr):
    n = len(arr)
    head = Node(arr[0])
    w = head
    for i in range(1, n):
        w.next = Node(arr[i])
        w = w.next

    return head

# Dostaje liste headow kazdej listy
def merge1(A):
    k = len(A)

    last_L = A[0]

    for i in range(1, k):
        new_L = Node()
        pointer = new_L
        curr_L = A[i]

        while curr_L != None and last_L != None:
            if curr_L.value <= last_L.value:
                pointer.next = Node(curr_L.value)
                pointer = pointer.next
                curr_L = curr_L.next
            else:
                pointer.next = Node(last_L.value)
                pointer = pointer.next
                last_L = last_L.next

        while curr_L != None:
            pointer.next = Node(curr_L.value)
            pointer = pointer.next
            curr_L = curr_L.next

        while last_L != None:
            pointer.next = Node(last_L.value)
            pointer = pointer.next
            last_L = last_L.next

        last_L = new_L.next

    return last_L


# ok a mozeeee by tak uzyc cos z heapsorta?
# O(t * logk) gdzie t to ilosc wszystkich elementow w listach ( wiec w sumie szybciej niz t * k)
# min_heapify daje mi na 1 miejscu w tablicy najmniejszy element wiec jego biore do nowej listy
# a wskaznik danej listy przesuwam dalej. Jesli L.next is None to ustawiam tam wartosc inf.
# Dzieki temu jak po wykonaniu heapify min na 1 miejscu w tablicy bedzie inf to wiem ze moge
# zwrocic new_L bo wszystkie k list zlaczylem.

def min_heapify(arr, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    k = i
    if left < n and arr[left].value < arr[k].value:
        k = left
    if right < n and arr[right].value < arr[k].value:
        k = right
    if k != i:
        arr[i], arr[k] = arr[k], arr[i]
        min_heapify(arr, n, k)



def merge2(A):
    k = len(A)
    new_L = Node()
    inf = float("inf")
    pointer = new_L

    while True:
        min_heapify(A, k, 0)
        if A[0].value == inf:
            break

        pointer.next = Node(A[0].value)
        pointer = pointer.next
        A[0] = A[0].next
        if A[0] == None:
            A[0] = Node(inf)

    return new_L.next





if __name__ == '__main__':
    L1 = array_to_linked_list([1,3,6,7])
    L2 = array_to_linked_list([2,3,4,5,8])
    L3 = array_to_linked_list([6,9,11,20])
    L4 = array_to_linked_list([10, 14, 15, 19])
    print_linked_list(L1)
    print_linked_list(L2)
    print_linked_list(L3)
    print_linked_list(L4)
    print()
    print_linked_list(merge2([L1, L3, L2, L4]))

    #print_linked_list(merge1([L1, L2, L3, L4]))
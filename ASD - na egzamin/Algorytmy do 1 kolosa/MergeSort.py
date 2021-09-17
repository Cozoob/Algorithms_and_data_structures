# Created by Marcin "Cozoob" Kozub 23.06.2021
# Nie dziala w miejscu / stabilne
# O(nlogn)

# mergesort na tablicy
def MergeSort1(array, left, right):
    if right <= left:
        return

    mid = (right + left) // 2
    MergeSort1(array, left, mid)
    MergeSort1(array, mid + 1, right)

    # left_size rozmiar lewej tablicy
    left_size = mid - left + 1
    # right_size rozmiar prawej tablicy
    right_size = right - mid

    L = [0 for _ in range(left_size)]
    R = [0 for _ in range(right_size)]

    for i in range(left_size):
        L[i] = array[left + i]
    for i in range(right_size):
        R[i] = array[mid + 1 + i]


    i = j = 0

    for k in range(left, right + 1):
        if i >= left_size:
            # tablica L sie skonczyla
            array[k] = R[j]
            j += 1
        elif j >= right_size:
            # tablica R sie skonczyla
            array[k] = L[i]
            i += 1
        elif L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1


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



# mergesort na liscie jednokierunkowej
def merge_two_linked_lists(L1, L2):

    newL = Node()
    pointer = newL
    while L1 != None and L2 != None:

        while L1 != None and L1.value <= L2.value:
            pointer.next = Node(L1.value)
            pointer = pointer.next
            L1 = L1.next

        while L2 != None and L1 != None and L1.value > L2.value:
            pointer.next = Node(L2.value)
            pointer = pointer.next
            L2 = L2.next

    if L1 != None:
        pointer.next = L1
    if L2 != None:
        pointer.next = L2

    return newL.next

def cut_linked_list(L):
    if L == None:
        return None

    head = L
    tail = L.next

    while tail != None and head.value <= tail.value:
        head = head.next
        tail = tail.next

    if tail == None:
        return head, tail

    while tail.next != None and tail.value <= tail.next.value:
        tail = tail.next

    return head, tail


def MergeSort2(L):

    head, tail = cut_linked_list(L)
    if tail == None:
        return L

    newL = Node()
    pointer = newL
    head = head.next
    stop = head
    tail = tail.next

    while L != stop and head != tail:
        if L.value <= head.value:
            pointer.next = Node(L.value)
            L = L.next
            pointer = pointer.next

        if L.value > head.value:
            pointer.next = Node(head.value)
            head = head.next
            pointer = pointer.next

    while L != stop:
        pointer.next = Node(L.value)
        pointer = pointer.next
        L = L.next

    while head != tail:
        pointer.next = Node(head.value)
        head = head.next
        pointer = pointer.next

    pointer.next = tail

    return MergeSort2(newL.next)




if __name__ == '__main__':
    T = [-3, 2, 1, 90, 4, 57, 1, 8]
    L = array_to_linked_list(T)
    MergeSort1(T, 0, len(T) - 1)
    print(T)
    print()

    print_linked_list(L)
    L = MergeSort2(L)
    print_linked_list(L)
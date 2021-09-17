# Created by Marcin "Cozoob" Kozub 24.06.2021
# O(nlogn)
# niestabilne

# QuickSort na tablicy
def partition1(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]

    return i


def QuickSort1(arr, left, right):
    while left < right:
        mid = partition1(arr, left, right)
        QuickSort1(arr, left, mid - 1)
        left = mid + 1

# QuickSort na liscie jednokierunkowej
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

def partition2(head, tail):
    if head == tail or head == None or tail == None:
        return head

    pivot_prev = head
    curr = head
    pivot = tail.value

    while head != tail:
        if head.value < pivot:

            pivot_prev = curr
            temp = curr.value
            curr.value = head.value
            head.value = temp
            curr = curr.next
        head = head.next

    temp = curr.value
    curr.value = pivot
    tail.value = temp

    return pivot_prev

def find_tail_in_linked_list(L):
    if L == None:
        return None

    while L.next != None:
        L = L.next

    return L


def QuickSort2(head, tail):

    if head == None or head == tail or head == tail.next:
        return head

    pivot_prev = partition2(head, tail)
    QuickSort2(head, pivot_prev)

    if pivot_prev != None and pivot_prev == head:
        QuickSort2(pivot_prev.next, tail)

    elif pivot_prev != None and pivot_prev.next != None:
        QuickSort2(pivot_prev.next.next, tail)

    return head

if __name__ == '__main__':
    T = [5,1,23,8, 3, 0, -1, -10]
    L = array_to_linked_list(T)
    QuickSort1(T, 0, len(T) - 1)
    print(T)
    print_linked_list(L)
    L = QuickSort2(L, find_tail_in_linked_list(L))
    print_linked_list(L)
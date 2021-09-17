# Created by Marcin "Cozoob" Kozub 24.06.2021
# O(nlogn)
# niestabilne

# W sumie tylko min_heapify i max_heapify sie roznia
# znakami nierownosc i tyle tak to poza innymi nazwami
# funkcji to min_buildheap =~= max_buildheap i to samo
# z heapsort

# TYPU MAX
# heapify do naprawiania kopca O(logn)
def max_heapify(arr, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    k = i
    if left < n and arr[left] > arr[k]:
        k = left
    if right < n and arr[right] > arr[k]:
        k = right
    if k != i:
        arr[i], arr[k] = arr[k], arr[i]
        max_heapify(arr, n, k)


def max_buildheap(arr):
    n = len(arr)
    parent = (n - 2) // 2
    for i in range(parent, -1, -1):
        max_heapify(arr, n, i)

def max_heapsort(arr):
    n = len(arr)
    max_buildheap(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, i, 0)

# TYPU MIN
def min_heapify(arr, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    k = i
    if left < n and arr[left] < arr[k]:
        k = left
    if right < n and arr[right] < arr[k]:
        k = right
    if k != i:
        arr[i], arr[k] = arr[k], arr[i]
        min_heapify(arr, n, k)


def min_buildheap(arr):
    n = len(arr)
    parent = (n - 2) // 2
    for i in range(parent, -1, -1):
        min_heapify(arr, n, i)

def min_heapsort(arr):
    n = len(arr)
    min_buildheap(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        min_heapify(arr, i, 0)

if __name__ == '__main__':
    T = [0, 3, 1, 4,6, 3,7 ,32, 8,5, 623, -1]
    min_heapify(T, len(T), 0)
    print(T)
    max_heapsort(T)
    print(T)
    min_heapsort(T)
    print(T)


    A = [10, 1, 2, 6]
    min_buildheap(A)
    print(A)


    min_heapify(A, len(A), 0)
    # A[0] = float("inf")
    # min_heapify(A, len(A), 0)
    print(A)
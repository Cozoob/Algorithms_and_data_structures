# Prosze przedstawic W jaki sposób zrealizowac strukture danych, która pozwala wykonywac
# operacje:
# 1. Insert
# 2. RemoveMin
# 3. RemoveMax
# tak, zeby wszystkie operacje działały w czasie O(log n).



# wiec mozna wykorzystac polaczone kopce typu max i min

def maxheapify(arr, i, heapsize):
    l = 2 * i + 1
    r = 2 * i + 2
    if l <= heapsize and arr[l] >= arr[i]:
        largest = l
    else:
        largest = i
    if r <= heapsize and arr[r] >= arr[largest]:
        largest = r
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        maxheapify(arr, largest, heapsize)

def minheapify(arr, i, heapsize):
    l = 2 * i + 1
    r = 2 * i + 2
    if l <= heapsize and arr[l] <= arr[i]:
        lowest = l
    else:
        lowest = i
    if r <= heapsize and arr[r] <= arr[lowest]:
        lowest = r
    if lowest != i:
        arr[lowest], arr[i] = arr[i], arr[lowest]
        minheapify(arr, lowest, heapsize)

def buildminheap(arr):
    heapsize = len(arr) - 1
    for i in range(heapsize // 2, -1, -1):
        minheapify(arr,i,heapsize)

def buildmaxheap(arr):
    heapsize = len(arr) - 1
    for i in range(heapsize//2, -1, -1):
        maxheapify(arr,i,heapsize)

def RemoveMin(arr):
    buildminheap(arr)
    # teraz tworze tablice mniejsza
    if len(arr) == 1: return None
    tab = [0 for _ in range(len(arr) - 1)]
    for i in range(1,len(arr)):
        tab[i - 1] = arr[i]
    return tab

def RemoveMax(arr):
    buildmaxheap(arr)
    if len(arr) == 1: return None
    tab = [0 for _ in range(len(arr) - 1)]
    for i in range(1, len(arr)):
        tab[i - 1] = arr[i]
    return tab


if __name__ == '__main__':
    T = [2,3,7,1,8,15,12,0]
    print(T)
    T = RemoveMin(T)
    print(T)
    T = RemoveMax(T)
    print(T)
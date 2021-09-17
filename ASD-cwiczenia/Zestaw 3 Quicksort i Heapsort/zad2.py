# Prosze zaimplementowac funkcje wstawiajaca dowolny element do kopca binarnego.

def heapify(arr, i, heapsize):
    l = 2 * i + 1
    r = 2 * i + 2
    if l <= heapsize and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r <= heapsize and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, heapsize)

def buildheap(arr):
    heapsize = len(arr) - 1
    for i in range(heapsize // 2, -1, -1):
        heapify(arr, i, heapsize)

def inserttoheap(arr, elem):
    # pewnie ten elem jest juz w tablicy tylko go do kopca wsadzamy
    # ale ja chce dodawac elem tez do tablicy
    newtab = [0 for _ in range(len(arr) + 1)]
    for i in range(len(arr)):
        newtab[i] = arr[i]
    newtab[len(newtab) - 1] = elem
    buildheap(newtab)
    return newtab

if __name__ == '__main__':
    T = [2,1,3]
    print(T)
    buildheap(T)
    print(T)
    print(inserttoheap(T, 4))

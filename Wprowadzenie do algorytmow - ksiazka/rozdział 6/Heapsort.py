# sortowanie przez kopcowanie O(nlgn)

# maxheapify sluzy do utrzymywania wlasnosci kopca typu max
def maxheapify(array, i, heapsize):
    # heapsize mowi jak duzy jest dany kopiec (wcale nie musi byc zbudowany ze wszystkich elementow tablicy)
    l = 2 * i + 1
    r = 2 * i + 2
    # lewe i prawe dziecko
    if l <= heapsize and array[l] > array[i]:
        largest = l
    else:
        largest = i
    if r <= heapsize and array[r] > array[largest]:
        largest = r
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        maxheapify(array, largest, heapsize)

# to samo co maxheapify ale kopiec typu min
def minheapify(array, i, heapsize):
    l = 2 * i + 1
    r = 2 * i + 2
    if l <= heapsize and array[l] < array[i]:
        lowest = l
    else:
        lowest = i
    if r <= heapsize and array[r] < array[lowest]:
        lowest = r
    if lowest != i:
        array[i], array[lowest] = array[lowest], array[i]
        minheapify(array, lowest, heapsize)

# budowanie kopca typu max
def buildmaxheap(array):
    heapsize = len(array) - 1
    for i in range(heapsize//2, -1, -1):
        maxheapify(array, i, heapsize)

# budowanie kopca typu min
def buildminheap(array):
    heapsize = len(array) - 1
    for i in range(heapsize//2, -1, -1):
        minheapify(array, i, heapsize)

# heapsort do sortowania rosnąco
def maxheapsort(array):
    buildmaxheap(array)
    heapsize = len(array) - 1
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapsize -= 1
        maxheapify(array, 0, heapsize)

def minheapsort(array):
    buildminheap(array)
    heapsize = len(array) - 1
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapsize -= 1
        minheapify(array, 0, heapsize)

if __name__ == '__main__':
    T1 = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    T2 = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    maxheapsort(T1)
    print(T1)
    minheapsort(T2)
    print(T2)
# Dana jest tablica liczb rzeczywistych wielkosci n reprezentujaca
# kopiec minimum (array-based heap). Majac dana liczbe rzeczywista
# x sprawdz, czy k-ty najmniejszy element jest wiekszy lub rowny x.

# moj pomysl O(klogn)
# k razy budujemy kopiec minimum i zdejmujemy z samej gory ten
# najmniejszy element i sprawdzamy na koncu czy jest wieksza lub rowny x

def buildminheap(arr, left, right):
    heapsize = right - left
    for i in range(heapsize // 2, -1, -1):
        minheapify(arr,i,heapsize)

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

def function(A, k, x):
    i = 0
    while k != 1:
        buildminheap(A, i, len(A) - 1)
        i += 1
        k -= 1
    if A[i] >= x:
        return A[i], True
    else:
        return A[i], False

if __name__ == '__main__':
    A = [4,6,78,2,54,7,8,2,45,7]
    print(function(A, 4, 7))
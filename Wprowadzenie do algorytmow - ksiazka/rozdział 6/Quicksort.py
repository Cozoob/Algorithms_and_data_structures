# sortowanie szybkie (pesymistycznie n^2 ALE bardzo rzadkie; zazwyczaj nlgn)

def quicksort(array, left, right):
    if left < right:
        mid = partition(array, left, right)
        quicksort(array, left, mid - 1)
        quicksort(array, mid + 1, right)

def partition(array, left, right):
    elem = array[right]
    i = left
    for j in range(left, right):
        if array[j] <= elem:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[right] = array[right], array[i]
    return i

if __name__ == '__main__':
    T1 = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    quicksort(T1, 0, len(T1) - 1)
    print(T1)
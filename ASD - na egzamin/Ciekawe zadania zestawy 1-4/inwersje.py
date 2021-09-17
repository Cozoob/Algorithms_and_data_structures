# Created by Marcin "Cozoob" Kozub 24.06.2021
# Proszę zaproponować i zaimplementować algorytm, który mając na wejściu tablicę A zwraca
# liczbę jej inwersji (t.j., liczbę par indeksów i < j takich, że A[i] > A[j].)
from random import randint
from random import seed
# bruteforce O(n^2)
def bruteforce(A):
    n = len(A)
    counter = 0
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] - A[j] > 0:
                counter += 1

    return counter

# z wykorzystaniem mergesorta
# O(nlogn)

def MergeSort(A, B, left, right):
    counter = 0

    if left >= right:
        return 0

    mid = left + (right - left) // 2

    counter += MergeSort(A, B, left, mid)
    counter += MergeSort(A, B, mid + 1, right)

    counter += merge(A, B, left, mid, right)

    return counter

def merge(A, B, left, mid, right):
    i = left
    j = mid + 1
    k = left
    counter = 0

    while i <= mid and j <= right:
        if A[i] <= A[j]:
            B[k] = A[i]
            k += 1
            i += 1
        else:
            B[k] = A[j]
            counter += (mid - i + 1)
            k += 1
            j += 1

    while i <= mid:
        B[k] = A[i]
        k += 1
        i += 1

    while j <= right:
        B[k] = A[j]
        k += 1
        j += 1

    for a in range(left, right + 1):
        A[a] = B[a]

    return counter


if __name__ == '__main__':
    seed(42)
    T = [randint(0,50) for _ in range(10)]
    print(T)
    print(bruteforce(T))
    print(MergeSort(T, [0 for _ in range(len(T))], 0, len(T) - 1))

# (Partition Hoare’a) Prosze zaimplementowac funkcje partition z algorytmu QuickSort
# według pomysłu Hoare’a (tj. mamy dwa indeksy, i oraz j, wedrujace z obu konców tablicy w strone srodka
# i zamieniamy elementy tablicy pod nimi jesli mniejszy indeks wskazuje na wartosc wieksza od piwota, a
# wiekszy na mniejsza.
import random

def quicksort(A, left, right):
    while left < right:
        mid = partition(A, left, right)
        if mid - left < right - mid:
            quicksort(A, left, mid - 1)
            left = mid + 1
        else:
            quicksort(A, mid + 1, right)
            right = mid - 1

def partition(A, left, right):
    elem = A[right]
    i = left
    j = right - 1
    while i <= j:
        while i <= j and A[i] <= elem:
            i += 1
        while i <= j and A[j] > elem:
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
    A[i], A[right] = A[right], A[i]

    return i

if __name__ == '__main__':
    n = 11
    T = [random.randint(0, 20) for _ in range(n)]
    print(T)
    quicksort(T, 0, len(T) - 1)
    print(T)
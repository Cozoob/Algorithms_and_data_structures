# Prosze zaimplementowac algorytm QuickSort do sortowania n elementowej tablicy tak, zeby
# zawsze uzywał najwyzej O(log n) dodatkowej pamieci na stosie, niezaleznie od jakosci podziałów w funkcji
# partition.
import random

def Quicksort(A, left, right):
    while left < right:
        mid = partition(A, left, right)
        if mid - left < right - mid:
            Quicksort(A, left, mid - 1)
            left = mid + 1
        else:
            Quicksort(A, mid + 1, right)
            right = mid - 1

def partition(A, left, right):
    elem = A[right]
    i = left
    for j in range(left, right):
        if A[j] <= elem:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[right] = A[right], A[i]
    return i

if __name__ == '__main__':
    n = 11
    T = [random.randint(0, 20) for _ in range(n)]
    print(T)
    Quicksort(T, 0, len(T) - 1)
    print(T)
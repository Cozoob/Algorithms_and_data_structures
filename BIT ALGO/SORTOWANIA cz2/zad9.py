# Dane sa trzy zbiory reprezentowane przez tablice A, B i C. Napisz algorytm, ktory powie,
# czy istnieje taka trójka a, b, c z odpowiednio A, B i C, że a + b = c. Nie wolno
# korzystac ze slownikow.
# (Dokladnie to samo dzialanie co w zad 4)

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
    for j in range(left, right):
        if A[j] <= elem:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[right] = A[right], A[i]
    return i

def bin_search(A, left, right, target):
    if left <= right:
        mid = (left + right) // 2
        if A[mid] == target:
            return True
        elif A[mid] > target:
            bin_search(A, left, mid - 1, target)
        else:
            bin_search(A, mid + 1, right, target)

    return False

# Pomysl O(n^2) najpierw posortowac nlgn a pozniej
# dwoma indeksami z poczatku i konca isc np i na poczatku tablicy A
# j na koncu tablicy B i jesli A[i] + B[j] > x to j-- zas jesli
# A[i] + B[j] < x to i ++

def findthesum(A, B, C):
    quicksort(A, 0, len(A) - 1)
    quicksort(B, 0, len(B) - 1)
    for b in range(len(C)):
        i = 0
        j = len(B) - 1
        while i < len(A) and j > -1:
            if A[i] + B[j] == C[b]:
                return True, i, j, b
            elif A[i] + B[j] > C[b]:
                j -= 1
            else:
                i += 1

    return False

if __name__ == '__main__':
    n = 5
    A = [random.randint(0,20) for _ in range(n)]
    B = [random.randint(0, 20) for _ in range(n)]
    C = [random.randint(0, 20) for _ in range(n)]
    quicksort(A, 0, len(A) - 1)
    quicksort(B, 0, len(B) - 1)
    print(A)
    print(B)
    print(C)
    print(findthesum(A,B,C))
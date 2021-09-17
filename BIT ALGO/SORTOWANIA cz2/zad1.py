# Dane są dwa zbiory liczb, reprezentowane jako tablice rozmiarow m i n,
# gdzie m jest znacznie mniejsze od n. Zaproponuj algorytm, ktory sprawdzi,
# czy zbiory sa rozlaczne.

# sortujemy quicksortem wieksza tablice i wyszukujemy binarnie
# czy jakis element z mniejszej tablicy wystepuje w wiekszej
# zatem:
# zlozonosc sortowania: O(nlogn)
# zlozonosc wyszukiwania: O(mlogn)
# ostatecznie algorytmu: O(nlogn)
import random

def quicksort(A, left, right):
    while left < right:
        mid = partition(A, left, right)
        if mid - left < right - mid:
            quicksort(A,left, mid - 1)
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
            return bin_search(A, left, mid - 1, target)
        else:
            return bin_search(A, mid + 1, right, target)

    return False

def function(m, n):
    # tablica m znacznie mniejsza od n !!!
    quicksort(n, 0, len(n) - 1)
    for elem in m:
        if bin_search(n, 0, len(n) - 1, elem):
            return "Zbiory nie sa rozlaczne"

    return "Zbiory sa rozlaczne"



if __name__ == '__main__':
    m = 5
    n = 30

    M = [random.randint(0,20) for _ in range(m)]
    N = [random.randint(0,20) for _ in range(n)]
    print(M)
    print(N)
    print(function(M,N))
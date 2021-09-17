# (szukanie sumy) Dana jest posortowana tablica A[1...n] oraz liczba x. Prosze napisac program,
# który stwierdza czy istnieja indeksy i oraz j takie, ze A[i] + A[j] = x.
import random

def function(A, x):

    # left/right zakres indeksow w A w ktorym szukamy num
    def binary_search(A, left, right, num):
        # sprawdzamy czy zakres nie jest pusty
        if left <= right:
            # dzielimy liste A na dwie listy
            mid = (left + right) // 2
            if A[mid] == num:
                # znalezlismy nasza szukana liczbe
                return True
            elif A[mid] > num:
                # nasza szukana jest mniejsza wiec
                # sprawdzamy lewa czesc tablicy
                return binary_search(A, left, mid - 1, num)
            else:
                # nasza szukana jest wieksza wiec
                # sprawdzamy prawa czesc tablicy
                return binary_search(A, mid + 1, right, num)
        return False

    # szukam za pomoca petli for pierwszej mozliwej liczby A[i]
    # a pozniej binarnie liczby num = A[j] = x - A[i]
    for i in range(len(A)):
        num = x - A[i]
        if binary_search(A, 0, len(A) - 1, num):
            return True

    # jesli nie znalezlismy zwracam False
    return False

def quicksort(A, left, right):
    if left < right:
        mid = partition(A, left, right)
        quicksort(A, left, mid - 1)
        quicksort(A, mid + 1, right)

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
    n = 10
    # T = [random.randint(0, 100) for _ in range(n)]
    T=[8, 30, 36, 38, 39, 76, 79, 81, 85, 96]
    quicksort(T, 0, n - 1)
    print(T)
    print(function(T, 66))
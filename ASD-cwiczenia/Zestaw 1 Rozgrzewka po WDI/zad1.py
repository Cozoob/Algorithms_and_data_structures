# Zadanie 1. Prosze zaimplementowac jeden ze standardowych algorytmów sortowania tablicy działajacy w
# czasie O(n2) (np. sortowanie babelkowe, sortowanie przez wstawianie, sortowanie przez wybieranie).

# sortowanie babelkowa
def bubble_sort(A):
    for i in range(len(A) - 2):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j-1], A[j]

# sortowanie przez wstawianie
def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key

# sortowanie przez wybieranie
def selection_sort(A):
    for i in range(len(A) - 1):
        elem = A[i]
        for j in range(i + 1, len(A)):
            elem = min(elem, A[j])
        for k in range(i, len(A)):
            if elem == A[k]:
                break
        A[k] = A[i]
        A[i] = elem

if __name__ == '__main__':
    A = [5, 2, 4, 6, 1, 3]
    B = [5, 2, 4, 6, 1, 3]
    C = [5, 2, 4, 6, 1, 3]
    print(A)
    bubble_sort(A)
    print(A)
    insertion_sort(B)
    print(B)
    selection_sort(C)
    print(C)
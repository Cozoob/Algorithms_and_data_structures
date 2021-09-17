# Prosze zaimplementowac algorytm QuickSort bez uzycia rekurencji (ale mozna wykorzystac
# własny stos).

def partition(A, left, right):
    elem = A[right]
    i = left
    for j in range(left, right):
        if A[j] <= elem:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[i], A[right] = A[right], A[i]
    return i

def iterative_quicksort(A):
    S = []
    left = 0
    right = len(A) - 1
    S.append((left, right))
    while len(S) > 0:
        (left, right) = S.pop()
        if left < right:
            mid = partition(A, left, right)
            if mid - left < right - mid:
                S.append((left, mid - 1))
                S.append((mid + 1, right))
            else:
                S.append((mid + 1, right))
                S.append((left, mid - 1))


if __name__ == '__main__':
    T = [0, 3, 4, 5, 2]
    iterative_quicksort(T)
    print(T)

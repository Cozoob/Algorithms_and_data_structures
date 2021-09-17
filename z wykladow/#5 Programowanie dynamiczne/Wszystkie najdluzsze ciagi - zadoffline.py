# Marcin Kozub

def bin_search(A, T, start, end, target):
    mid = (start + end) // 2
    if A[T[mid]] < A[target] and A[target] <= A[T[mid + 1]]:
        return mid + 1
    elif A[T[mid]] < A[target]:
        start = mid + 1
        return bin_search(A, T, start, end, target)
    else:
        end = mid - 1
        return bin_search(A, T, start, end, target)


def getLIS(A):
    results =[[-1 for _ in range(len(A))] for _ in range(len(A))]
    T = [-1 for _ in range(len(A))]
    R = [-1 for _ in range(len(A))]
    length = 0
    T[0] = 0
    # operuje caly czas w taki sposob ze w talicy T mam indeksy
    # elementow z tablicy A ze wartosci tych elementow sa posortowane
    for i in range(1, len(A)):
        # A[i] powieksza obecny najdluzszy podciag
        if A[i] > A[T[length]]:
            R[i] = T[length]
            length += 1
            T[length] = i
        # zmieniamy pierwszy element w podciagu
        elif A[i] < A[T[0]]:
            T[0] = i
        else:
        # zmieniam ktorys elemen w podciagu w srodku
            idx = bin_search(A, T, 0, length, i)
            T[idx] = i
            R[idx] = T[idx - 1]

    return length + 1



def printLIS(A ,T):
    k = 0
    i = T[k]
    while i != -1:
        print(A[i], end=' < ')
        k += 1
        i = T[k]
    print()


if __name__ == '__main__':
    A = [2,1,4,3]
    B = [3,4,-1,5,8,2,3,12,7,9,10]
    print(getLIS(B))
# Created by Marcin "Cozoob" Kozub 24.06.2021
#
# Zadanie 6 (największy przedział). Dany jest ciąg przedziałów domkniętych [a1, b1], . . . ,[an, bn]. Proszę
# zapropnować algorytm, który znajduje taki przedział [at, bt], w którym w całości zawiera się jak najwięcej
# innych przedziałów.

# mamy przdzial [a,b]
# Najpierw sortuje po a
# obliczam f dla kazdego przedzialu i dolaczam informacje do tablicy
# f(x) - liczba przedzialow ktore zaczynaja sie na pozycji
# x lub wczesniej
# sortuje po b
# g(x) - liczba przedzialow ktore koncza sie na pozycji
# x lub wczesniej
# obliczamy g(b) - f(a) na biezaco i zapisujemy w tablicy

# wynik to taki [a,b], że jest max(g(b) - f(a))

# O(nlogn)
def find_the_biggest(A):
    n = len(A)
    QuickSort1(A, 0, len(A) - 1, 0)
    i = 0
    while i < n:
        c = 0
        last = i
        j = i
        while j + 1 < n and A[j + 1][0] == A[j][0]:
            j += 1
            c += 1


        A[i].append(last + c + 1)
        i += 1
        while i <= j:
            A[i].append(last + c + 1)
            i += 1


    print(A)
    QuickSort1(A, 0, len(A) - 1, 1)
    i = 0
    while i < n:
        c = 0
        last = i
        j = i
        while j + 1 < n and A[j + 1][0] == A[j][0]:
            j += 1
            c += 1

        A[i].append(last + c)
        i += 1
        while i <= j:
            A[i].append(last + c + 1)
            i += 1

    best = -1
    answer = None
    print(A)
    for i in range(n):
        if A[i][3] - A[i][2] > best:
            best = A[i][3] - A[i][2]
            answer = A[i][0], A[i][1]

    return answer


def partition1(arr, left, right, pos):
    pivot = arr[right][pos]
    i = left
    for j in range(left, right):
        if arr[j][pos] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]

    return i


def QuickSort1(arr, left, right, pos):
    while left < right:
        mid = partition1(arr, left, right, pos)
        QuickSort1(arr, left, mid - 1, pos)
        left = mid + 1

if __name__ == '__main__':

    T = [[1,2],[1,3],[2,8],[3,4],[4,7],[3,5],[2,9]]
    print(find_the_biggest(T))
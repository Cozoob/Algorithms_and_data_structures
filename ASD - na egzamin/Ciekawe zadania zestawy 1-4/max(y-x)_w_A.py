# Created by Marcin "Cozoob" Kozub 25.06.2021
# Zadanie 6. Dana jest tablica A zawierająca n parami różnych liczb. Proszę zaproponować algorytm, który
# znajduje takie dwie liczby x i y z A, że y −x jest jak największa oraz w tablicy nie ma żadnej liczby z takiej,
# że x < y < z (innymi słowy, po posortowaniu tablicy A rosnąco wynikiem byłyby liczby A[i] oraz A[i+1] dla
# których A[i + 1] − A[i] jest największe).

# Niefortunnie napisane chyba chodzi o to ze w posortowanej A[last] - A[last - 1] byloby wynikiem...
# Czyli stosuje dwa razy heapify max wyciagajac dwa najwieksze liczby z tablicy A i juz?

def max_heapify(arr, n, i):
    left = i * 2 + 1
    right = i * 2 + 2
    k = i
    if 0 <= left < n and arr[left] > arr[k]:
        k = left
    if 0 <= right < n and arr[right] > arr[k]:
        k = right
    if k != i:
        arr[i], arr[k] = arr[k], arr[i]
        max_heapify(arr, n, k)

def strange_alg(A):
    n = len(A)
    last = float("inf")
    while True:
        max_heapify(A, n, 0)
        if last == A[0]:
            break
        last = A[0]

    print(A)
    res = A[0]
    print(res)
    A[0] = - float("inf")
    last = A[0]

    while True:
        max_heapify(A, n, 0)
        if last == A[0]:
            break
        last = A[0]

    res -= A[0]
    return res

if __name__ == '__main__':
    A = [0, 3, -1, 4, 6, 3, 7, 32, 8, 5, 623, 1]
    print(strange_alg(A))
# Created by Marcin "Cozoob" Kozub 24.06.2021
# Countsort stosujemy gdy wiemy ze najwieksza liczba
# z danych wejciowych nie jest duza i wszystkie
# liczby sa naturalne.

# stabilne
# O(n + k), gdzie n to liczba elementow w tablicy zac k to
# najwieksza liczba z tej tablicy

def countsort(arr):
    n = len(arr)
    largest = max(arr)
    C = [0 for _ in range(largest + 1)]
    B = [0 for _ in range(n)]

    for i in range(n):
        C[arr[i]] += 1

    for i in range(1, largest + 1):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        C[arr[i]] -= 1
        B[C[arr[i]]] = arr[i]

    for i in range(n):
        arr[i] = B[i]



if __name__ == '__main__':
    T = [1, 3, 2, 5, 4, 0, 2, 1, 3, 7, 4, 2, 0]
    countsort(T)
    print(T)
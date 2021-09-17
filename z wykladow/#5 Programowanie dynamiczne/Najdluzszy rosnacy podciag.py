# Created by Marcin "Cozoob" Kozub at 10.04.2021 19:27

# O(n^2)
def LIS(A):
    n = len(A)
    F = [1 for _ in range(n)]
    P = [-1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[i] < F[j] + 1:
                F[i] = F[j] + 1
                # zapisujemy informacje o rodzicu (indeks)
                P[i] = j

    return max(F), F, P

# (prof. P. Faliszewski nazwal to printLIS ale wcale
# longest nie musi wypisac; wypisze kazdy rosnacy podciag
# zaczynajacy sie pod indeksem i)
def printIS(A, P, i):
    if P[i] >= 0:
        printIS(A, P, P[i])
    print(A[i], end=' ')

if __name__ == '__main__':
    arr = [3, 1, 5, 7, 2, 4, 9, 3, 17, 3]
    longest, F, P = LIS(arr)
    print(longest)
    for i in range(len(arr)):
        if F[i] == longest:
            printIS(arr, P, i)
            break
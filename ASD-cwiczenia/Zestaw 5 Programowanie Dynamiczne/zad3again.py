# Created by Marcin "Cozoob" Kozub 15.05.2021
# Zadanie 3.1 (najdłuższy wspólny podciąg) Mamy dane dwie tablice, A[n] i B[n]. Należy znaleźć
# długość ich najdłuższego wspólnego podciągu. (Klasyczny algorytm dynamiczny O(n^2)).

# f(i, j) - dlugosc najdluzszego wspolnego podciagu rosnacego konczacego sie na A[i] = B[j]
# f(i, j) = 1 + max( f(k, l) : k < i and l < j and A[k] = B[l] and A[k] < A[i] and B[l] < B[j] )
# wynik: max( f(n,j) )

# O(n^2)
# Longest Common Increasing Subsequence of A and B
def LCIS1(A, B):
    # A oraz B maja ta sama dlugosc n
    n = len(A)
    C = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                # znalezlismy koleny elemeny LCIS
                C[i][j] = C[i - 1][j - 1] + 1
            else:
                C[i][j] = max(C[i - 1][j - 1], C[i][j - 1])

    result = 0
    for i in range(n + 1):
        if result < C[i][n]:
            result = C[i][n]

    return result

if __name__ == '__main__':
    # 3 bo 1-2-3
    A = [1, 2, 3, 4]
    B = [3, 1, 2, 3]
    print(LCIS1(A, B))
    # 1 bo 1
    A = [1, 1, 1, 1]
    B = [1, 2, 3, 4]
    print(LCIS1(A ,B))
    # 2 bo 5-3
    A = [10, 5, 24, 3]
    B = [5, 8, 9, 3]
    print(LCIS1(A, B))
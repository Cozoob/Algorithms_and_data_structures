# Created by Marcin "Cozoob" Kozub at 23.04.2021 21:30

# Dostajemy tablicę (M x N) wypełnioną wartościami(kosztem wejścia).
# Mamy znaleźć minimalny koszt potrzebny do dostania się z pozycji [0][0] do [M-1][N-1]
#
#
# Wprowadzimy na początek pewne ułatwienia:
# 1. Możemy poruszać się tylko w bok i w dół
# 2. Wszystkie koszty są dodatnie

# f(i, j) - minimalny koszt potrzebny do dostania sie z pozycji 0,0 do i,j
# f(i, j) = min( f(i - 1, j) + A[i][j], f(i, j - 1) + A[i][j]) = min( f(i - 1, j), f(i, j - 1)) + A[i][j]

def cost(A):
    n = len(A[0])
    m = len(A)
    # tworze pomocnicza tablice P ktora bedzie przechowywac podproblemy
    P = [[0 for _ in range(n)] for _ in range(m)]
    # wypelniam wartosci poczatkowe
    P[0][0] = A[0][0]
    for i in range(1, n):
        P[0][i] = P[0][i - 1] + A[0][i]

    for i in range(1, m):
        P[i][0] = P[i - 1][0] + A[i][0]


    for i in range(1, m):
        for j in range(1, n):
            P[i][j] = min(P[i - 1][j], P[i][j - 1]) + A[i][j]

    # odpowiedz znajduje sie na koncu tablicy
    return P[m - 1][n - 1]

if __name__ == '__main__':
    A = [[3, 4, 5, 2, 1], [1, 2, 13, 7, 8], [3, 1, 4, 6, 5], [2, 8, 11, 10, 3], [3, 5, 1, 6, 2]]
    print(cost(A))
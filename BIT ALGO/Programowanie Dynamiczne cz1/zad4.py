# Created by Marcin "Cozoob" Kozub at 23.04.2021 00:35

# Dostajemy tablicę (M x N) wypełnioną wartościami(kosztem wejścia).
# Mamy znaleźć minimalny koszt potrzebny do dostania się z pozycji [0][0] do [M-1][N-1]
#
#
# Wprowadzimy na początek pewne ułatwienia:
# 1. Możemy poruszać się tylko w bok i w dół
# 2. Wszystkie koszty są dodatnie

# f(i, j) - minimalny koszt przejscia z pozycji 0,0 na pozycje i,j
# f(i, j) = min( f(i-1, j), f(i, j - 1) ) + A[i][j]
# f(0,0) = A[0][0]

def cost(A):
    m = len(A)
    n = len(A[0])

    result = [[0 for _ in range(n)] for _ in range(m)]
    result[0][0] = A[0][0]

    # wypelniam poczatkowe wartosci w tablicy rozwiazan
    for i in range(1, n):
        result[0][i] = result[0][i - 1] + A[0][i]

    for j in range(1, m):
        result[j][0] = result[j - 1][0] + A[j][0]

    # teraz uzupelniam reszte przy pomocy mojej funkcji
    for i in range(1, m):
        for j in range(1, n):
            result[i][j] = min(result[i-1][j], result[i][j-1]) + A[i][j]

    return result[m-1][n-1]


if __name__ == '__main__':
    A = [[3, 4, 5, 2, 1], [1, 2, 13, 7, 8], [3, 1, 4, 6, 5], [2, 8, 11, 10, 3], [3, 5, 1, 6, 2]]
    print(cost(A))
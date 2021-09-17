# Created by Marcin "Cozoob" Kozub at 23.04.2021 22:24

# Dostajemy listę wartości. Gramy z drugim graczem. Wybieramy zawsze jedną wartość z jednego z końców tablicy
# i dodajemy do swojej sumy, a następnie to samo robi nasz przeciwnik. Zakładając, że przeciwnik gra optymalnie,
# jaką maksymalną sumę możemy uzbierać?
# “Uogólniony problem paczki mentosów”

# WAZNE: MY ZACZYNAMY

# zlozonosc czasowa O(n^2)

# f(i,j) - maksymalny zysk jaki gracz moze uzsykac po zebraniu monet od i-tego do j-tego miejsca
# 0 <= i <= j

# f(i,j) = max( A[i] + min(f(i - 1, j - 1), f(i - 2, j)), A[j] + min(f(i - 1, j - 1), f(i, j - 2)) )
# f(i,j) = A[i], gdy i == j
# f(i,j) = max(A[i], A[j]), gdy i + 1 == j

def to_win(A):
    # w zmiennej profit bede zapisywac wynik
    profit = -1
    # zatem wprowadzamy nasza strategie w zycie
    j = len(A) - 1

    # tworze sobie pomocznia tablice  j x j w ktorej bede zapisywac wyniki
    P = [[0 for _ in range(j + 1)] for _ in range(j + 1)]
    # uzupelniam poczatkowe wartosci
    for a in range(j + 1):
        for b in range(j + 1):
            if a > b:
                # taki przedzial nie spelnia warnuku ze i <= j
                P[a][b] = -1
            if a == b:
                P[a][b] = A[a]
            if a + 1 == b:
                P[a][b] = max(A[a], A[b])

    # szukam pierwszego zera od konca w tablicy P
    # wykonuje funkcje i szukam kolejnego zera
    # dotad az uzupelnie wszystkie wartosci w P
    for a in range(j + 1):
        # jesli znalazlem 0 to uzupelniam 0 na skos
        if P[0][a] == 0:
            x = 0
            y = a
            while y != j + 1:
                P[x][y] = max(A[x] + min(P[x + 1][y - 1], P[x + 2][y]), A[y] + min(P[x + 1][y - 1], P[x][y - 2]))
                y += 1
                x += 1

    return P[0][j]

if __name__ == '__main__':
    # Driver Code
    # 22
    arr1 = [8, 15, 3, 7]
    print(to_win(arr1))

    # 4
    arr2 = [2, 2, 2, 2]
    print(to_win(arr2))

    # 42
    arr3 = [20, 30, 2, 2, 2, 10]
    print(to_win(arr3))
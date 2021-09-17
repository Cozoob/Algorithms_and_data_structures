# Created by Marcin "Cozoob" Kozub 27.06.2021

# Zadanie 5 (dwuwymiarowy problem plecakowy) Proszę zaproponować algorytm dla dwuwymiarowej
# wersji dyskretnego problemu plecakowego. Mamy dany zbiór P = {p1, . . . , pn} przedmiotów i dla każdego
# przedmiotu pi dane sa nastepujace trzy liczby:
# 1. v(pi) – wartość przedmiotu,
# 2. w(pi) – waga przedmiotu, oraz
# 3. h(pi) – wysokość przedmiotu.
# Złodziej chce wybrać przedmioty o maksymalnej wartości, których łączna waga nie przekracza danej liczby
# W oraz których łączna wysokość nie przekracza danej liczby H (przedmioty zapakowane są w kartony, które
# złodziej układa jeden na drugim). Proszę oszacować złozoność czasową swojego algorytmu oraz uzasadnić
# jego poprawność.

# f(i, w, h) - najwiekszy zysk jaki mozna osiagnac wybierajac sposrod przedmiotow
# o indeksach od 0 do i przedmioty, nie przekraczajac wagi w oraz nie przekraczajace wysokosci h
# W - tablica wag przedmiotow
# P - tablica zyskow przedmiotow
# H - tablica wysokosci przedmiotow
# f(i, w, h) = max( f(i - 1, w, h), f(i - 1, w - W[i], h - H[i]) + P[i] : w - W[i] >= 0 , h - H[i] >= 0)
# Warunki brzegowe:
# f(i,0,0) = 0
# f(0,w, h) = {P[0], jesli W[0] <= w oraz H[0] <= h
#             { 0, jesli W[0] > w oraz H[0] > h , dla w > 0 i h > 0

def Knapsack2D(A, W, H):
    n = len(A)
    # ai = (pi, wi, hi); pi - cena za i-ty przedmiot, wi - waga i-tego przedmiotu, hi - wyskosc i-tego przedmiotu

    F = [[[-1 for _ in range(H + 1)] for _ in range(W + 1)] for _ in range(n)]

    for i in range(n):
        F[i][0][0] = 0

    for w in range(W + 1):
        for h in range(H + 1):
            if w - A[0][1] >= 0 and h - A[0][2] >= 0:
                F[0][w][h] = A[0][0]
            else:
                F[0][w][h] = 0


    best = _rek(n - 1, W, H, F, A)

    return best

def _rek(i, w, h, F, A):
    if i < 0:
        return -1
    if F[i][w][h] != -1:
        return F[i][w][h]

    best = _rek(i - 1, w, h, F, A)
    if w - A[i][1] >= 0 and h - A[i][2] >= 0:
        best = max(best, _rek(i - 1, w - A[i][1], h - A[i][2], F, A) + A[i][0])

    F[i][w][h] = best
    return F[i][w][h]

if __name__ == '__main__':
    P = [5, 12, 7, 1, 56, 4]
    W = [1, 11, 9, 4, 10, 2]
    H = [7, 13, 1, 9, 27, 1]
    A = [[5, 1, 7], [12, 11, 13], [7, 9, 1], [1, 4, 9], [56, 10, 27], [4, 2, 1]]
    print(Knapsack2D(A, 20, 35))
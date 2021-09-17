# Created by Marcin "Cozoob" Kozub at 11.04.2021 20:48

# f(i,p) = minimalna waga jaka trzeba uzyc aby uzywajac
# i przedmiotow osiagnac zysk rowny p

def print_2d(tab):
    for i in range(len(tab)): print(tab[i])

def Knapsack2(W, P, MaxW):
    n = len(P)
    # zapisuje najwiekszy zysk jaki moge osiagnac w MaxP
    MaxP = 0
    for i in range(n):
        MaxP += P[i]
    # zapisuje pomocnicza zmienna inf ktora jest wieksza niz
    # suma wszystkich wag przedmiotow
    inf = 1
    for i in range(n):
        inf += W[i]

    # tworze tablice tablic F
    F = [[0] * (MaxP + 1) for _ in range(n)]
    # print_2d(F)

    # w tablie F wpisuje wage inf
    # dla wszystkich zyskow od 1 do MaxP
    for p in range(1, MaxP + 1):
        F[0][p] = inf
    # w tablice F wpsiuje wage przedmiotu i=0 (pierwszego przedmiotu) w W (tzn. W[0])
    F[0][P[0]] = W[0]


    # teraz ide po calej tablicy F i uzupelniam reszte
    for i in range(1,n):
        for p in range(1, MaxP + 1):

            F[i][p] = F[i - 1][p]

            if p >= P[i]:
                F[i][p] = min(F[i][p], F[i - 1][p - P[i]] + W[i])

    print_2d(F)
    for p in range(MaxP, -1, -1):
        for i in range(n):
            if F[i][p] <= MaxW:
                S = get_solution2(F, W, P, i, p)
                return p, S


def get_solution2(F, W, P, i, p):

    if i < 0: return []

    if i == 0:
        if p == P[0]: return [0]
        return []

    if p >= P[i] and F[i][p] == F[i-1][p-P[i]] + W[i]:
        return get_solution2(F, W, P, i-1, p-P[i]) + [i]

    return get_solution2(F, W, P, i-1, p)

if __name__ == '__main__':
    P = [10, 8, 4, 5, 3, 7]
    W = [4, 5, 12, 9, 1, 13]
    print(Knapsack2(W, P, 24))
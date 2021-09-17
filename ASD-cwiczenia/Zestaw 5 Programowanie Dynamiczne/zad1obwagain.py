# Created by Marcin "Cozoob" Kozub 15.05.2021
# Zadanie 1. (problem plecakowy) Proszę podać i zaimplementować algorytm znajdujący wartość optymalnego zbioru przedmiotów w dyskretnym problemie plecakowym. Algorytm powinien działać w czasie
# wielomianowym względem liczby przedmiotów oraz sumy ich profitów. (Chodzi o to ze kazda rzecz pakowana do plecaka moze wystapic tylko jeden raz).

# f(i, p) - minimalna waga jaka trzeba uzyc aby biorac i przedmiotow osiagnac zysk rowny p
# f(i, p) = min(f(i - 1, p), f(i - 1, p - Pi) + Wi), gdzie Pi to profit i-tego przedmioty, Wi to waga i-tego przedmiotu
# f(i, 0) = 0
# f(0, p) = +inf
# f(0, P0) = W0

# K to pojemnosc plecaka
def Discrete_Knapsack(P, W, K):
    n = len(P)
    # zapisuje najwiekszy zysk jaki moge osiagnac w MaxP
    # w MaxW najwieksza wage jaka moge miec + 1; czyli takie nasze +inf
    MaxP = 0
    MaxW = 1
    for i in range(n):
        MaxP += P[i]
        MaxW += W[i]

    # tworze tablice F do zapisywania wynikow
    F =[[0 for _ in range(MaxP + 1)] for _ in range(n)]
    for p in range(1, MaxP + 1):
        F[0][p] = MaxW
    # uzupelniam wartosc startowa tzn dla przedmiotu 0 jego wage
    F[0][P[0]] = W[0]

    # uzupelniam reszte tablicy F
    for i in range(1, n):
        for p in range(1, MaxP + 1):
            if p - P[i] >= 0:
                F[i][p] = min(F[i - 1][p], F[i - 1][p - P[i]] + W[i])
            else:
                F[i][p] = F[i - 1][p]
    # moje rozwiazanie to profit
    profit = 0
    for i in range(MaxP + 1):
        if F[n - 1][i] <= K and profit < i:
            profit = i

    return profit


if __name__ == '__main__':
    P = [10, 8, 4, 5, 3, 7]
    W = [4, 5, 12, 9, 1, 13]
    print(Discrete_Knapsack(P, W, 24))
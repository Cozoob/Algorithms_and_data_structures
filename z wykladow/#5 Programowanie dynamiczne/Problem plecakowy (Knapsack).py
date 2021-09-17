# Created by Marcin "Cozoob" Kozub at 10.04.2021 21:41
# knap - rozbijac
# sack - plecak
# O(n*Maxw) gdzie n to ilosc elementow do ukradniecia a Maxw to maksymalna waga przedmiotu

def Knapsack(W, P, Maxw):
    n = len(W)
    F = [None] * n
    for i in range(n):
        F[i] = [0]*(Maxw + 1)
    for w in range(1, Maxw + 1):
        F[0][w] = P[0]

    for i in range(1, n):
        for w in range(1, Maxw + 1):
            F[i][w] = F[i - 1][w]
            if w >= W[i]:
                F[i][w] = max(F[i][w], F[i-1][w-W[i]] + P[i])
    return F[n-1][Maxw], F


# z wykladu a cos nie dziala... xD
def getsolution(F, W, P, i, w):
    if i < 0: return []
    if i == 0:
        if w >= W[0]: return[0]
        return []
    if w >= W[i] and F[i][w] == F[i - 1][w-W[i]] + P[i]:
        return getsolution(F, W, P, i - 1, w - W[i]) + [i]
    return getsolution(F, W, P, i - 1, w)


if __name__ == '__main__':
    W = [4,1,2,4,3,5,10,3]
    P = [7,3,2,10,4,1,7,2]
    Maxw = 10
    solution, F = Knapsack(W, P, Maxw)
    print(solution)
    tab = getsolution(F, W, P, len(W) - 1, Maxw)
    for i in range(len(tab)):
        idx = tab[i]
        print(W[idx], P[idx], end=' | ')


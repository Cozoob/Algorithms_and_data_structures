# Created by Marcin "Cozoob" Kozub 26.06.2021

# Wykaz, przedmioty o jak najwiekszej wartosci, ktore lacznie nie przekraczaja
# dopuszczalnej wagi.

# f(i, w) - najwiekszy zysk jaki mozna osiagnac wybierajac sposrod przedmiotow
# o indeksach od 0 do i przedmioty, nie przekraczajac wagi w
# W - tablica wag przedmiotow
# P - tablica zyskow przedmiotow
# f(i, w) = max( f(i - 1, w), f(i - 1, w - W[i]) + P[i] : w - W[i] >= 0 )
# Warunki brzegowe:
# f(i,0) = 0
# f(0,w) = {P[0], jesli W[0] <= w
#          { 0, jesli W[0] > w      , dla w > 0

def Knapsack(W, P, w):
    n = len(W)

    F = [[-1 for _ in range(w + 1)] for _ in range(n)]
    for i in range(n):
        F[i][0] = 0

    for j in range(1, w + 1):
        if j - W[0] >= 0:
            F[0][j] = P[0]
        else:
            F[0][j] = 0

    for i in range(1, n):
        for j in range(1, w + 1):
            F[i][j] = F[i-1][j]

            if j - W[i] >= 0 and F[i][j] < F[i - 1][j - W[i]] + P[i]:
                F[i][j] = F[i - 1][j - W[i]] + P[i]


                #F[i][j] = max(F[i][j], F[i - 1][j - W[i]] + P[i])



    return F[n - 1][w], F



if __name__ == '__main__':
    W = [4, 1, 2, 4, 3, 5, 10, 3]
    P = [7, 3, 2, 10, 4, 1, 7, 2]

    #print(Knapsack(W, P, 10))
    _, l = Knapsack(W, P, 10)
    for elem in l:
        print(elem)
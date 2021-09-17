# Created by Marcin "Cozoob" Kozub 16.05.2021
# Zadanie 1. (Black Forest) Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las
# składa się z n drzew rosnących na pozycjach 0, . . . , n−1. Dla każdego i ∈ {0, . . . , n−1} znany jest zysk ci, jaki
# można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać maksymalny zysk ze ścinanych
# drzew, ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować algorytm, dzięki któremu
# John znajdzie optymalny plan wycinki.

# f(i) - maksymalny zysk ze sciecia i drzew, tak aby nie sciac dwoch drzew pod rzad
# f(i) = max( f(i - 2) + C[i], f(i - 1) ), gdzie C[i], to zysk ze sciecia drzewa i
# f(0) = C[0]
# f(1) = { C[0] : C[0] >= C[1]
#        { C[1] : C[1] > C[0]


# O()
def cut_woods(profit_woods):
    n = len(profit_woods)
    F = [0 for _ in range(n)]

    F[0] = profit_woods[0]
    if profit_woods[0] >= profit_woods[1]:
        F[1] = profit_woods[0]
    else:
        F[1] = profit_woods[1]

    for i in range(2, n):
        if F[i - 2] + profit_woods[i] >= F[i - 1]:
            F[i] = F[i - 2] + profit_woods[i]
        else:
            F[i] = F[i - 1]

    res = get_solution(n - 1, F, profit_woods, [])


    return F[n - 1], res

def get_solution(i, F, C, res):
    if i < 2:
        if C[1] >= C[0]:
            res.append(C[1])
            return res
        else:
            res.append(C[0])
            return res
    # to oznacza ze scialem drzewo i
    if F[i] == F[i - 2] + C[i]:
        res = get_solution(i - 2, F, C, res)
        res.append(C[i])
    else:
        res = get_solution(i - 1, F, C, res)

    return res

if __name__ == '__main__':
    C = [3, 201, 5, 8, 2, 201]
    print(cut_woods(C))
    C = [2, 4, 5, 100, 15, 4, 12]
    print(cut_woods(C))
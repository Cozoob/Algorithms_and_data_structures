# Created by Marcin "Cozoob" Kozub 27.06.2021
# Zadanie 1. (Black Forest) Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las
# składa się z n drzew rosnących na pozycjach 0, . . . , n−1. Dla każdego i ∈ {0, . . . , n−1} znany jest zysk ci
# , jaki
# można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać maksymalny zysk ze ścinanych
# drzew, ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować algorytm, dzięki któremu
# John znajdzie optymalny plan wycinki.


# f(i) - maksymalny zysk ze scinanych drzew od 0 do i, tak, że zadne dwa drzewa nie sa sciete pod rzad
# C[i] - zysk po scieciu drzewa na pozycji i
# f(i) = max( f(i - 2) + C[i], f(i - 1) ) ; i > 1
# f(0) = C[0]
# f(1) = max(C[1], C[0])

def cut_the_woods(C):
    n = len(C)
    if n == 0:
        return C[0], [0]
    if n == 1:
        if C[1] >= C[0]:
            return C[1], [1]
        else:
            return C[0], [0]

    F = [-1 for _ in range(n)]
    F[0] = C[0]
    F[1] = max(C[0], C[1])
    for i in range(2, n):
        F[i] = max(F[i - 2] + C[i], F[i - 1])

    res = get_solution(C, F)

    return F[n - 1], res

def get_solution(C, F):
    res = []
    n = len(C)
    k = n - 1
    T = F[n - 1]
    while k > -1:
        if k > - 2 and F[k] == F[k - 1]:
            k -= 1
        res.append(C[k])
        T -= C[k]
        while k > -1 and T != F[k]:
            k -= 1

    return res[::-1]

if __name__ == '__main__':
    C = [2, 4, 5, 100, 15, 4, 12]
    print(cut_the_woods(C))
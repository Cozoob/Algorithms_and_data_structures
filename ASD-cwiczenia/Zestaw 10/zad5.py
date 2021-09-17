# Created by Marcin "Cozoob" Kozub 12.06.2021
# Zadanie 5. (autostrady) W pewnym państwie, w którym znajduje się N miast, postanowiono połączyć
# wszystkie miasta siecią autostrad, tak aby możliwe było dotarcie autostradą do każdego miasta. Ponieważ
# kontynent, na którym leży państwo jest płaski położenie każdego z miast opisują dwie liczby x, y, a odległość
# w linii prostej pomiędzy miastami liczona w kilometrach wyraża się wzorem
# len = sqrt((x1 − x2)^2 + (y1 − y2)^2).
# Z uwagi na oszczędności materiałów autostrada łączy dwa miasta w linii prostej.
# Ponieważ zbliżają się wybory prezydenta, wszystkie autostrady zaczęto budować równocześnie i jako cel
# postanowiono zminimalizować czas pomiędzy otwarciem pierwszej i ostatniej autostrady.
# Czas budowy autostrady wyrażony w dniach wynosi ⌈len⌉ (sufit z długości autostrady wyrażonej w km). Proszę zaproponować
# algorytm wyznaczający minimalną liczbę dni dzielącą otwarcie pierwszej i ostatniej autostrady.
from math import sqrt
from math import ceil
# Pomysł: Utworzyc graf G, gdzie kazde miasto jest połączone z kazdym a waga krawedzi pomiedzy miastami to ich dni budowy
# sufit(len) tak jak podano we wzorze. Nastepnie szukamy maksymalnego drzewa rozpinajacego przy pomocy zmodyfikowanego
# algorytmu Kruskala usawajac po jednej krawedzi.
# Zlozonosc czasowa: O(E^2logE) przez zmod. algorytm Kruskala



def fun_len(x1, y1, x2, y2):
    x = x1 - x2
    y = y1 - y2
    x = x * x
    y = y * y
    answer = sqrt(x + y)
    return int(ceil(answer))


def matrix_to_list(G):
    n = len(G)

    W = [[] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if G[u][v] > 0:
                W[u].append((v, G[u][v]))

    return W


def Kruskal(G, vertices):
    def find(x):
        nonlocal parent
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)

        if x == y:
            return
        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y
            if rank[x] == rank[y]: rank[y] += 1

    n = len(G)
    A = []
    # FIND - UNION
    parent = [i for i in range(vertices)]
    rank = [0] * vertices

    G.sort(key=lambda x: x[2])
    # print(G)

    for i in range(n):
        u, v, w = G[i]

        x = find(u)
        y = find(v)

        if x != y:
            union(x, y)
            A.append((u, v, w))
            A.append((v, u, w))  # jesli nieskierowany

    group = find(0)
    for i in range(1, vertices):
        if find(i) != group: return None

    return A


def highway(T):
    n = len(T)
    G_prim = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            G_prim[i][j] = fun_len(T[i][0], T[i][1], T[j][0], T[j][1])

    G = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            G.append([i, j, G_prim[i][j]])

    best = float("inf")
    while len(G) > 1:
        A = Kruskal(G, n)
        if A is None: break
        min_val = float("inf")
        max_val = -1
        for i in range(len(A)):
            min_val = min(min_val, A[i][2])
            max_val = max(max_val, A[i][2])

        best = min(best, max_val - min_val)

        G.pop(0)

    return best


A = [(10, 10), (15, 25), (20, 20), (30, 40)]
# # odp to 7
print(highway(A))

# runtests( highway )

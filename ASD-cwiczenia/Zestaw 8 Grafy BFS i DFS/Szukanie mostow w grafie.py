# Created by Marcin "Cozoob" Kozub at 10.05.2021 13:01
# Szukanie mostow w grafie
# Algorytm z wykładu:
# 1. Wykonaj DFS, dla kazdego v nalezacego do V zapisujac jego czas odwiedzenia - d(v).
# 2. Dla kazdego v nalezacego do V obliczamy low(v) = min( d(v), min( d(u) ), min ( low(w) ) ).
# min(d(u)) to krawedz wsteczna z v do u; min(low(w)) w jest dzieckiem v w drzewie DFS
# 3. Mosty to krawędzie {v, p(v)} gdzie p(v) - ojciec v w drzewie DFS oraz d(v) = low(v).
# Algorytm zrobiony na reprezentacji grafu przy pomocy list sąsiedztwa.
# DLA GRAFU NIESKIEROWANEGO
# DZIALA :D

def dfs(graph, s):
    n = len(graph)
    # -1 oznacza ze wierzcholek nie zostal odwiedzony
    # w tablicy tej zapisuje pod odpwiednim indeksem czas odwiedzenia wierzcholka
    visited = [-1] * n
    time = 1
    # tablicy parent zapisuje rodzicow danego wierzcholka
    parent = [-1] * n
    # w tablicy low zapisuje wartosc paramtetru low dla danego wierzcholka
    low = [0] * n
    bridges = []

    def dfs_visit(u):
        nonlocal graph, visited, time, parent, bridges, low

        visited[u] = time
        low[u] = time
        for v in graph[u]:
            if visited[v] == -1:
                parent[v] = u
                time += 1
                dfs_visit(v)

        # jesli wierzcholek u ma juz wszystkich sasiadow odwiedzonych
        # to wyliczam jego low (tzn patrzymy na krawedz wtorna)
        min_val = low[u]
        for v in graph[u]:
            if v != parent[u] and min_val > low[v]:
                min_val = low[v]

        low[u] = min_val

        # sprawdzam czy istnieje most
        if low[u] == visited[u] and parent[u] != -1:
            bridges.append([parent[u], u])


    dfs_visit(s)
    return bridges



if __name__ == '__main__':
    # most dla tego grafu to 1-4
    g0 = [
        [1, 2],
        [0, 2, 4],
        [0, 1],
        [4, 5],
        [1, 3, 5],
        [3, 4]
    ]
    print(dfs(g0, 0))

    # dla tego grafu nieskierowanego mosty to 2-3, 1-4 oraz 6-9
    g1 = [
        [1,2],
        [0,2,4],
        [0,1,3],
        [2],
        [1,5,8],
        [4,6],
        [5,7,9],
        [8,6],
        [4,7],
        [6,10,11],
        [9,11],
        [9,10]
    ]
    print(dfs(g1, 0))

    # dla tego grafu nieskierowanego mosty to 2-12, 6-9, 2-3
    g2 = [
        [1, 2, 8],
        [0, 2, 4],
        [0, 1, 3, 12],
        [2],
        [1, 5, 8],
        [4, 6],
        [5, 7, 9],
        [8, 6],
        [0, 4, 7],
        [6, 10, 11],
        [9, 11],
        [9, 10],
        [2]
    ]
    print(dfs(g2,0))
    G = [
        [1, 2, 3],
        [0, 2],
        [0, 1],
        [0, 4],
        [3]
    ]
    print(dfs(G, 0))
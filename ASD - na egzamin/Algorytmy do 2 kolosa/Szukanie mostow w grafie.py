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

# O(V + E)-listy/O(V^2) - macierz

def dfs(graph, s):
    n = len(graph)
    # -1 oznacza ze wierzcholek nie zostal odwiedzony
    # w tablicy tej zapisuje pod odpwiednim indeksem czas odwiedzenia wierzcholka
    visited = [-1 for _ in range(n)]
    time = 1
    # tablicy parent zapisuje rodzicow danego wierzcholka
    parent = [-1 for _ in range(n)]
    # w tablicy low zapisuje wartosc paramtetru low dla danego wierzcholka
    low = [0 for _ in range(n)]
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

#----------------------------------------------------
#listy sasiedztwa
def bridges(G):

    def DFS_Visit(G, v):
        nonlocal time, visited, visit_time, parent, low

        time += 1
        visit_time[v] = time
        visited[v] = True
        low[v] = time

        for u in G[v]:
            if not visited[u]:
                visited[u] = True
                parent[u] = v
                DFS_Visit(G, u)
                low[v] = min(low[v], low[u])
            elif parent[v] != u:
                low[v] = min(low[v], low[u])

        time += 1

    n = len(G)
    visited = [False for _ in range(n)]
    visit_time = [-1 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    low = [-1 for _ in range(n)]
    time = 0
    for v in range(n):
        if not visited[v]:
            DFS_Visit(G, v)

    B = []
    for v in range(n):
        if visit_time[v] == low[v] and parent[v] != -1:
            B.append([parent[v], v])

    return B

#macierz sasiedztwa
#przy interpretacji ze od teraz most istnieje miedzy u i v
#wtw gdy G[u][v] > 1 oraz G[v][u] > 1
def bridges2(G):

    def DFS_Visit(G, v):
        nonlocal time, visited, parent, low, visit_time

        time += 1
        visited[v] = True
        visit_time[v] = time
        low[v] = time

        for u in range(len(G)):
            if G[v][u] == 1:
                if not visited[u]:
                    parent[u] = v
                    DFS_Visit(G, u)
                    low[v] = min(low[v], low[u])
                elif parent[v] != u:
                    low[v] = min(low[v], low[u])
        time += 1

    n = len(G)
    time = 0
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    visit_time = [-1 for _ in range(n)]
    low = [-1 for _ in range(n)]

    DFS_Visit(G, 0)

    for v in range(n):
        if visit_time[v] == low[v] and parent[v] is not None:
            G[v][parent[v]] += 1
            G[parent[v]][v] += 1

    return G



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
    print(bridges(g0))

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
    print(bridges(g1))

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
    print(bridges(g2))
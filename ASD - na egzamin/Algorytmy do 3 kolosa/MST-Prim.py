# Created by Marcin "Cozoob" Kozub 24.06.2021
# Implementacja algorytmu Prima

from queue import PriorityQueue


# repr.list sasiedztwa O(ElogV) w repr. mac. O(V^2)

# implementacja na macierzy
def Prim_algorithm(G):
    n = len(G)
    inf = float("inf")

    weights = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]

    queue = PriorityQueue()
    # niewazne z ktorego wierzcholka zaczniemy
    queue.put([0, 0])
    weights[0] = 0

    while not queue.empty():
        u = queue.get()
        u = u[1]
        for v in range(n):
            if G[u][v] != -1:
                if weights[v] > G[u][v]:
                    weights[v] = G[u][v]
                    parent[v] = u

    return parent, weights
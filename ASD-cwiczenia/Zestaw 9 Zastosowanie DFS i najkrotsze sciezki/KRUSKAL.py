# Created by Marcin "Cozoob" Kozub 13.06.2021
# Implementacja algorytmu Kruskala

# na liscie krawedzi; O(ElogE)
def Kruskala(G, amount_of_vertices):

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
            if rank[x] == rank[y]:
                rank[y] += 1

    n = len(G)
    A = []
    # FIND - UNION
    parent = [i for i in range(amount_of_vertices)]
    rank = [0 for _ in range(amount_of_vertices)]

    G.sort(key=lambda x: x[2])

    for i in range(n):
        u, v, w = G[i]

        x = find(u)
        y = find(v)

        if x != y:
            union(x, y)
            A.append((u, v, w))
            A.append((v, u, w))  # jesli nieskierowany

    return A

def matrix_to_edge_list(G):
    n = len(G)
    new_G = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            new_G.append([i, j, G[i][j]])

    return new_G

def list_to_edge_list(G):
    n = len(G)
    new_G = []

    for i in range(n):
        for elem in G:
            new_G.append([i, elem[0], elem[1]])

    return new_G
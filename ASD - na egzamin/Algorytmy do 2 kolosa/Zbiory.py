# Created by Marcin "Cozoob" Kozub 24.06.2021

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(x, y, rank, parent):
    x = find(x, parent)
    y = find(y, parent)

    if x == y:
        return
    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

def make_set(G):
    n = len(G)

    vertex_amount = 0
    for i in range(n):
        vertex_amount = max(vertex_amount, G[i][0], G[i][1])
    vertex_amount += 1

    # FIND - UNION
    parent = [i for i in range(vertex_amount)]
    rank = [0] * vertex_amount
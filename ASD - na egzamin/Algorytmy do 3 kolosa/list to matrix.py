# Created by Marcin "Cozoob" Kozub 24.06.2021
# sample to jak oznaczam brak krawedzi
def list_to_matrix(G, sample):
    n = len(G)
    new_G = [[sample for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for edge in G[i]:
            u = edge[0]
            w = edge[1]
            new_G[i][u] = w

    return new_G
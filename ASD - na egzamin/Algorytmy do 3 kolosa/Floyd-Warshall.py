# Created by Marcin "Cozoob" Kozub 24.06.2021

# O(V^3)

def Floyd_Warshall(G):
    n = len(G)
    inf = float("inf")
    S = [[inf for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            S[i][j] = G[i][j]


    for t in range(n):

        for u in range(n):
            if u == t:
                continue

            for v in range(n):
                if u == v or t == v:
                    continue

                S[u][v] = min(S[u][v], S[u][t] + S[t][v])

    return S

if __name__ == '__main__':
    inf = float("inf")
    # inf oznacza brak krawedzi pomiedzy wierzcholkami
    G1 = [
        [0, 5, inf, 10],
        [inf, 0, 3, inf],
        [inf , inf, 0, 1],
        [inf, inf, inf, 0]
    ]
    S1 = Floyd_Warshall(G1)
    for elem in S1:
        print(elem)
    print()


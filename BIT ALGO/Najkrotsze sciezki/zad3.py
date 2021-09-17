# Created by Marcin "Cozoob" Kozub 30.05.2021

# Zaimplementuj algorytm Floyda-Warshalla tak, aby pozostawiał informację pozwalającą na  rekonstrukcję najkrótszej ścieżki
# między dwoma dowolnymi parami wierzchołków w czasie zależnym od długości tej ścieżki.

# algorym ktory szuka najkrotszych sciezek ze wszystkich wierzcholkow do wszystkich
# n:n gdzie n to ilosc wierzcholkow w grafie G
# Dijkstra i alg. Bellmana-Forda szuka 1:n (Bellmana-Forda w sytuacji gdy wagi moga byc ujemne)

# reprezentacja macierzowa grafu G
def Floyd_Warshall(G):
    n = len(G)
    inf = float("inf")
    # inicjalizacja macierzy S oraz P parentow wierzcholkow
    S = [[inf for _ in range(n)] for _ in range(n)]
    P = [[-1 for _ in range(n)] for _ in range(n)]

    # inicjalizuje tablice S oraz P
    for v in range(n):
        S[v][v] = 0

    for v in range(n):
        for u in range(n):
            if G[v][u] != -1:
                S[v][u] = G[v][u]
                P[v][u] = v

    # przechodze do glownej czesci algorytmu
    for t in range(n):
        for u in range(n):
            for v in range(n):
                if S[u][v] > S[u][t] + S[t][v]:
                    S[u][v] = S[u][t] + S[t][v]
                    P[u][v] = P[t][v]

    return S, P

# dodatkowo chce uzyskac najkrotsza sciezke z s do t
def get_shortest_path(G, s, t):
    S, P = Floyd_Warshall(G)
    distance = S[s][t]

    # czyli odtwarzam sciezkie z t do s
    res = []
    while t != s:
        res.append(t)
        # print(t, end=' ')
        t = P[s][t]
    # print(s)
    res.append(s)
    return res, distance


if __name__ == '__main__':

    G0 = [
        [-1, 1, -1, -1],
        [1, -1, 1, 10],
        [-1, 1, -1, 1],
        [-1, 10, 1, -1]
    ]
    print(Floyd_Warshall(G0))
    print(get_shortest_path(G0, 0,3))
# Created by Marcin "Cozoob" Kozub 30.05.2021

# zad2 obw
# Dany jest graf skierowany G = (V, E) w reprezentacji macierzowej (bez wag). Proszę zaimplementować
# algorytm, który oblicza domknięcie przechodnie grafu G (domknięcie przechdonie grafu G to taki graf H,
# że w H mamy krawedz z u do v wtw gdy w G jest sciezka skierowana z u do v).

# Aby znalezc domkniecie przechodnie grafu G uzyje po prostu algorytmu Floyda-Warshalla.

def Floyd_Warshall(G):
    n = len(G)
    inf = float("inf")
    # inicjalizacja macierzy S
    S = [[inf for _ in range(n)] for _ in range(n)]
    # w res w krotkach trzymam domkniecie przechodnie grafu G,
    res = []

    # inicjalizuje tablice S
    for v in range(n):
        S[v][v] = 0

    for v in range(n):
        for u in range(n):
            if G[v][u] != -1:
                S[v][u] = G[v][u]
                res.append((v, u))

    # przechodze do glownej czesci algorytmu
    for t in range(n):
        for u in range(n):
            for v in range(n):
                if S[u][v] > S[u][t] + S[t][v]:
                    S[u][v] = S[u][t] + S[t][v]
                    res.append((u, v))

    res.sort()
    return res

if __name__ == '__main__':
    # -1 - brak krawedzi ; 1 - jest krawedz
    G = [
        [-1, 1, -1, -1, -1, 1, -1],
        [-1, -1, 1, -1, -1, -1, -1],
        [-1, -1, -1, 1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, 1, -1]
    ]
    print(Floyd_Warshall(G))
# Created by Marcin "Cozoob" Kozub at 09.05.2021 15:34
# Średnicą drzewa nazywamy odległość między jego najbardziej oddalonymi od siebie wierzchołkami.
# Napisz algorytm, który przyjmując na wejściu drzewo (niekoniecznie binarne!) w postaci listy krawędzi zwróci jego średnicę.

# Najpierw odpalamy DFS na dowolnym wierzcholku v i znajdujemy wierzcholek u ktory jest najdalej od wierzcholka v.
# Skoro jest najdalej to MUSI znajdowac na srednicy drzewa. Teraz wystarczy odpalic DFS na wierzcholku v i znalesc
# odleglosc do najdluzszego wierzcholka od wierzcholka v, bo jestesmy juz na srednicy.

def find_diameter_DFS(graph):
    n = len(graph)
    # tablica d zapisuje odleglosci, jesli odleglosc -1 tzn ze wierzcholek nieodwiedzony
    d = [-1] * n

    def DFS_visit(u, s):
        nonlocal graph, d

        # s to aktualna odleglosc od pocz. punktu
        d[u] = s
        s += 1
        for v in graph[u]:
            if d[v] == -1:
                DFS_visit(v, s)

    # dowonlny punkt naprawde; niech bedzie 5
    DFS_visit(5, 0)

    # i teraz znajduje ktory wierzcholek był najdalej
    max_val = d[0]
    u = 0
    for i in range(1, n):
        if d[i] > max_val:
            max_val = d[i]
            u = i

    # czyszcze tablice d i dla wierzcholka u odpaldam DFS
    # i na koncu wystarczy ze zczytam maksymalna wartosc w tablicy d
    for i in range(n):
        d[i] = -1

    DFS_visit(u, 0)

    return max(d)

if __name__ == '__main__':
    # odleglosc rozumiem jako ilosc krawedzi miedzy wierzcholkami (a nie ilosc wierzcholkow)
    g1 = [
        [1],
        [0,2],
        [3,4,5,1],
        [2],
        [2],
        [2,6,7,8],
        [5],
        [5],
        [5,9,13],
        [8,11,10],
        [9],
        [9,12],
        [11],
        [8,14],
        [13]
    ]
    print(find_diameter_DFS(g1))
    g2 = [
        [1],
        [0, 2, 3],
        [1, 3, 4, 18],
        [1, 2, 4, 5, 6],
        [2, 3, 5, 12],
        [3, 7, 8, 4],
        [3, 7, 10],
        [6, 5, 9],
        [5, 9, 13],
        [7, 8, 14],
        [6, 11],
        [10],
        [18, 4, 13],
        [12, 8, 14],
        [9, 13, 15],
        [14, 16],
        [15, 17],
        [16],
        [2, 12]
    ]
    print(find_diameter_DFS(g2))
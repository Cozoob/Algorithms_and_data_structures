# Created by Marcin "Cozoob" Kozub 30.05.2021
from queue import PriorityQueue
# zad1 obw
# Dany jest graf nieskierowany G=(V,E) z wazonymi krawedziami (w: E -> N; N - zb. liczb naturalnych).
# Prosze zaproponować jak najszybszy algorytm, który znajduje ścieżkę z danego wierzcholka s do danego
# wierzcholka t, taką, że:
# a) Każda kolejna krawedz ma mniejsza wage niz poprzednia.
# b) Sposrod sciezek spelniajacych powyzszy warunek, znaleziona ma najmniejsza sume wag.

# Pomysl: Uzycie zmodyfikowanego algorytmu Dijkstry. Jedyne co sie zmienia to relaksacja troche
# tak aby sciezka ktora szukam spelniala warunki zadania.

# reprezentacja macierzowa
def find_path(G, s, t):

    # u i v to krotki/tablice wierzcholkow u oraz v
    def relax(u, distance_u, v, distance_v, parent, G):

        if distance_v > distance_u + G[u][v]:
            distance_v = distance_u + G[u][v]
            parent[v] = u

        v = [distance_v, v, G[u][v]]
        return v, parent

    n = len(G)
    inf = float("inf")
    parent = [-1 for _ in range(n)]

    queue = PriorityQueue()
    # umieszczam wszystkie wierzcholki w kolejce priorytetowej
    # wraz z informacja o odleglosc do s
    # [distance to s, vertex, waga poprzedniej krawedzi]
    # dla wierzcholka s ustawiam distance = 0 i wage "poprzedniej krawedzi" na inf (bo nie istnieje)
    queue.put([0, s, inf])

    # nasz zbior wierzcholkow przetworzony z informacja o odleglosci do s
    distance = [inf for _ in range(n)]
    distance[s] = 0


    # dopoki sa wierzcholki w kolejce
    while not queue.empty():
        # wyjmuje wierzcholek u o minimalnym oszacowaniu odleglosci
        u = queue.get()
        # weight to waga poprzedniej krawedzi
        weight = u[2]
        u = u[1]
        for v in range(n):
            # tutaj dodaje dodatkowy warunek
            if G[u][v] != -1 and G[u][v] < weight:
                # dla kazdej krawedzi {u, v} wykonuje relaksacje
                new_v, parent = relax(u, distance[u], v, distance[v], parent, G)
                if new_v[0] < distance[v]:
                    distance[v] = new_v[0]
                    queue.put(new_v)

    # pozostaje tylko odtworzyc sciezke z s do t
    if parent[t] == -1:
        # to oznacza ze sciezka ktora by spelniala warunki zadania nie istnieje
        return None
    res = []
    while t != s:
        res.append(t)
        t = parent[t]
    res.append(s)


    return res

if __name__ == '__main__':
    # -1 to brak krawedzi
    G0 = [
        [-1, 5, -1, 3, -1, -1],
        [5, -1, 4, -1, -1, -1],
        [-1, 4, -1, -1, -1, 1],
        [3, -1, -1, -1, 2, -1],
        [-1, -1, -1, 2, -1, 1],
        [-1, -1, 1, -1, 1, -1]
    ]
    print(find_path(G0, 0, 5))
    print(find_path(G0, 0, 2))
    # dla tego grafu z wierzcholka 5 sa same rosnace krawedzie w obie strony (no oprocz do wierzcholka 2 i 4)
    print(find_path(G0, 5, 0))
    print(find_path(G0, 5, 2))
    # G1 to graf G0 tylko waga krawedzi miedzy wierzcholkami {2,5} teraz rowna 0
    G1 = [
        [-1, 5, -1, 3, -1, -1],
        [5, -1, 4, -1, -1, -1],
        [-1, 4, -1, -1, -1, 0],
        [3, -1, -1, -1, 2, -1],
        [-1, -1, -1, 2, -1, 1],
        [-1, -1, 0, -1, 1, -1]
    ]
    # odp to 0-3-4-5-2
    print(find_path(G1, 0, 2))
# Created by Marcin "Cozoob" Kozub 31.05.2021
from queue import PriorityQueue

def gas(G, s, D):
    # D - pojemnosc baku

    def relax(u, distance_u, v, distance_v, parent, G):

        if distance_v > distance_u + G[u][v]:
            distance_v = distance_u + G[u][v]
            parent[v] = u

        v = [distance_v, v]
        return v, parent


    n = len(G)
    inf = float("inf")
    parent = [-1 for _ in range(n)]

    queue = PriorityQueue()
    # umieszczam wszystkie wierzcholki w kolejce priorytetowej
    # wraz z informacja o odleglosc do s
    # [distance to s, vertex]
    # dla wierzcholka s ustawiam distance = 0

    # dla tresci zadania rozdzielam kazdy wierzcholek na ilosc mozliwosci zatankowan

    queue.put([0, s])

    # nasz zbior wierzcholkow przetworzony z informacja o odleglosci do s
    distance = [inf for _ in range(n)]
    distance[s] = 0

    # dopoki sa wierzcholki w kolejce
    while not queue.empty():
        # wyjmuje wierzcholek u o minimalnym oszacowaniu odleglosci
        u = queue.get()
        u = u[1]
        for v in range(n):
            if G[u][v] != -1:
                # dla kazdej krawedzi {u, v} wykonuje relaksacje
                new_v, parent = relax(u, distance[u], v, distance[v], parent, G)
                if new_v[0] < distance[v]:
                    distance[v] = new_v[0]
                    queue.put(new_v)

    return distance
# Created by Marcin "Cozoob" Kozub 12.06.2021
# Zadanie 6. (najlepszy korzeń) Dany jest acykliczny, spójny nieskierowany, ważony graf T (czyli T jest
# tak naprawdę ważonym drzewem). Proszę wskazać algorytm, który znajduje taki wierzchołek T, z którego
# odległość do najdalszego wierzchołka jest minimalna.
from queue import PriorityQueue
# Pomysł: Najpierw przy pomocy Dijkstry znajduje jeden koniec srednicy grafu T.
# Nastepnie drugi raz wykonuje Dijkstre i znajduje drugi koniec srenicy grafu T.
# Majac oba konce srednicy i dlugosc srednicy d po drugiej Dijkstrze dla obu
# koncow srednicy D1, D2 po raz trzeci i czwarty uzywam Dijkstry ale tym razem szukam takiego
# wierzcholka v ktory abs(d/2 - distance[v]) jest minimalne. Taki wierzcholek v
# bedzie nasza odpowiedzia jesli distanceD1[v1] > distanceD2[v2]: v = v1 else: v = v2

# Zlozonosc czasowa: O(v^2) bo repr. macierzowa

def Dijkstra1(G, s):

    # u i v to krotki/tablice wierzcholkow u oraz v
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


def Dijkstra2(G, s, d):

    # u i v to krotki/tablice wierzcholkow u oraz v
    def relax(u, distance_u, v, distance_v, parent, G):

        if distance_v > distance_u + G[u][v]:
            distance_v = distance_u + G[u][v]
            parent[v] = u

        v = [distance_v, v]
        return v, parent


    n = len(G)
    inf = float("inf")
    parent = [-1 for _ in range(n)]
    answer = inf
    A = s

    queue = PriorityQueue()
    # umieszczam wszystkie wierzcholki w kolejce priorytetowej
    # wraz z informacja o odleglosc do s
    # [distance to s, vertex]
    # dla wierzcholka s ustawiam distance = 0
    queue.put([0, s])

    # nasz zbior wierzcholkow przetworzony z informacja o odleglosci do s
    distance = [inf for _ in range(n)]
    distance[s] = 0

    # dopoki sa wierzcholki w kolejce
    while not queue.empty():
        # wyjmuje wierzcholek u o minimalnym oszacowaniu odleglosci
        u = queue.get()
        if answer > abs(d / 2 - u[0]):
            answer = abs(d/2 - u[0])
            A = u[1]

        u = u[1]


        for v in range(n):
            if G[u][v] != -1:
                # dla kazdej krawedzi {u, v} wykonuje relaksacje
                new_v, parent = relax(u, distance[u], v, distance[v], parent, G)
                if new_v[0] < distance[v]:
                    distance[v] = new_v[0]
                    queue.put(new_v)

    return distance, A


def the_best_root(G):
    n = len(G)

    distance = Dijkstra1(G, 0)
    # znajduje 1 koniec srednicy grafu
    tmp = -1
    D1 = 0
    for i in range(n):
        if tmp < distance[i]:
            tmp = distance[i]
            D1 = i
    # znajduje drugi koniec grafu i zapisuje dlugosc srednicy d
    distance = Dijkstra1(G, D1)
    D2 = 0
    d = -1
    for i in range(n):
        if d < distance[i]:
            d = distance[i]
            D2 = i

    # teraz jeszcze dwa ostatnie razy odpalam Dijkstre
    distance1, v1 = Dijkstra2(G, D1, d)
    distance2, v2 = Dijkstra2(G, D2, d)

    if distance1[v1] > distance2[v2]:
        return v1

    return v2

if __name__ == '__main__':
    T1 = [
        [-1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, -1, 1, 1, -1, -1, -1, -1, -1, -1],
        [-1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1],
        [-1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1],
        [-1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1]
    ]
    print(the_best_root(T1))
    T2 = [
        [-1, -1, -1, 1000, -1, -1, -1],
        [-1, -1, -1, 1, -1, -1, -1],
        [-1, -1, -1, 1, 1, -1, -1],
        [1000, 1, 1, -1, -1, 1, -1],
        [-1, -1, 1, -1, -1, -1, -1],
        [-1, -1, -1, 1, -1, -1, 1],
        [-1, -1, -1, -1, -1, 1, -1]
    ]
    print(the_best_root(T2))
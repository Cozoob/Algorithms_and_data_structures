# Created by Marcin "Cozoob" Kozub 22.05.2021
# ALGORYTM DIJKSTRY (shortest path algorithm)
from queue import PriorityQueue
# 1 implementacja dla reprezentacji macierzowej
# 2 implementacja dla reprezentacji list sąsiedztwa, zlozonosc czasowa: O(ElogV)

# w sumie parent nie jest nam potrzebny jesli chcemy uzyskac tylko distance
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


def Dijkstra2(G, s):

    # u i v to krotki/tablice wierzcholkow u oraz v
    def relax(u, distance_u, v, distance_v, parent, weight):

        if distance_v > distance_u + weight:
            distance_v = distance_u + weight
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

        for v in G[u]:
            # dla kazdej krawedzi {u, v} wykonuje relaksacje
            new_v, parent = relax(u, distance[u], v[0], distance[v[0]], parent, v[1])
            if new_v[0] < distance[v[0]]:
                distance[v[0]] = new_v[0]
                queue.put(new_v)

    return distance



if __name__ == '__main__':
    # Dystans z wierzcholka 0
    # do 0 to 0; do 1 to 4; do 2 to 12; do 3 to 19; do 4 to 21; do 5 to 11; do 6 to 9; do 7 to 8; do 8 to 14
    G1 = [[-1, 4, -1, -1, -1, -1, -1, 8, -1],
         [4, -1, 8, -1, -1, -1, -1, 11, -1],
         [-1, 8, -1, 7, -1, 4, -1, -1, 2],
         [-1, -1, 7, -1, 9, 14, -1, -1, -1],
         [-1, -1, -1, 9, -1, 10, -1, -1, -1],
         [-1, -1, 4, 14, 10, -1, 2, -1, -1],
         [-1, -1, -1, -1, -1, 2, -1, 1, 6],
         [8, 11, -1, -1, -1, -1, 1, -1, 7],
         [-1, -1, 2, -1, -1, -1, 6, 7, -1]
         ]
    print(Dijkstra1(G1, 0))

    # Dystans z wierzcholka 0
    # do 0 to 0; do 1 to 1; do 2 to 3; do 4 to 6; do 5 to 7;
    # u: [[v, waga{u,v}]]
    G2 = [
        [[1, 1], [2, 5]],
        [[0, 1], [2, 2], [3, 8], [4, 7]],
        [[0, 5], [1, 2], [3, 3]],
        [[1, 8], [2, 3], [4, 1]],
        [[1, 7], [3, 1]]
    ]
    print(Dijkstra2(G2, 0))
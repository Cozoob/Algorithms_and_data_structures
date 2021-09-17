from queue import PriorityQueue

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
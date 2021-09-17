# Created by Marcin "Cozoob" Kozub 28.06.2021
# Zadanie 1. (malejące krawędzie, c.d.) Dany jest graf G = (V, E), gdzie każda krawędź ma wagę
# ze zbioru {1, . . . , ∣E∣} (wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dla danych
# wierzchołków x i y oblicza ścieżkę o najmniejszej sumie wag, która prowadzi z x do y po krawędziach o
# malejących wagach (jeśli ścieżki nie ma to zwracamy ∞).


from queue import PriorityQueue
# Zmodyfikowany Dijkstra gdzie w kolejce wrzucam (distance, last_edge, vertex).
# Do kolejnej krawedzi przechodze wtw, gdy waga nastepnej krawedzi jest mniejsza niz last_edge.
# Wrzucam tak kazda mozliwa krawedz do odp. kolejki w tablicy distance tak aby rozpatrzec wszystkie mozliwosci.

# reprezentacja list sasiedztwa
def shortest_decreasing_path(G, s, t):
    n = len(G)
    inf = float("inf")
    queue = PriorityQueue()
    distance = [PriorityQueue() for _ in range(n)]


    queue.put([0, inf, s])

    while not queue.empty():
        elem = queue.get()
        distance_u = elem[0]
        u = elem[2]
        last_edge = elem[1]
        if u == t:
            continue

        # edge[0] - wierzcholek v, edge[1] - waga krawedzi {u, v}
        for edge in G[u]:
            v = edge[0]
            weight = edge[1]
            if last_edge > weight:
                queue.put([distance_u + weight, weight, v])
                # tutaj zapisuje dystans nowy, jaka krawedzia dotarl, oraz rodzica v
                distance[v].put([distance_u + weight, last_edge, u])

    _, last_edge, w = distance[t].get()
    res = [t]
    while w != s:


        while not distance[w].empty():
            parent = distance[w].get()
            if parent[1] > last_edge:
                # znalazlem rodzica
                break

        res.append(w)
        w = parent[2]
        last_edge = parent[1]

    res.append(s)


    return res[::-1]

if __name__ == '__main__':
    G = [[(1, 8), (2, 7), (6, 5)],
         [(0, 8), (2, 6), (3, 5)],
         [(0, 7), (1, 6), (3, 3), (4, 8)],
         [(1, 5), (2, 3), (4, 2), (5, 4), (6, 4)],
         [(2, 8), (3, 2), (5, 3)],
         [(3, 4), (4, 3)],
         [(0, 5), (4, 4)]]

    print(shortest_decreasing_path(G, 0, 5))
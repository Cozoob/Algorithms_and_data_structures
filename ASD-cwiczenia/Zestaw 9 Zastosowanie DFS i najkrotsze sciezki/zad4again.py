# Created by Marcin "Cozoob" Kozub 10.06.2021
# Zadanie 4. (logarytmy) Mamy dany graf G = (V, E) z wagami w∶ E → N−{0} (dodatnie liczby naturalne).
# Chcemy znalezc scieżkę z wierzchołka u do v tak, by iloczyn wag był minimalny. Omówic rozwiązanie (bez
# implementacji)
from queue import PriorityQueue
from math import log2
# A JA ZROBIE Z IMPLEMENTACJA HA!

# Pomysł: Po prostu jesli chcemy zeby iloczyn wag byl minimalny to wykorzystujemy zastosowania logarytmow.
# Tzn.: loga + logb = logab. Zatem logarytmujemy kazda wage i tak szukamy zwyklym algorytmem Dijkstry
# najkrotszej sciezki z u do v.

# Zlozonosc czasowa: O(V^2) - zwykla Dijkstra na repr. macierzowej

def find_path(G, s, t):

    # u i v to krotki/tablice wierzcholkow u oraz v
    def relax(u, distance_u, v, distance_v, parent, G):
        nonlocal res

        if distance_v > log2(distance_u) + log2(G[u][v]):
            distance_v = log2(distance_u) + log2(G[u][v])
            if distance_v == 0:
                distance_v = 1
            parent[v] = u
            res[v] = G[u][v]

        v = [distance_v, v]
        return v, parent


    n = len(G)
    inf = float("inf")
    parent = [-1 for _ in range(n)]

    queue = PriorityQueue()
    # umieszczam wszystkie wierzcholki w kolejce priorytetowej
    # wraz z informacja o odleglosc do s
    # [distance to s, vertex]
    # dla wierzcholka s ustawiam distance = 1
    queue.put([1, s])

    # nasz zbior wierzcholkow przetworzony z informacja o odleglosci do s
    distance = [inf for _ in range(n)]
    distance[s] = 1
    res = [-1 for _ in range(n)]

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


    # cosik slabo to dziala dla 1*1*1*1 XD
    answer = [res[t]]
    tmp = parent[t]
    while tmp != t and tmp != s:
        answer.append(res[tmp])
        tmp = parent[tmp]


    return answer



if __name__ == '__main__':
    # najmniejszy iloczyn to 1 * 1 * 1 * 1
    G0 = [
        [-1, 1, -1, -1, 2],
        [1, -1, 1, -1, -1],
        [-1, 1, -1, 1, -1],
        [-1, -1, 1, -1, 1],
        [2, -1, -1, 1, -1]
    ]
    print(find_path(G0, 0, 4))
    # najmniejszy iloczyn 1*2*2 = 4
    G1 = [
        [-1, 1, -1, 3, 100],
        [1, -1, 2, -1, -1],
        [-1, 2, -1, -1, 2],
        [3, -1, -1, -1, 3],
        [100, -1, 2, 3, -1]
    ]
    print(find_path(G1, 0, 4))
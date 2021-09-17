# Created by Marcin "Cozoob" Kozub 29.06.2021
# Komunikacja miejska w Pewnym Mieście jest dość dziwnie zorganizowana.
# Za przejechanie każdego odcinka między dwiema stacjami obowiązuje osobna opłata.
# Od tej kwoty jest jednak odejmowany całkowity koszt poniesiony od początku podróży (jeśli jest ujemny, po prostu nic się nie płaci).
from queue import PriorityQueue
# Czyli Dijkstra do ktorej w kolejce wrzucam informacje o tym, jaka ostatnio oplate zaplacilem i aktualizuje
# ja zmniejszajac o dana oplate. Jesli ostatni koszt poniesiony za przejazd jest mniejszy niz 0
# to dodaje 0 jak koszt przejazdu przez nastepna krawedz.

# repr. list sasiedztwa
def strange_city(G, s, t):
    n = len(G)
    inf = float("inf")
    cost = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    queue = PriorityQueue()
    # [jaka w sumie oplate juz zaplacil, vertex]
    queue.put([0, s])
    cost[s] = 0


    while not queue.empty():
        last_cost, u = queue.get()
        for elem in G[u]:
            v = elem[0]
            v_cost = elem[1]
            new_cost = v_cost - cost[u]
            if new_cost < 0:
                new_cost = 0
            if cost[v] > new_cost and parent[u] != v:
                cost[v] = new_cost + cost[u]
                queue.put([cost[v], v])
                parent[v] = u

    res = []
    w = t
    while w != s:
        res.append(w)
        w = parent[w]
    res.append(s)

    return res[::-1], cost[t]

if __name__ == '__main__':
    G = [
        [],
        [[2, 60],[4, 120]],
        [[1, 60], [3, 80]],
        [[2, 80], [5, 70]],
        [[1, 120], [5, 150]],
        [[3, 70], [4, 150]]
    ]
    print(strange_city(G, 1, 5))
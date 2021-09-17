# Created by Marcin "Cozoob" Kozub 07.06.2021
# Zadanie 6. (dwóch kierowców) Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to
# miasta a krawędzie to drogi łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach
# jako liczba naturalna). Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V , zamieniając się za kierownicą w każdym kolejnym mieście.
# Alicja wybiera trasę oraz decyduje, kto prowadzi pierwszy.
# Proszę zapropnować algorytm, który wskazuje taką trasę (oraz osobę, która ma prowadzić pierwsza), żeby
# Alicja przejechała jak najmniej kilometrów. Algorytm powinien być jak najszybszy (ale przede wszystkim
# poprawny).

# O(V^2LogE) lub nawet O(V^3) ? Przez zmodyfikowana Dijkstre. Czy da sie lepiej np tym DFS'em?
# NIE DZIALA


from queue import PriorityQueue

# Pomysł: Wystarczy uzyc dwa razy algorytmu Dijkstry ktory raz znajdzie nam najkrotsza wtedy gdyby Alicja zaczynala jechac jako pierwsza
# i drugi raz najkrotsza wtedy gdyby Alicja zaycznala jechac jako druga i z tych dwoch odp wybieram krotsza opcje, ktora bedzie moja odp.
# Dzieki temu dostane informajce kto powinien zaczac jechac i ile km Alicja przejedzie w ostatecznosci.

# reprezentacja macierzowa
def two_drivers(G,s,t):
    # s to nasze miasto-start, t to nasze miasto-meta

    def relax(u, distance_u, v, distance_v, parent, G, counter):

        if distance_v > distance_u + G[u][v]:
            distance_v = distance_u + G[u][v]
            parent[v] = u

        v = [distance_v, v, counter]
        return v, parent


    n = len(G)
    inf = float("inf")
    parent = [-1 for _ in range(n)]
    queue = PriorityQueue()
    # w kolejce dwuelementowe wierzcholki z informacja o odleglosci do wierzcholka s oraz
    # ktory to juz jest z kolei wierzcholek liczac od wierzcholka s
    # [distance to s, vertex, counter]
    queue.put([0,s, 1])
    distance = [inf for _ in range(n)]
    distance[s] = 0

    sum1 = 0
    sum2 = 0
    counter = 1

    while not queue.empty():
        u = queue.get()
        d = u[0]
        u = u[1]
        counter += 1
        for v in range(n):
            if G[u][v] != -1 and counter % 2 != 0 and d != inf:
                new_v, parent = relax(u, distance[u], v, distance[v], parent, G, counter)
                if new_v[0] < distance[v]:
                    distance[v] = new_v[0]
                    queue.put(new_v)
            elif d != inf:
                for k in range(n):
                    if G[v][k] != -1:
                        queue.put([inf, k, counter])



    # if sum1 <= sum2:
    #     return sum1, "Alicja zaczyna pierwsza"
    # else:
    return sum1, "Alicja zaczyna druga"

if __name__ == '__main__':

    G0 = [
        [-1, 2, -1, -1, -1, -1, -1],
        [2, -1, 8, -1, -1, -1, 3],
        [-1, 8, -1, 1, -1, -1, -1],
        [-1, -1, 1, -1, 1, -1, 2],
        [-1, -1, -1, 1, -1, 1, 4],
        [-1, -1, -1, -1, 1, -1, 3],
        [-1, 3, -1, 2, 4, 3, -1]
    ]
    print(two_drivers(G0, 0, 5))
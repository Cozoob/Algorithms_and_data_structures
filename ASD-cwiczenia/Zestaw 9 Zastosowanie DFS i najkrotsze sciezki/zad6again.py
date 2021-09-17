# Created by Marcin "Cozoob" Kozub 11.06.2021
# Zadanie 6. (dwóch kierowców) Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to
# miasta a krawędzie to drogi łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach
# jako liczba naturalna). Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V , zamieniając
# się za kierownicą w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje, kto prowadzi pierwszy.
# Proszę zapropnować algorytm, który wskazuje taką trasę (oraz osobę, która ma prowadzić pierwsza), żeby
# Alicja przejechała jak najmniej kilometrów. Algorytm powinien być jak najszybszy (ale przede wszystkim
# poprawny).
from queue import PriorityQueue

# Pomysł: Stosuje algorytm Dijkstry, gdzie uzywam dwoch dablicy distance. W jednej zapisuje najkrotsza
# trase jaka by przejala Alicja z punktu startowego do wierzcholka v tak jakby zaczynala pierwsza.
# W drugiej to samo tyle ze tak jakby zaczynala jechac jako druga. W tablicy parent rowniez
# zapisuje informacje ktora przyda mi sie do odtworzenia trasy. Pod koniec wybieram, czy
# jako pierwsza czy jako druga Alicja powinna jechac i odtwarzam trase, ktora powinni jechac.

# W sumie mozna to zrobic w jednej tablicy distance ale troche zagmatwane to wtedy by bylo.

# za duza zlozonosc imo myslalme ze lepiej pojdzie...

# z miasta s do t
def two_drivers(G, s, t):

    # u i v to krotki/tablice wierzcholkow u oraz v
    def relax(u, distance_u, v, distance_v, parent, G, x):

        if distance_v > distance_u + G[x][v]:
            distance_v = distance_u + G[x][v]
            parent[v] = u

        v = [distance_v, v]
        return v, parent


    n = len(G)
    inf = float("inf")
    parent1 = [-1 for _ in range(n)]

    queue = PriorityQueue()
    # umieszczam wszystkie wierzcholki w kolejce priorytetowej
    # wraz z informacja o odleglosc do s
    # [distance to s, vertex]
    # dla wierzcholka s ustawiam distance = 0
    queue.put([0, s])

    # nasz zbior wierzcholkow przetworzony z informacja o odleglosci do s
    distance1 = [inf for _ in range(n)]
    distance1[s] = 0

    # dopoki sa wierzcholki w kolejce
    while not queue.empty():
        # wyjmuje wierzcholek u o minimalnym oszacowaniu odleglosci
        u = queue.get()
        u = u[1]
        for x in range(n):
            if G[u][x] != -1:
                for v in range(n):
                    if G[x][v] != -1 and u != v:
                        # dla kazdej krawedzi {u, v} wykonuje relaksacje
                        new_v, parent1 = relax(u, distance1[u], v, distance1[v], parent1, G, x)
                        if new_v[0] < distance1[v]:
                            distance1[v] = new_v[0]
                            queue.put(new_v)

    parent2 = [-1 for _ in range(n)]
    distance2 = [inf for _ in range(n)]

    for i in range(n):
        if G[s][i] != -1:
            queue.put([0, i])
            distance2[i] = 0

    # dopoki sa wierzcholki w kolejce
    while not queue.empty():
        # wyjmuje wierzcholek u o minimalnym oszacowaniu odleglosci
        u = queue.get()
        u = u[1]
        for x in range(n):
            if G[u][x] != -1:
                for v in range(n):
                    if G[x][v] != -1 and u != v:
                        # dla kazdej krawedzi {u, v} wykonuje relaksacje
                        new_v, parent2 = relax(u, distance2[u], v, distance2[v], parent2, G, x)
                        if new_v[0] < distance2[v]:
                            distance2[v] = new_v[0]
                            queue.put(new_v)

    # zostaje mi sprawdzicy czy Alicja ma jechac pierwsza czy druga
    if distance1[t] <= distance2[t]:
        flag = True
    else:
        flag = False

    # no i jeszcze odtworzyc ale da sie napewno szybciej zrobic te zadanie
    if flag is True:
        # Alicja ma jechac pierwsza
        return "Alicja jedzie pierwsza!", distance1[t]

    return "Alicja jedzie druga!", distance2[t]





if __name__ == '__main__':
    G0 = [
        [-1, 5, -1, -1, -1, -1, -1, -1, -1, -1],
        [5, -1, 10, -1, -1, -1, 1, -1, -1, -1],
        [-1, 10, -1, 8, -1, -1, -1, -1, -1, -1],
        [-1, -1, 8, -1, 9, -1, -1, -1, -1, -1],
        [-1, -1, -1, 9, -1, 1, -1, -1, -1, -1],
        [-1, -1, -1, -1, 1, -1, -1, -1, -1, 40],
        [-1, 1, -1, -1, -1, -1, -1, 30, 20, -1],
        [-1, -1, -1, -1, -1, -1, 30, -1, -1, 1],
        [-1, -1, -1, -1, -1, -1, 20, -1, -1, 5],
        [-1, -1, -1, -1, -1, 40, -1, 1, 5, -1]
    ]
    print(two_drivers(G0, 0, 4))
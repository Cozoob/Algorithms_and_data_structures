# Created by Marcin "Cozoob" Kozub 28.06.2021
from queue import PriorityQueue
# Zadanie 6. (dwóch kierowców) Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to
# miasta a krawędzie to drogi łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach
# jako liczba naturalna). Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V , zamieniając się za
# kierownicą w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje, kto prowadzi pierwszy.
# Proszę zapropnować algorytm, który wskazuje taką trasę (oraz osobę, która ma prowadzić pierwsza), żeby
# Alicja przejechała jak najmniej kilometrów. Algorytm powinien być jak najszybszy (ale przede wszystkim
# poprawny).

# Dwa razy Dijkstra tylko ze co drugi wierzcholek (czyli w momencie gdy Bob ma prowadzic) wrzucam
# dany wierzcholek z dystansem poprzednio obliczonym przez Alicje.

# reprezentacja list sasiedztwa
def two_drivers(G, s, t):
    n = len(G)
    inf = float("inf")
    # distance[i][0] - dystans dla Alicji; distance[i][1] - dystans dla Boba
    distance = [[inf, inf] for _ in range(n)]
    parent = [[-1, -1] for _ in range(n)]
    queue = PriorityQueue()

    # do kolejki wsadzam [dystance_to_u, u, who_drove], who_drove = 'A' - Alicja, 'B' - Bob
    # najpierw sytuacja gdy Alicja jedzie pierwsza
    queue.put([0, s, 'B']) # wsadzam B ze tak jakby "wczesniej" jechal Bob wiec teraz musi Alicja jechac
    distance[s][1] = 0
    queue.put([0, s, 'A'])
    distance[s][0] = 0

    while not queue.empty():
        u = queue.get()
        who_drove = u[2]
        u = u[1]
        if who_drove == 'A':
            for elem in G[u]:
                # teraz jedzie Bob
                v = elem[0]
                # weight = elem[1] # waga {u, v}
                if distance[v][1] > distance[u][0]:
                    distance[v][1] = distance[u][0]
                    parent[v][1] = u
                    queue.put([distance[s][1], v, 'B'])
        else:
            for elem in G[u]:
                # teraz jedzie Alicja
                v = elem[0]
                weight = elem[1] # waga {u, v}
                if distance[v][0] > distance[u][1] + weight:
                    distance[v][0] = distance[u][1] + weight
                    parent[v][0] = u
                    queue.put([distance[v][0], v, 'A'])

    # Zostalo odczytac wynik i odtworzyc trase
    road = [t]
    if distance[t][0] <= distance[t][1]:
        # pierwsza prowadzi Alicja
        curr_driver = 0
    else:
        curr_driver = 1

    w = t
    while parent[t][curr_driver] != -1:
        t = parent[t][curr_driver]
        curr_driver = (curr_driver + 1) % 2
        road.append(t)

    if (curr_driver + 1) % 2 == 0:
        answer = ("Pierwsza jedzie Alicja, ktora przejedzie:", min(distance[w]))
    else:
        answer = ("Pierwszy jedzie Bob, gdzie Alicja przejedzie:", min(distance[w]))


    return answer, road[::-1]

def change_to_graph(T):
    n = len(T)
    # najpierw szukam max wierzcholka
    max_v = 0
    for i in range(n):
        max_v = max(max_v, T[i][1], T[i][0])

    G = [[] for _ in range(max_v + 1)]
    for i in range(n):
        x, y, c = T[i]
        G[x].append([y, c])
        G[y].append([x, c])  # bo zakladam ze graf jest nieskierowany

    return G

if __name__ == '__main__':
    # (x,y,d) - polaczenie z miasta x do y o dlugosci d w km
    T0 = [(0, 1, 2), (1, 2, 3), (0, 4, 5), (4,5,4), (5,3,10),(2,3,8),(3,6,1)]
    G0 = change_to_graph(T0)
    print(two_drivers(G0, 0, 6))
    T1 = [(0, 1, 100), (0, 4, 10), (1, 2, 99), (2, 3, 98), (3, 4, 1)]
    G1 = change_to_graph(T1)
    print(two_drivers(G1, 0, 4))
    T2 = [(0, 1, 10), (1, 2, 8), (1, 3, 4), (1, 4, 3), (2, 5, 2), (3, 5, 4), (4, 5, 10)]
    G2 = change_to_graph(T2)
    print(two_drivers(G2, 0, 5))
    G = [[(1, 100), (2, 100)],
         [(0, 100), (2, 1), (3, 100)],
         [(0, 100), (1, 1), (3, 100), (4, 10000)],
         [(1, 100), (2, 100)],
         [(2, 10000), (5, 1000)],
         [(4, 1000)]]
    print(two_drivers(G, 0, 5))
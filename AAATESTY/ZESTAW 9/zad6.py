# Created by Marcin "Cozoob" Kozub 13.06.2021
from queue import PriorityQueue
import random
import networkx as nx

def Marcin_two_drivers(G, s, t):
    # u i v to krotki/tablice wierzcholkow u oraz v
    def relax(u, distance_u, v, distance_v, parent, G, x):

        if distance_v > distance_u + G[x][v]:
            distance_v = distance_u + G[x][v]
            parent[u] = v
            parent[v] = x

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
            queue.put([G[s][i], i])
            distance2[i] = G[s][i]

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
    ODP2 = distance2[t]
    ODP1 = distance1[t]
    for i in range(n):
        if G[i][t] != -1:
            ODP2 = min(ODP2, distance2[i])
            ODP1 = min(ODP1, distance1[i])

    if ODP1 <= ODP2:
        flag = True
    else:
        flag = False

    # no i jeszcze odtworzyc ale da sie napewno szybciej zrobic te zadanie
    if flag is True:
        # Alicja ma jechac druga
        return "B", ODP1, parent1

    # Alicja jedzie pierwsza
    return "A", ODP2, parent2

def Rafal_shortest_for_Alice( G, s, t ):

    A = 0
    B = 1

    n = len(G)
    Q = PriorityQueue()
    inf = float( "inf" )
    parent = [ [None, None] for _ in range( n ) ]
    distance = [ [inf, inf] for _ in range( n ) ]

    Q.put( (0, A, s) )
    Q.put( (0, B, s) )
    distance[s] = [0,0]

    while not Q.empty():
        Adist, last_driver, u = Q.get()
        # print(Adist, last_driver, u)

        if last_driver == A:
            for v,d in G[u]:
                # print("--", v, d, distance[v][B], distance[v][A] + d)
                if distance[v][B] > distance[u][A]:
                    # print("+")
                    distance[v][B] = distance[u][A]
                    parent[v][B] = u
                    Q.put( (Adist, B, v) )
        else:
            for v, d in G[u]:
                # print("--", v, d, distance[v][B], distance[v][A] + d)
                if distance[v][A] > distance[u][B] + d:
                    # print("+")
                    distance[v][A] = distance[u][B] + d
                    parent[v][A] = u
                    Q.put((Adist+d, A, v))

    # print(parent)
    # print(distance)
    path = [t]
    curr_driver = None

    if distance[t][A] < distance[t][B]: curr_driver = A
    else: curr_driver = B

    w = t
    while parent[w][curr_driver] is not None:
        w = parent[w][curr_driver]
        curr_driver = (curr_driver+1)%2 #zmiana na drugiego kierowce
        path.append(w)

    return path[::-1], min(distance[t]), "A" if (curr_driver+1)%2 == 0 else "B"


# sample to jak oznaczam brak krawedzi
def list_to_matrix(G, sample):
    n = len(G)
    new_G = [[sample for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for edge in G[i]:
            u = edge[0]
            w = edge[1]
            new_G[i][u] = w

    return new_G

if __name__ == '__main__':
    # TESTY WSTEPNE

    # TEST 2; 233 alicja pierwsza
    # K = [[(2, 5106), (3, 233)], [(2, 2982), (3, 1564)], [(0, 5106), (1, 2982)], [(0, 233), (1, 1564)], [], []]
    # s = 0
    # t = 1
    # R = Rafal_shortest_for_Alice(K, s, t)
    # M = Marcin_two_drivers(list_to_matrix(K, -1), s, t)
    # print(R)
    # print(M)
    #
    # exit()


    # TEST 1
    G = [[(1, 100), (2, 100)],
         [(0, 100), (2, 1), (3, 100)],
         [(0, 100), (1, 1), (3, 100), (4, 10000)],
         [(1, 100), (2, 100)],
         [(2, 10000), (5, 1000)],
         [(4, 1000)]]
    s = 0
    t = 5

    M = Marcin_two_drivers(list_to_matrix(G, -1), s, t)
    R = Rafal_shortest_for_Alice(G, s, t)
    who_M, d_M, MM = M
    RR, d_R, who_R = R
    if who_M != who_R or d_R != d_M:
        print("BLAD!")
        print(G)
        print("MACINA WYNIK", M)
        print("RAFALA WYNIK", R)
        print("s: ", s)
        print("t: ", t)
        print()
        print(list_to_matrix(G, -1))
        exit()
    print("TEST WSTEPNY OK")

    # TESTY LOSOWE
    for i in range(30):
        a = random.randint(5, 10)
        G = nx.gnp_random_graph(a, 0.5, directed=False)

        G = nx.DiGraph([(u, v, {'weight': random.randint(1, 10000)}) for (u, v) in G.edges() if u < v])



        T = G.out_edges()
        n = G.number_of_nodes()

        # print(T, n)
        G2 = [[] for _ in range(n + 2)]
        for edge in T:
            w = G.get_edge_data(edge[0], edge[1])
            tupla1 = (edge[1], w['weight'])
            tupla2 = (edge[0], w['weight'])

            G2[edge[0]].append(tupla1)
            G2[edge[1]].append(tupla2)

        # print()
        #print(G2)

        s = 0
        t = random.randint(1, n - 1)
        new_G2 = list_to_matrix(G2, -1)
        #print(new_G2)

        M = Marcin_two_drivers(new_G2, s, t)
        R = Rafal_shortest_for_Alice(G2, s, t)
        who_M, d_M, MM = M
        RR, d_R, who_R = R

        if who_M != who_R or d_R != d_M:
            print("BLAD!")
            print(G)
            print("MACINA WYNIK", M)
            print("RAFALA WYNIK", R)
            print("s: ", s)
            print("t: ", t)
            print(G2)
            exit()

    print("LOSOWE TESTY OK")
# Created by Marcin "Cozoob" Kozub 13.06.2021
import networkx as nx
import random

from queue import PriorityQueue

def Marcin_how_many_groups(T, A, B, K):

    # sprawdzam ile wierzcholkow musze stworzyc
    n = -1
    for i in range(len(T)):
        n = max(n, T[i][0], T[i][1])

    n += 1
    inf = float("inf")
    G = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(len(T)):
        a = T[i][0]
        b = T[i][1]
        G[a][b] = T[i][2]
        G[b][a] = G[a][b]

    # u i v to krotki/tablice wierzcholkow u oraz v
    def relax(u, capacity_u, v, capacity_v, G):

        if capacity_v < capacity_u:
            capacity_v = min(capacity_u, G[u][v])

        v = [capacity_v, v]
        return v

    queue = PriorityQueue()
    # umieszczam wszystkie wierzcholki w kolejce priorytetowej
    # wraz z informacja o pojemnosc trasy do danego wierzcholka
    # [capacity of A, vertex]
    # dla wierzcholka A ustawiam umownie capacity = inf
    queue.put([inf, A])

    # nasz zbior wierzcholkow przetworzony z informacja o odleglosci do s
    capacity = [0 for _ in range(n)]
    capacity[A] = inf

    # dopoki sa wierzcholki w kolejce
    while not queue.empty():
        # wyjmuje wierzcholek u o minimalnym oszacowaniu pojemnosci
        u = queue.get()
        u = u[1]
        for v in range(n):
            if G[u][v] != -1:
                # dla kazdej krawedzi {u, v} wykonuje relaksacje
                new_v = relax(u, capacity[u], v, capacity[v], G)
                if new_v[0] > capacity[v]:
                    capacity[v] = new_v[0]
                    queue.put(new_v)

    c = capacity[B]
    answer = K // c
    if K % c != 0:
        answer += 1

    return answer

def Rafal_count_groups( E,s,t,k ):
    amount_of_v = 0
    for i in range( len(E) ): amount_of_v = max( amount_of_v, E[i][0], E[i][1] )
    amount_of_v += 1

    n = amount_of_v
    G = [ [] for _ in range(n) ]
    for i in range( len(E) ): G[ E[i][0] ].append( ( E[i][1], E[i][2] ) )

    inf = float("inf")
    lowest_edge = [0]*n
    parent = [None]*n

    Q = PriorityQueue()
    Q.put( (-inf, s) )
    lowest_edge[s] = inf

    while not Q.empty():
        cap, u = Q.get()
        cap = -cap #to przyjecie mojej dziwnej konwencji XD

        for v, d in G[u]:
            if lowest_edge[v] < min( cap, d ):
                lowest_edge[v] = min( cap, d )
                parent[v] = u
                Q.put( (-lowest_edge[v], v) )


    # print(parent, lowest_edge)
    best_cap = lowest_edge[t]
    return k//best_cap if k%best_cap == 0 else k//best_cap+1

if __name__ == '__main__':
    # TESTY WSTEPNE
    # 1 TEST
    A = 0
    B = 4
    K = 14
    E = [(0, 1, 10), (1, 2, 8), (1, 3, 4), (1, 4, 3), (2, 5, 2), (3, 5, 4), (4, 5, 10)]
    M = Marcin_how_many_groups(E, A, B, K)
    R = Rafal_count_groups(E, A, B, K)
    if M != R:
        print("BLAD!")
        print(E)
        print("MACINA WYNIK", M)
        print("RAFALA WYNIK", R)
        print("A: ", A)
        print("B: ", B)
        print("K: ", K)
        exit()
    # 2 TEST
    T0 = [(0, 1, 10), (1, 2, 8), (1, 3, 4), (1, 4, 3), (2, 5, 2), (3, 5, 4), (4, 5, 10)]
    M = Marcin_how_many_groups(T0, A, B, K)
    R = Rafal_count_groups(T0, A, B, K)
    if M != R:
        print("BLAD!")
        print(T0)
        print("MACINA WYNIK", M)
        print("RAFALA WYNIK", R)
        print("A: ", A)
        print("B: ", B)
        print("K: ", K)
        exit()

    # 3 TEST
    K = 9
    T1 = [(0, 1, 100), (0, 4, 10), (1, 2, 99), (2, 3, 98), (3, 4, 1)]
    M = Marcin_how_many_groups(T1, A, B, K)
    R = Rafal_count_groups(T1, A, B, K)
    if M != R:
        print("BLAD!")
        print(T1)
        print("MACINA WYNIK", M)
        print("RAFALA WYNIK", R)
        print("A: ", A)
        print("B: ", B)
        print("K: ", K)
        exit()

    print("TESTY WSTEPNE OK")

    exit()
    # Losowe testy
    for i in range(30):


        M = Marcin_how_many_groups(T, A, B, K)
        R = Rafal_count_groups(T, A, B, K)
        if M != R:
            print("BLAD!")
            print(T)
            print("MACINA WYNIK", M)
            print("RAFALA WYNIK", R)
            print("A: ", A)
            print("B: ", B)
            print("K: ", K)
            exit()

    print("LOSOWE TESTY OK")
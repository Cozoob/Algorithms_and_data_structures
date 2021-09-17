# Created by Marcin "Cozoob" Kozub 13.06.2021
from queue import PriorityQueue
from math import log2, inf
import networkx as nx
import random

# repr. macierzowa
def Marcin_find_path(G, s, t):

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
    visited = [False for _ in range(n)]
    while tmp != t and tmp != s and not visited[tmp]:
        #print("PETLA?M")
        answer.append(res[tmp])
        visited[tmp] = True
        tmp = parent[tmp]


    return answer


# repr. list sasiedztwa
def Rafal_Dijkstry( G, s, t ):

    n = len(G)
    Q = PriorityQueue()
    distance = [inf]*n
    done = [False]*n
    parent = [None]*n

    Q.put( (0,s) )
    distance[s]=0
    done[s]=True

    while not Q.empty():
        _,u = Q.get()
        if done[u]: continue
        done[u] = True

        for v,w in G[u]:
            w = log2(w)
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                parent[v] = w
                Q.put( ( distance[v], v ) )


    result = [t]
    u = t
    while u != s and u != None:
        print("PETLA?")
        u = parent[u]
        result.append(u)

    return result


# sample to jak oznaczam brak krawedzi
def list_to_matrix(G, sample):
    n = len(G)
    new_G = [[sample for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for edge in G[i]:
            u = edge[0]
            w = edge[1]
            new_G[i][u] = w
            new_G[u][i] = w

    return new_G


if __name__ == '__main__':

    # Losowe testy
    for i in range(30):
        a = random.randint(3,10)
        G = nx.gnp_random_graph(a, 0.5, directed=False)

        DAG = nx.DiGraph([(u, v, {'weight': random.randint(0, 10)}) for (u, v) in G.edges() if u < v])

        #nx.is_directed_acyclic_graph(DAG)

        T = DAG.out_edges()
        n = DAG.number_of_nodes()

        #print(T, n)
        G2 = [[] for _ in range(n + 2)]
        for edge in T:
            w = DAG.get_edge_data(edge[0],edge[1])
            tupla = (edge[1], w['weight'])

            G2[edge[0]].append(tupla)

        #print()
        #print(G2)

        if n - 2 <= 0:
            s = 0
            t = 1
        else:
            s = random.randint(0, n - 1)
            t = random.randint(0, n -1)

        R = Rafal_Dijkstry(G2, s, t)
        new_G = list_to_matrix(G2, -1)
        #print(n)
       # print(new_G)
        M = Marcin_find_path(new_G, s, t)

        if M != R:
            print("BLAD!")
            print(G2)
            print("MACINA WYNIK" , M)
            print("RAFALA WYNIK", R)
            print("s: ", s)
            print("t: ", t)
            exit()

    print("LOSOWE TESTY OK")
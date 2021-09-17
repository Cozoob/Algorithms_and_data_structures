# Created by Marcin "Cozoob" Kozub 13.06.2021
import networkx as nx
import random

# repr. macierzowa, gdzie inf to brak krawedzi
def Marcin_find_shortest_path(G, s):
    n = len(G)
    inf = float("inf")
    distance = [inf for _ in range(n)]
    visited = [False for _ in range(n)]

    def visit_top_sort(u):
        nonlocal n, G, visited, stack, inf

        visited[u] = True
        for v in range(n):

            if G[u][v] != inf and visited[v] is False:
                visit_top_sort(v)
        stack.append(u)



    stack = []
    for v in range(n):
        if not visited[v]:
            visit_top_sort(v)

    stack = stack[::-1]
    distance[s] = 0

    for u in stack:
        for v in range(n): # t: byloby O(V + E) na listach sasiedztwa ale ze repr. macierzeowa to O(V^2) niestety
            if G[u][v] != inf and distance[v] > distance[u] + G[u][v]:
                distance[v] = distance[u] + G[u][v]

    return distance


# repr. list sasiedztwa
def Rafal_shortest_paths( G, s ):

    n = len(G)
    visited = [False]*n
    top_sorted = []

    def top_dfs_visit( u ):
        nonlocal G, top_sorted, visited

        visited[u] = True

        for v, _ in G[u]:
            if not visited[v]:
                top_dfs_visit(v)

        top_sorted.append(u)


    top_dfs_visit(s)

    top_sorted = top_sorted[::-1]

    inf = float("inf")
    distance = [inf]*n
    distance[s] = 0

    for i in range( len(top_sorted) ):
        u = top_sorted[i]
        for v, cost in G[u]:
            distance[v] = min( distance[v], distance[u]+cost )

    return distance



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

    # Losowe testy
    for i in range(30):
        a = random.randint(3,10)
        G = nx.gnp_random_graph(a, 0.5, directed=True)

        DAG = nx.DiGraph([(u, v, {'weight': random.randint(-10, 10)}) for (u, v) in G.edges() if u < v])

        nx.is_directed_acyclic_graph(DAG)

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
        else:
            s = random.randint(0, n - 1)

        R = Rafal_shortest_paths(G2, s)
        new_G = list_to_matrix(G2, float("inf"))
        #print(n)
       # print(new_G)
        M = Marcin_find_shortest_path(new_G, s)

        if M != R:
            print("BLAD!")
            print(G2)
            print("MACINA WYNIK" , M)
            print("RAFALA WYNIK", R)
            exit()

    print("LOSOWE TESTY OK")
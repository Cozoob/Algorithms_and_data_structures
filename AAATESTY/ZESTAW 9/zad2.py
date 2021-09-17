# Created by Marcin "Cozoob" Kozub 13.06.2021
import networkx as nx
import random


# reprezentacja list sasiedztwa
def Marcin_the_good_start(G):
    n = len(G)
    visited = [False for _ in range(n)]

    # flaga pomaga mi w dodawaniu wierzcholkow do sortowania
    def visit(u, flag):
        nonlocal n, G, visited, stack

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                visit(v, flag)
        if flag:
            stack.append(u)

    stack = []
    for v in range(n):
        if not visited[v]:
            visit(v, True)

    stack = stack[::-1]
    visited = [False for _ in range(n)]
    visit(stack[0], False)
    for i in range(n):
        if visited[i] is False:
            return False

    return True


def Rafal_good_beginnig( G ):
    def top_DFS_Visit( u ):
        nonlocal visited, G, topological_sorted

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                top_DFS_Visit(v)

        topological_sorted.append(u)


    def DFS_Visit( u ):
        nonlocal visited, G

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS_Visit( v )


    n = len(G)
    visited = [False]*n
    topological_sorted = []

    for u in range( n ):
        if not visited[u]:
            top_DFS_Visit(u)

    topological_sorted = topological_sorted[::-1]

    for i in range(n): visited[i]=False
    DFS_Visit( topological_sorted[-1] )

    for u in range(n):
        if not visited[u]: return False

    return topological_sorted[-1]


if __name__ == '__main__':


    # Losowe testy
    for i in range(30):
        a = random.randint(2,10)
        G = nx.gnp_random_graph(a, 0.5, directed=True)

        DG = nx.DiGraph([(u, v, {'weight': random.randint(-10, 10)}) for (u, v) in G.edges() if u < v])

        nx.is_directed(DG)

        T = DG.out_edges()
        n = DG.number_of_nodes()

        #print(T, n)
        G2 = [[] for _ in range(n + 2)]
        for edge in T:
            G2[edge[0]].append(edge[1])

        #print()
        #print(G2)

        M = Marcin_the_good_start(G2)
        R = Rafal_good_beginnig(G2)
        if M != R:
            print("BLAD!")
            print(G2)
            print("MACINA WYNIK" , M)
            print("RAFALA WYNIK", R)
            exit()

    print("LOSOWE TESTY OK")
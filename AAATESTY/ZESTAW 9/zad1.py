# Zadanie 1. (ścieżka Hamiltona w DAGu) ZESTAW 9
import networkx as nx
import random
# reprezentacja list sasiedztwa
def Marcin_is_Hamilton_Path(G):
    n = len(G)
    visited = [False for _ in range(n)] # t: O(n), m: O(n), n = V

    def visit(u, flag):
        nonlocal visited, stack, n, G

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                visit(v, flag)
                if flag is False:
                    break

        if flag:
            stack.append(u)


    stack = []
    for v in range(n): # sortowanie topologiczne t: O(V + E), m: O(n), n = V
        if not visited[v]:
            visit(v, True)

    stack = stack[::-1]
    visited = [False for _ in range(n)] # t: O(n), m: O(n), n = V
    visit(stack[0], False) # t: O(V + E), m: O(n), n = V


    for i in range(n): # t: O(n), n = V
        if visited[i] is False:
            return False

    return True

def Rafal_Hamilton(G):
    n = len(G)
    visited = [False] * n
    top_sorted = []

    def top_dfs_visit(u):
        nonlocal G, visited, top_sorted

        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                top_dfs_visit(v)

        top_sorted.append(u)

    for u in range( n ):
        if not visited[u]:
            top_dfs_visit(u)

    top_sorted = top_sorted[::-1]

    for i in range( n-1 ):
        if not top_sorted[i+1] in G[ top_sorted[i] ]:
            return False

    return True



if __name__ == '__main__':
    # Testy wstepne
    # True
    G0 = [
        [1,2],
        [2],
        [3],
        []
    ]

    if(Marcin_is_Hamilton_Path(G0) != Rafal_Hamilton(G0)):
        print("BLAD! TEST WSTEPNY")
        exit()

    # False (G0 tylko ze brak krawedzi z 0 do 1)
    G1 = [
        [2],
        [2],
        [3],
        []
    ]
    if (Marcin_is_Hamilton_Path(G1) != Rafal_Hamilton(G1)):
        print("BLAD! TEST WSTEPNY")
        exit()
    else:
        print("TESTY WSTEPNE OK")

    # Losowe testy
    for i in range(30):
        a = random.randint(2,10)
        G = nx.gnp_random_graph(a, 0.5, directed=True)

        DAG = nx.DiGraph([(u, v, {'weight': random.randint(-10, 10)}) for (u, v) in G.edges() if u < v])

        nx.is_directed_acyclic_graph(DAG)

        T = DAG.out_edges()
        n = DAG.number_of_nodes()

        #print(T, n)
        G2 = [[] for _ in range(n + 2)]
        for edge in T:
            G2[edge[0]].append(edge[1])

        #print()
        #print(G2)

        M = Marcin_is_Hamilton_Path(G2)
        R = Rafal_Hamilton(G2)
        if M != R:
            print("BLAD!")
            print(G2)
            print("MACINA WYNIK" , M)
            print("RAFALA WYNIK", R)
            exit()

    print("LOSOWE TESTY OK")
# Created by Marcin "Cozoob" Kozub 30.05.2021

# Zadanie 2. (dobry początek) Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli
# każdy inny wierzchołek można osiągnąć scieżką skierowaną wychodzącą z v. Proszę podać algorytm, który
# stwierdza czy dany graf zawiera dobry początek.

# Pomysl: Zwykle sortowanie topologiczne i puszczenie DFS z pierwszego wierzcholka i sprawdzenie czy odwiedzilismy
# wszystkie wierzcholki.

# Zlozonosc: O(V + E)

# reprezentacja list sasiedztwa
def good_start(G):
    n = len(G)
    visited = [False for _ in range(n)]

    def topological_sort(s):
        nonlocal visited, stack, n, G

        visited[s] = True
        for v in G[s]:
            if not visited[v]:
                topological_sort(v)

        stack.append(s)

    def dfs_visit(u):
        nonlocal visited, G, n

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(v)


    stack = []
    for v in range(n):
        if not visited[v]:
            topological_sort(v)

    stack = stack[::-1]
    visited = [False for _ in range(n)]
    dfs_visit(stack[0])

    for i in range(n):
        if visited[i] == False:
            return False
    return True


if __name__ == '__main__':
    G = [
        [],
        [],
        [3],
        [1],
        [1, 0],
        [2,0]
    ]
    print(good_start(G))
    G2 = [
        [1, 2],
        [3],
        [],
        []
    ]
    print(good_start(G2))
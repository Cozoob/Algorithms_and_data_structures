# Created by Marcin "Cozoob" Kozub at 08.05.2021 16:36
# Implementacja DFS dla grafu w postaci list sąsiedztwa

# repr. listowa O(V + E), repr. macierzowa O(V^2)
def dfs(G, s):
    n = len(G)
    visited = [False for _ in range(n)]

    def dfs_visit(u):
        nonlocal G, visited

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(v)

    dfs_visit(s)
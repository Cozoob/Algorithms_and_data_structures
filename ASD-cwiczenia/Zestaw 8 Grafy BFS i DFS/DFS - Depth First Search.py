# Created by Marcin "Cozoob" Kozub at 08.05.2021 16:36
# Implementacja DFS dla grafu w postaci list sąsiedztwa
# O(V + E)
# dla repr. macierzowej O(V^2)

def dfs(graph, s):
    visited = [False]*len(graph)

    def dfs_visit(u):
        nonlocal graph, visited

        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs_visit(v)

    dfs_visit(s)

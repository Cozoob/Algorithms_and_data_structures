from queue import Queue
# Created by Marcin "Cozoob" Kozub at 08.05.2021 16:32
# Implementacja BFS dla grafu w postaci list sąsiedztwa
# O(V + E)
# dla repr. macierzowej O(V^2)

def bfs(graph, s):
    queue = Queue()
    visited = [False] * len(graph)

    queue.put(s)
    visited[s] = True

    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.put(v)
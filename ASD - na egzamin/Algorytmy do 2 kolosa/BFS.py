from queue import Queue
# Created by Marcin "Cozoob" Kozub at 08.05.2021 16:32
# Implementacja BFS dla grafu w postaci list sąsiedztwa

# repr. listowa O(V + E), repr. macierzowa O(V^2)
def bfs(G, s):
    n = len(G)
    queue = Queue()
    visited = [False for _ in range(n)]

    queue.put(s)
    visited[s] = True

    while not queue.empty():
        u = queue.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                queue.put(v)
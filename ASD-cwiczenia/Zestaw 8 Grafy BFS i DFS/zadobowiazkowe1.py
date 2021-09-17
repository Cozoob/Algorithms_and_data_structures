# Created by Marcin "Cozoob" Kozub at 09.05.2021 20:47
from queue import Queue

# Prosze zaimplementować algorytm sprawdzający czy graf jest dwudzielny.

# Pomysł: Wystarczy wykorzystac algorytm BFS, gdzie na poczatku wszystkie wierzcholki
# są pokolorwane na kolor neutralny (u nas None) zaś przechodzac z wierzchołka v do u
# bedziemy wierzcholek v kolorowac na czerwono (u nas reprezentacyjnie 0) a u na czarno
# (u nas reprezentacyjnie 1). Jesli uda nam sie pokolorwac wszystkie wierzcholki
# na czarno lub czerwono to mamy graf dwudzielny.
# Wykorzystuje reprezentacje list sasiedztwa grafu.

def color_vertices_BFS(graph):
    n = len(graph)
    queue = Queue()
    visited = [None] * n

    # zaczynam z dowolonego wierzcholka; niech zawsze to bedzie 0
    queue.put(0)
    visited[0] = 0

    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            # jesli wierzcholki sa pokolorowane na te same kolory
            # to graf nie jest dwudzielny
            if visited[v] == visited[u]:
                return False
            elif visited[v] == None:
                queue.put(v)
                if visited[u] == 0:
                    visited[v] = 1
                else:
                    visited[v] = 0
    # jesli przejde i pokoloruje tak caly graf tzn ze mam graf dwudzielny
    return True

if __name__ == '__main__':
    g1 = [
        [1,3,5],
        [0,2],
        [1,3],
        [0,2],
        [5,6],
        [4,0],
        [4]
    ]
    print(color_vertices_BFS(g1))
    # True

    # g2 powstaje poprzez polaczenie wierzcholka 0 z 2 przez co zwraca False
    g2 = [
        [1, 3, 5, 2],
        [0, 2],
        [1, 3, 0],
        [0, 2],
        [5, 6],
        [4, 0],
        [4]
    ]
    print(color_vertices_BFS(g2))
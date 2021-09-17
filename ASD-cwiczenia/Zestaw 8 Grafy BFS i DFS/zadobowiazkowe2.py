# Created by Marcin "Cozoob" Kozub at 09.05.2021 21:14
from queue import Queue

# Zad. 1. Dany jest spójny graf nieskierowany G = (V,E). Proszę
# zaproponować algorytm, który znajdzie taką kolejność usuwania
# wierzchołków, która powoduje że w trakcie usuwania graf nigdy nie
# przestaje być spójny (usunięcie wierzchołka usuwa, oczywiście, wszystkie
# dotykające go krawędzie).

# Pomysł: Wykonuje BFS gdzie zapisuje w tablicy visited odleglosc od wierzcholka startowego
# i po zapisaniu odleglosci znajduje ten krory znajduje sie najdalej od tego wierzcholka
# dzieki temu moge znalezc wierzcholek ktory znajduje sie na "koncu grafu" (bo znajduje sie na "srednicy grafu").
# Nastepnie znow wykonuje BFS dla znalezionego wierzcholka i teraz usuwam wierzcholki ktore sa
# najdalej od znalezionego wierzcholka.
# Krawedz to odleglosc 1.
# Graf reprezentuje poprzez listy sasiedztwa.

def delete_vertices_BFS(graph):
    n = len(graph)
    queue = Queue()
    # -1 oznacza ze punkt nie byl odwiedzony
    visited = [-1] * n

    # wkladam dowolny wierzcholek; niech u mnie zawsze to bedzie 0
    queue.put(0)
    visited[0] = 0

    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if visited[v] == -1:
                visited[v] = visited[u] + 1
                queue.put(v)

    # znajduje wierzcholek ktory jest najdalej
    max_val = visited[0]
    s = 0
    for i in range(n):
        if max_val < visited[i]:
            max_val = visited[i]
            s = i
    # i teraz wykonuje bfs dla wierzcholka s odrazu zapisuja wierzcholki pod odpwiednie odleglosci
    visited = [-1] * n
    queue.put(s)
    visited[s] = 0
    # w talblicy d zapisuje wierzcholki z danymi odleglosciami do wierzcholka s
    d = [[] for _ in range(n)]
    d[0] = [s]

    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if visited[v] == -1:
                visited[v] = visited[u] + 1
                queue.put(v)
                d[visited[v]].append(v)
    # znajduje najwieksza odleglosc
    max_val = max(visited)
    # i wypisuje wszystko co znajduje sie w d[max_val] i tak az dotre do d[0] ktore bedzie puste
    while max_val >= 0:
        for elem in d[max_val]:
            print(elem, end=' ')
        max_val -= 1

    print()

    return visited, max_val, s, d

if __name__ == '__main__':
    g1 = [
        [1,3],
        [0,2,4],
        [0,1,3,4],
        [0,2,4],
        [1,2,3]
    ]
    print(delete_vertices_BFS(g1))

    g2 = [
        [1],
        [0,2,3],
        [1],
        [1,4],
        [3,5,6],
        [4],
        [4]
    ]
    print(delete_vertices_BFS(g2))
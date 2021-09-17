# Created by Marcin "Cozoob" Kozub 13.05.2021
# (BFS i najkrótsze sciezki) Prosze zaimplementowac algorytm BFS tak, zeby znajdował
# najkrótsze sciezki w grafie i nastepnie, zeby dało sie wypisac najkrotsza sciezke z zadanego punktu startowego
# do wskazanego wierzchołka.
from collections import deque

# Pomysł: Odpalam BFS na wierzcholku v i w tablicy visited zapisuje czas przejscia przez dany wierzcholek.
# Jesli napotkalem wierzcholek u to koncze BFS.
# Nastepnie jesli chce znalezc najkrotsza sciezke z v do u to z u ide do w wtw, gdy visited[u] - 1 = visited[w]

def find_path(graph, s, t):
    n = len(graph)
    # -1 oznacza ze wierzcholek nieodwiedzony
    visited = [-1] * n
    queue = deque()

    queue.append(s)
    visited[s] = 0
    flag = False
    counter = 0
    while len(queue) != 0:
        v = queue.pop()
        for u in graph[v]:
            if visited[u] == -1 or visited[u] >= visited[v] + 1:
                # Jesli istnieja dwie najkrotsze sciezki to zapisuje te informacje w counter
                if visited[t] != -1 and visited[t] == visited[v] + 1:
                    counter += 1
                    queue.append(u)
                else:
                    counter = 1
                    visited[u] = visited[v] + 1
                    queue.append(u)
            # to oznacza ze doszedlem BFS z wierzcholka s do wierzcholka t


    #teraz szukam rozwiazania czyli ide z wierzcholka t do s
    res = []
    while s != t:
        res.append(t)
        for w in graph[t]:
            if visited[w] != -1 and visited[w] == visited[t] - 1:
                t = w
                break
    res.append(s)
    # czyli jesli istnieja dwie takie najkrotsze sciezki z s do t nie ma opcji zeby usunac tylko
    # jedna krawedz i wydluzyc najkrotsze sciezkie w grafie G

    return res, counter

if __name__ == '__main__':
    g0 = [
        [1],
        [0,2,4],
        [1,3,5],
        [2,4],
        [1,3,6],
        [2,7],
        [4,7],
        [6,5]
    ]
    print(find_path(g0, 7, 2))
    G = [[1, 2],
         [0, 2],
         [0, 1]]
    print(find_path(G, 0, 2))
    G = [
        [1, 4],
        [0 ,2],
        [1, 3],
        [2, 5],
        [0, 5],
        [4, 3]
    ]
    print(find_path(G, 0, 3))
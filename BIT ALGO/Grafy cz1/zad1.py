from queue import Queue
# Created by Marcin "Cozoob" Kozub at 08.05.2021 16:46
# Napisz algorytm sprwadzający, czy graf nieskierowany posiada cykl.

# Wykonujemy BFS i po prostu sprawdzamy czy idac dalej nie trafiamy
# na wierzcholek juz odwiedzony jednoczesnie nie bedacy naszym rodzicem.

def find_cycle_bfs(graph, s):
    n = len(graph)
    queue = Queue()
    visited = [False]*n
    parent = [None]*n

    queue.put(s)
    visited[s] = True


    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if visited[v]:
                if parent[v] != u:
                    return True
            else:
                visited[v] = True
                parent[v] = u
                queue.put(v)

    return False

if __name__ == '__main__':
    # g1 ma cykl 1, 2, 3, 4, 1
    # g1 = [
    #     [1],
    #     [4, 2],
    #     [1, 3],
    #     [2, 4],
    #     [1, 3]
    # ]
    # print(find_cycle_bfs(g1,0))

    # g2 nie ma cyklu
    g2 = [
        [1],
        [2],
        [3, 4],
        [],
        [5],
        [],
        [7],
        [8],
        []
    ]
    print(find_cycle_bfs(g2,0))
    # g3 to stworzenie cyklu w g2 ktory ma postac 1,2,6,7,8,1
    # poprzez polaczenie wierzcholkow 8 i 1
    g3 = [
        [1],
        [2, 8],
        [3, 4, 5],
        [],
        [5],
        [],
        [7],
        [8],
        [1]
    ]
    print(find_cycle_bfs(g3,0))
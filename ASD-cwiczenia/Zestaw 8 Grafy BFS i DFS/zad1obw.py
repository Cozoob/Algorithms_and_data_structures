# Created by Marcin "Cozoob" Kozub 13.05.2021
# Zadanie 1. (Pause) Znany operator telefonii komórkowej Pause postanowił zakonczyc działalnosc w
# Polsce. Jednym z głównych elementów całej procedury jest wyłaczenie wszystkich stacji nadawczych (które
# tworza spójny graf połaczen). Ze wzgledów technologicznych urzadzenia nalezy wyłaczac pojedynczo a operatorowi
# dodatkowo zalezy na tym, by podczas całego procesu wszyscy abonenci znajdujacy sie w zasiegu
# działajacych stacji mogli sie ze soba łaczyc (czyli by graf pozostał spójny). Prosze zaproponowac algorytm
# podajacy kolejnosc wyłaczania stacji.
from queue import PriorityQueue
# Pomysł: Odpalam BFS z dowolnego wierzcholka i usuwam wierzchołki najdalsze.


def pause_bfs(graph):
    n = len(graph)
    # -1 oznacza ze wierzcholek nie zostal odwiedzony
    visited = [-1] * n
    queue = PriorityQueue()
    # w kolejse priorytetowej res zapisuje w krotkach
    # ktore krawedzi w jakiej kolejnosc mam usuwac zeby
    # nierospojnic graf
    res = PriorityQueue()

    # zaczynam z dowolnego wierzcholka
    s = 2
    queue.put(s)
    res.put((n, s))
    visited[s] = n

    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if visited[v] == -1:
                visited[v] = visited[u] - 1
                queue.put(v)
                res.put((visited[v], v))
    # wypisuje ktore wierzcholki mam usunac w odp kolejnosci
    while not res.empty():
        v = res.get()
        print(v[1], end=' ')
    print(end='\n')

    return visited




if __name__ == '__main__':
    g1 = [
        [1],
        [0, 2, 3],
        [1, 3],
        [1, 2, 4],
        [3, 5, 6, 7],
        [4],
        [4],
        [4, 8],
        [7]
    ]
    print(pause_bfs(g1))
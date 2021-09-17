from queue import Queue
# Created by Marcin "Cozoob" Kozub at 09.05.2021 14:48
# Mamy mapę miasteczka, w którym są domy i sklepy.
# Na mapie są również drogi (każda długości 1), które łączą dom z domem,
# albo dom ze sklepem. Naszym zadaniem jest, dla każdego domu, znaleźć odległość do najbliższego sklepu.

# Uzyje BFS dla kazdego sklepu, tylko na poczatku wrzuce wszystkie sklepy jakie mam do kolejki

def find_path_BFS(graph, stores):
    n = len(graph)
    queue = Queue()
    # w tablicy d zapisuje wyniki odleglosci do najbliszego sklepu
    # -1 oznacza ze dany wierzcholek nie byl odwiedzany
    d = [-1] * n

    # wsadzam wszystkie sklepy do kolejki i zmieniam ich odleglosc na 0
    for s in stores:
        queue.put(s)
    for s in stores:
        d[s] = 0

    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if d[v] == -1:
                d[v] = d[u] + 1
                queue.put(v)

    return d



if __name__ == '__main__':
    g1 = [
        [1],
        [0,2,3],
        [1,3,4,18],
        [1,2,4,5,6],
        [2,3,5,12],
        [3,7,8,4],
        [3,7,10],
        [6,5,9],
        [5,9,13],
        [7,8,14],
        [6,11],
        [10],
        [18,4,13],
        [12,8,14],
        [9,13,15],
        [14,16],
        [15,17],
        [16],
        [2,12]
    ]
    stores = [6, 12, 16]
    print(find_path_BFS(g1, stores))
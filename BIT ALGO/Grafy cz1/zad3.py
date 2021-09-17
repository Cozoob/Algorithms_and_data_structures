# Created by Marcin "Cozoob" Kozub at 08.05.2021 18:08
from queue import Queue

# Dana jest dwuwymiarowa tablica N x N, w której każda komórka ma wartość “W” - reprezentującą wodę lub “L” - ląd.
# Grupę komórek wody połączonych ze sobą brzegami nazywamy jeziorem.
# 1. Policz, ile jezior jest w tablicy.
# 2. Policz, ile komórek zawiera największe jezioro.
# 3. Znajdź najkrótszą ścieżkę między tymi punktami. Wypisz po kolei indeksy pól w tej ścieżce.

def find_path_bfs(graph, x, y):
    n = len(graph)
    m = len(graph[0])
    queue = Queue()
    visited = [[False for _ in range(m)] for _ in range(n)]
    # w counterze zliczam odleglosc do punktu 0,0 wykonujac bfs
    counter = [[-1 for _ in range(m)] for _ in range(n)]
    counter[0][0] = 0


    queue.put((x, y))
    visited[x][y] = True

    while not queue.empty():
        u = queue.get()
        x, y = u[0], u[1]
        # mozemy isc w prawo
        if y + 1 != n and visited[x][y + 1] == False:
            visited[x][y + 1] = True
            if graph[x][y + 1] == "L":
                counter[x][y + 1] = counter[x][y] + 1
                queue.put((x, y + 1))
        # mozemy isc w gore
        if x > 0 and visited[x - 1][y] == False:
            visited[x - 1][y] = True
            if graph[x - 1][y] == "L":
                counter[x - 1][y] = counter[x][y] + 1
                queue.put((x - 1, y))
        # mozemy isc w lewo
        if y > 0 and visited[x][y - 1] == False:
            visited[x][y - 1] = True
            if graph[x][y - 1] == "L":
                counter[x][y - 1] = counter[x][y] + 1
                queue.put((x, y - 1))
        # mozemy isc w dol
        if x + 1 != n and visited[x + 1][y] == False:
            visited[x + 1][y] = True
            if graph[x + 1][y] == "L":
                counter[x + 1][y] = counter[x][y] + 1
                queue.put((x + 1, y))

    # teraz wystarczy odtworzyc dana droge
    def rec_print(counter, x, y):
        if x == 0 and y == 0:
            return
        # a, b to indeksy do ktorych ide nastepnym razem
        a = x
        b = y
        min_val = counter[x][y]
        # moze w prawo
        if y + 1 != n and min_val > counter[x][y + 1] and counter[x][y + 1] != -1:
            min_val = counter[x][y + 1]
            b = y + 1
        if x + 1 != n and min_val > counter[x + 1][y] and counter[x + 1][y] != - 1:
            a = x + 1
            min_val = counter[x + 1][y]
        if y > 0 and min_val > counter[x][y - 1] and counter[x][y - 1] != - 1:
            b = y - 1
            min_val = counter[x][y - 1]
        if x > 0 and min_val > counter[x - 1][y] and counter[x - 1][y] != -1:
            a = x - 1
            min_val = counter[x - 1][y]
        # to samo rekurencyjnie sprawdzam dla a, b
        rec_print(counter, a, b)
        print(a, b)

    rec_print(counter, n - 1, n - 1)

    return counter

def count_lakes_dfs(graph, x, y):
    n = len(graph)
    visited = [[False for _ in range(n)] for _ in range(n)]
    parent = [[None for _ in range(n)] for _ in range(n)]


    def dfs_visit(x, y):
        nonlocal visited, graph, parent

        visited[x][y] = True
        if x + 1 != n and visited[x + 1][y] == False:






def printarr(arr):
    for elem in arr:
        print(elem)


if __name__ == '__main__':
    T = [
        ["L", "W", "L", "L", "L", "L", "L", "L"],
        ["L", "W", "L", "W", "W", "L", "L", "L"],
        ["L", "L", "L", "W", "W", "L", "W", "L"],
        ["L", "W", "W", "W", "W", "L", "W", "L"],
        ["L", "L", "W", "W", "L", "L", "L", "L"],
        ["L", "W", "L", "L", "L", "L", "W", "W"],
        ["W", "W", "L", "W", "W", "L", "W", "L"],
        ["L", "L", "L", "W", "L", "L", "L", "L"]
    ]
    # res = find_path_bfs(T, 0, 0)
    # printarr(res)
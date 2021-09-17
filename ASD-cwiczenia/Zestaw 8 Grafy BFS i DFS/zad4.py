# Created by Marcin "Cozoob" Kozub 13.05.2021
# (malejące krawędzie) Dany jest graf G = (V, E), gdzie każda krawędź ma wagę ze zbioru
# {1, . . . , ∣E∣} (wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dla danych wierzchołków
# x i y sprawdza, czy istnieje ścieżka z x do y, w której przechodzimy po krawędziach o coraz mniejszych wagach.

# Pomysł: Zapisac graf w reprezentacji macierzowej gdzie 0 oznacza brak krawedzi, a dowolny x > 0 ozn.
# ze krawedzi miedzy wierzcholkami istnieje i ma wage x. Odpalamy troche zmodyfikowanego DFS'a zeby nam
# sprawdzil czy mozemy przejsc po krawedziach o coraz mniejszych wagach z x do y.
# No nawet jesli bysmy dostali osobna tablice z wagami miedzy krawedziami to nie ma znaczenia w zlozonosci czasowej...

def find_path(graph, x, y):
    n = len(graph)
    visited = [False] * n
    flag = False
    latest_edge = float("inf")

    def dfs_visit(u, latest_edge):
        nonlocal graph, visited, y, flag

        visited[u] = True
        for v in range(n):
            if flag:
                break
            if graph[u][v] != 0 and visited[v] == False and latest_edge > graph[u][v]:
                if v == y:
                    flag = True
                    break
                dfs_visit(v, graph[u][v])


    # odpalamy DFS'a z wierzcholka x i przechodzimy do wierzcholkow
    # ktore nie byly odwiedzone i krawedzie maja mniejsza wage
    dfs_visit(x, latest_edge)
    return flag



if __name__ == '__main__':
    g0 = [
        [0, 1, 0, 0, 0, 0, 0],
        [1, 0, 2, 3, 0, 10, 0],
        [0, 2, 0, 0, 0, 11, 0],
        [0, 3, 0, 0, 5, 0, 0],
        [0, 0, 0, 5, 0, 4, 0],
        [0, 0, 11, 0, 4, 0, 6],
        [0, 0, 0, 0, 0, 6, 0]
    ]
    # z 1 do 5 True
    print(find_path(g0, 1, 5))
    # z 5 do 1 True
    print(find_path(g0, 5, 1))
    # z 6 do 3 False
    print(find_path(g0, 6, 3))
    # z 4 do 0 True
    print(find_path(g0, 4, 0))
    # z 4 do 2 True
    print(find_path(g0, 4, 2))
    # z 6 do 0 False
    print(find_path(g0, 6, 0))
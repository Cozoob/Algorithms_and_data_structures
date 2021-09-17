# Created by Marcin "Cozoob" Kozub 13.05.2021
# Zaimplementuj:
# Policzyc liczbe spójnych składowych w grafie skierowanym.

# Algorytm z wykladu
# Algorytm: 1. Wykonaj DFS dla grafu, zapisujac w wierzcholkach czas przetworzenia.
# 2. Odwróć kolejnosc krawedzi
# 3. Wykonaj DFS drugi raz (w kolejnosci malejacych czasow).

def dfs(graph):
    n = len(graph)
    visited = [-1] * n
    counter = 0

    def dfs_visit(u, time):
        nonlocal graph, visited, counter

        visited[u] = time
        for v in range(n):
            if graph[u][v] == 1 and visited[v] == -1:
                dfs_visit(v, time + 1)
            # jesli nastepny sasiad byl odwiedzony i jego czas przetworzenia
            # jest mniejszy niz nasz to mamy +1 silna spojna skladowa
            if graph[u][v] == 1 and visited[v] > 0 and visited[v] < visited[u]:
                counter += 1

    dfs_visit(0, 1)
    return visited, counter

if __name__ == '__main__':
    # jedna silna spojna skladowa: 1-2-3
    g1 = [
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]
    ]
    print(dfs(g1))
    # trzy silne spojne skladowe: 1-2-3-4, 6-7-8, 9-10-11
    g2 = [
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    ]
    print(dfs(g2))
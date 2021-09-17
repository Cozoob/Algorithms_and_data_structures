# Created by Marcin "Cozoob" Kozub at 09.05.2021 15:54
# Dostajemy na wejściu listę krawędzi drzewa (niekoniecznie binarnego!)
# oraz wyróżniony wierzchołek - korzeń. Każdy wierzchołek tworzy swoje własne poddrzewo.
# Dla każdego wierzchołka, wyznacz ilość wierzchołków w jego poddrzewie.

def count_vertices_DFS(graph, s):
    n = len(graph)
    # w tablicy res zapisuje ilosc wierzcholkow w poddrzewie ktorego korzen to wierzcholek o danym indeksie
    res = [0] * n
    visited = [False] * n

    def DFS_visit(u):
        nonlocal graph, res

        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                res[v] = DFS_visit(v) + 1

        # zliczam ile wierzcholkow pod soba mam
        tmp = 0
        for v in graph[u]:
            tmp += res[v]

        return tmp

    res[s] = DFS_visit(s) + 1

    return res

if __name__ == '__main__':
    g1 = [
        [1,8],
        [0,2],
        [1,3,7],
        [2,4,5],
        [3],
        [3],
        [7],
        [6,2],
        [0,9],
        [8,10,11],
        [9],
        [9,12],
        [11,13],
        [12]
    ]
    print(count_vertices_DFS(g1, 0))
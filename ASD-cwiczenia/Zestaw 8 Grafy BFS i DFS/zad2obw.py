# Created by Marcin "Cozoob" Kozub 13.05.2021
# Dany jest graf nieskierowany G zawierajacy n wierzchołków. Zaproponuj
# algorytm, który stwierdza czy w G istnieje cykl składajacy sie z dokładnie 4 wierzchołków. Zakładamy, ze
# graf reprezentowany jest przez macierz sasiedztwa A.

# Pomysł: Korzystam z DFS za kazdym razem sprawdzajac czy saidziedzi krawedzi e byli odwiedzeni juz (takie krawedzie
# ktore nie sa rodzicem krawedzi e), jesli byl juz odwiedzony to sprawdzam czy zachodzi tam cykl dlugosci 4.

def find_cycle(graph):
    n = len(graph)
    # w tablicy visited -1 ozn wierzcholek nieodwiedzony
    visited = [-1] * n
    # w talblicy parent zapisuje rodzicow wierzcholkow
    parent = [-1] * n
    # flag pomoze mi wyjsc z rekurencji
    flag = False

    def dfs_visit(u, time):
        nonlocal graph, visited, parent, flag

        visited[u] = time
        for v in range(n):
            if graph[u][v] == 1 and visited[v] == -1:
                parent[v] = u
                dfs_visit(v, time + 1)
            # jesli zas zostal juz odwiedzony i v nie jest rodzicem wierzcholka u
            # to sprawdzam czy z u do v tworzy sie cykl dlugosci 4
            if graph[u][v] == 1 and visited != -1 and parent[u] != v:
                counter = 0
                x = u
                while x != v:
                    counter += 1
                    x = parent[x]
                    if counter > 4:
                        break

                if counter == 4:
                    flag = True


    dfs_visit(0, 1)
    return flag





if __name__ == '__main__':
    # postac macierz sasiedztwa
    # tak istnieje taki cykl
    g1 = [
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    ]
    print(find_cycle(g1))
    # nie istnieje taki cykl
    g2 = [
        [0, 1, 0, 0],
        [1, 0, 1, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 0]
    ]
    print(find_cycle(g2))
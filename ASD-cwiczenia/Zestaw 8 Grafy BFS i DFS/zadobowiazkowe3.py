# Created by Marcin "Cozoob" Kozub at 09.05.2021 22:03

# Zad. 2. Proszę podać jak najszybszy algorytm, który znajduje w grafie
# cykl długości dokładnie 4 (trywialny algorytm ma złożoność O(n^4), gdzie
# n to liczba wierzchołków---chodzi o rozwiązanie szybsze).
# PS. W zadaniu 2 chodzi o reprezentację grafu przez macierz sąsiedztwa

# Pomysł: Dla kazdego wierzchołka w grafie wykonuje DFS, sprawdzajac czy moge zbudowac cykl dlugosci 4
# Zlozonosc czasowa n^3, gdzie n to ilosc wierzcholkow

def find_cycle_DFS(graph):
    n = len(graph)
    # sprawdzam dla kazdego wierzcholka w grafie
    for i in range(n):
        visited = [[False for _ in range(n)] for _ in range(n)]
        # flag pomaga wyjsc z rekurencji
        flag = False

        # counter zlicza dlugosc drogi
        def dfs_visit(v, counter):
            nonlocal graph, visited, flag

            # sprawdzam gdzie moge przejsc z wierzcholka v
            for j in range(n):
                if graph[v][j] == 1 and visited[v][j] == False:
                    # ide do wierzcholka j
                    visited[v][j] = True
                    visited[j][v] = True
                    # sprawdzam czy moge stworzyc cykl; tzn czy istnieje krawedz miedzy
                    # wierzcholkiem i a j, a aktualna dlugosc drogi wynosi 3 (po przejsciu
                    # do wierzcholka poczatkowego tworze cykl dlugosci 4)
                    if counter == 3 and graph[j][i] == 1:
                        flag = True
                        return
                    elif counter < 3:
                        dfs_visit(j, counter + 1)
                    # nie ma sensu sprawdzac dalej jesli dlugosc drogi wieksza bedzie niz 3,
                    # a cykl dlugosci 4 nie zostal znaleziony
                    if counter > 3:
                        return
                    if flag == True:
                        return

        dfs_visit(i, 1)
        if flag is True:
            return True

    # jesli nie znajdzie to zwracam False
    return False

if __name__ == '__main__':
    g1 = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    print(find_cycle_DFS(g1))
    # True (cykl 1, 2, 3, 0)
    g2 = [
        [0, 1, 0, 0],
        [1, 0, 1, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 0]
    ]
    print(find_cycle_DFS(g2))
    # False (cyklu dlugosci 4 nie ma)
    g3 = [
        [0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0]
    ]
    print(find_cycle_DFS(g3))
    # False (cyklu dlugosci 4 nie ma)
    # g4 to graf z g3 gdzie lacze wierzcholek 2 z 5
    # i tworze dzieki temu cykl dlugosci 4
    g4 = [
        [0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 1],
        [1, 1, 0, 0, 1, 0]
    ]
    print(find_cycle_DFS(g4))
    # True (cykl 2, 3, 4, 5)
    g5 = [
        [0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 1],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0]
    ]
    print(find_cycle_DFS(g5))
    # True (cykl 2, 3, 4, 5)
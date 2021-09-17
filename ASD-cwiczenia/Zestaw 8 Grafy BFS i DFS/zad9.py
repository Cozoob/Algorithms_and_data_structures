# Created by Marcin "Cozoob" Kozub 14.05.2021
# (czy nieskierowany?) Proszę podać algorytm, który mając na wejściu graf G reprezentowany
# przez listy sąsiedztwa sprawdza, czy jest nieskierowany (czyli czy dla każdej krawędzie u → v istnieje także
# krawędź przeciwna).
from collections import deque

# Pomysł: Odpalam BFS i przypisuje wartosc True przy odwiedzniu wierzcholka wtw,gdy istnieje krawedz
# powrotna do rodzica. Nie ma znaczenia z ktorego wierzcholka wystartuje BFS'a. Na koniec tylko sprawdzam
# czy wszystkie wierzcholki maja wartosc True.

# O(n^3) mi sie wydaje, a co gdyby zamienic reprezntacje w postac macierzowa stworzenie zajeloby
# O(n^2) a sprawdzanie czy pomiedzy kazdymi wierzcholkami jest krawedz w obie strony O(n^2/2)
def check_graph(graph):
    n = len(graph)
    visited = [False] * n
    queue = deque()

    # skoro wierzcholek od ktorego zaczynamy nie ma znaczenia to zawsze zaczynajmy od wierzcholka 0
    queue.append(0)
    visited[0] = True

    while len(queue) != 0:
        u = queue.pop()
        for v in graph[u]:
            if not visited[v]:
                # sprawdzam dodatkowo czy istnieje krawedz z v do u
                for x in graph[v]:
                    if x == u:
                        visited[v] = True
                        queue.append(v)

    # sprawdzam tylko dodatkowo czy wszedzie jest True
    for i in range(n):
        if visited[i] == False:
            return False

    return True


if __name__ == '__main__':
    # False z 1 do 0 nie ma
    g0 = [
        [1],
        [2,5],
        [1,3,4],
        [2],
        [2],
        [1]
    ]
    print(check_graph(g0))
    # True
    g1 = [
        [1],
        [0, 2, 5],
        [1, 3, 4],
        [2],
        [2],
        [1]
    ]
    print(check_graph(g1))
    print()
    print(better_checker(g0))
    print(better_checker(g1))
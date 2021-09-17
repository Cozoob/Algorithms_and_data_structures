# Created by Marcin "Cozoob" Kozub at 10.05.2021 17:29
# Zadanie 5. (krawędzie 0/1) Dana jest mapa kraju w postaci grafu G = (V, E). Kierowca chce przejechać
# z miasta (wierzchołka) s to miasta t. Niestety niektóre drogi (krawędzie) są płatne. Każda droga ma taką
# samą jednostkową opłatę. Proszę podać algorytm, który znajduje trasę wymagającą jak najmniejszej liczby
# opłat. W ogólności graf G jest skierowany, ale można najpierw wskazać algorytm dla grafu nieskierowanego.

# Reprezentacja macierzowa, gdzie -1 ozn brak krawedzi pomiedzy wierzcholkami, a 0/1 oplate.
# Pomysł: Lacze dwa wierzcholki w nowy jeden wtw, gdy pomiedzy nimi krawedz ma oplate 0. Tzn. znajduje
# spojne skladowe i zmieniam graf. W nowym grafie wszystkie krawedzie pomiedzy wierzcholkami maja platnosc 1.
# Zatem wystarczy puscic BFS'a z wierzcholka s i wyczytac odleglosc do wierzcholka t.
# FAJNE DO OPISU ALE DO IMPLEMENTACJI NIE
# Rozwiazanie od hindusa uzywajace algorytm dijkstry troche zmieniony
# jesli jakas krawedz nie byla przez nas odwiedzona (lub byla ale mozemy do niej dotrzec w lepszy sposob
# to ja poprawiamy) to ja odwiedzamy. Jesli poprawiajac lub idac do wierzcholka przeszlismy po krawedzi
# o wadze 0 to wkladamy wierzcholek wierzcholek do ktorego przyszlismy na poczatek kolejki, bo ponowne
# wywolanie go moze poprawic teraz nastepne wierzcholki a chcemy to zrobic od razu. Jesli krawedz po ktorej
# przeszlismy ma wage 1, to odkladamy na koniec kolejki wierzcholek, aby pooblicza odpowiednio odleglosci miedzy
# wierzcholkami polaczonymi 0

from collections import deque

def find_path(graph, s, t):
    inf = float("inf")
    n = len(graph)
    dist = [inf] * n
    parent = [None] * n
    queue = deque()

    queue.append(s)
    dist[s] = 0

    while len(queue) != 0:
        u = queue.pop()
        for v in range(n):
            if graph[u][v] >= 0 and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
                parent[v] = u
                if graph[u][v] == 0:
                    queue.appendleft(v)
                else:
                    queue.append(v)

    path = get_path(s, t, [], parent)
    return dist[t], path

def get_path(s, t, path, parent):
    if s == t:
        path.append(t)
    else:
        get_path(s, parent[t], path, parent)
        path.append(t)
    return path

if __name__ == '__main__':
    # grafy acykliczny nieskierowane
    # odp to 1 dla 0-5
    g0 =[
        [-1, 1, -1, -1, -1, -1],
        [1, -1, 0, -1, -1, 1],
        [-1, 0, -1, 0, -1, -1],
        [-1, -1, 0, -1, 0, -1],
        [-1, -1, -1, 0, -1, 0],
        [-1, 1, -1, -1, 0, -1]
    ]
    print(find_path(g0, 0, 5))
    # odp to 1 dla 0-4
    g1 = [
        [-1, 0, -1, -1, -1, -1, -1],
        [0, -1, 1, -1, -1, -1, 0],
        [-1, 0, -1, 0, -1, -1, -1],
        [-1, -1, 0, -1, 1, -1, -1],
        [-1, -1, -1, 1, -1, 1, -1],
        [-1, -1, -1, -1, 1, -1, 0],
        [-1, 0, -1, -1, -1, 0, -1]
    ]
    print(find_path(g1, 0, 4))
    # odp to 3 dla 0-3
    g2 = [
        [-1, 1, -1, -1],
        [1, -1, 1, -1],
        [-1, 1, -1, 1],
        [-1, -1, 1, -1]
    ]
    print(find_path(g2, 0, 3))
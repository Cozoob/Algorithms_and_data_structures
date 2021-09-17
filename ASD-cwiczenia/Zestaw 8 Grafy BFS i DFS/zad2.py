# Created by Marcin "Cozoob" Kozub 13.05.2021
# (uniwersalne ujscie) Mówimy, ze wierzchołek t w grafie skierowanym jest uniwersalnym
# ujsciem, jesli:
# (a) z kazdego innego wierzchołka v istnieje krawedz z v do t
# (b) nie istnieje zadna krawedz wychodzaca z t.
# 1. Podac algorytm znajdujacy uniwersalne ujscie (jesli istnieje) przy reprezentacji macierzowej (O(n2)).
# 2. Pokazac, ze ten problem mozna rozwiazac w czasie O(n) w reprezentacji macierzowej.

# Pomysl: Sprawdzam dla wierzcholka 0, czyli w pierwszej podtablicy w reprezentacji macierzowej
# gdzie jest jedynka (jesli jest zero to sprawdzam czy wszystkie pozostale liczby w kolumnie
# sa 1-kami jesli tak to wierzcholek 0 jest ujsciem), jesli znajde jedynke to sprawdzam
# czy wszstkie pozostale liczby w kolumnie sa 1-kami oprocz jednego wierzcholka v. Jesli tak
# to wierzcholek v jest ujsciem.

def check_escape(graph):
    n = len(graph)
    if n == 2:
        if graph[0][1] == 1:
            return 1
        else:
            return 0
    if n == 1:
        return 0

    for v in range(n):
        if graph[0][v] == 0 and graph[1][v] == 1:
            i = 2
            while i < n:
                if graph[i][v] == 0:
                    i -= 1
                    break
                i += 1
            if i == n - 1:
                return 0

        if graph[0][v] == 1 and graph[1][v] == 1:
            i = 2
            x = -1
            while i < n:
                if graph[i][v] == 0:
                    if x != -1:
                        break
                    x = i
                i += 1
            if x != -1:
                return x

    return -1

if __name__ == '__main__':
    g0 = [
        [0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 1],
        [0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0]
    ]
    print(check_escape(g0))
# Created by Marcin "Cozoob" Kozub 14.05.2021
# (kapitan statku, zadanie z kolokwium w 2012/13) Kapitan pewnego statku zastanawia
# się, czy może wpłynąć do portu mimo, że nastąpił odpływ. Do dyspozycji ma mapę zatoki w postaci tablicy
# M, gdzie M[x][y] to głebokość zatoki na pozycji (x, y). Jeśli jest ona większa niż pewna wartość int T
# to statek może się tam znaleźć. Początkowo statek jest na pozycji (0, 0) a port znajduje się na pozycji
# (n − 1, m − 1). Z danej pozycji statek może przepłynąć bezpośrednio jedynie na pozycję bezpośrednio obok
# (to znaczy, na pozycję, której dokładnie jedna ze współrzędnych różni się o jeden). Proszę napisać funkcję
# rozwiązującą problem kapitana.

# Sprawdzam BFS'em czy kapitan moze doplynac z pozycji (0,0) na pozycje (x,y), wiec aktualizuje tablice visited wtw, gdy M[x][y] - T >= 0
# Zakladam ze kapitan moze plynac tylko w gore, dol, lewo i prawo.
from collections import deque

def find_path(M, T):
    n = len(M)
    m = len(M[0])
    # w tablcy visited trzymam odp do ktorych punktow kapitan moze doplynac
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True

    queue = deque()
    queue.append((0,0))
    moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    while len(queue) != 0:
        i, j = queue.pop()
        for move in moves:
            if 0 <= i + move[0] < n and 0 <= j + move[1] < m:
                if not visited[i + move[0]][j + move[1]] and M[i + move[0]][j + move[1]] - T >= 0:
                    visited[i + move[0]][j + move[1]] = True
                    queue.append((i + move[0], j + move[1]))

    return visited[n - 1][m - 1], visited

if __name__ == '__main__':
    # True
    M1 = [
        [6, 1, 2, 3],
        [5, 3, 4, 2],
        [1, 2, 2, 2]
    ]
    print(find_path(M1, 2))
    # False
    print(find_path(M1, 5))
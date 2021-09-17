# Created by Marcin "Cozoob" Kozub 14.05.2021
# Zadanie 7. (kosztowna szachownica) Dana jest szachownica o wymiarach n × n. Każde pole (i, j)
# ma koszt (liczbę ze zbioru {1, . . . , 5}) umieszczony w tablicy A (na polu A[i][j]). W lewym górnym rogu
# szachownicy stoi król, którego zadaniem jest przejsc do prawego dolnego rogu, przechodzac po polach o
# minmalnym sumarycznym koszcie. Prosze zaimplementowac funkcje kings path(A), która oblicza koszt
# sciezki króla. Funkcja powinna byc mozliwie jak najszybsza.

# Pomysł: Odpalam DFS ktory przejdzie wszystkimi mozliwymi drogami z lewego gornego do prawego dolnego rogu.
# Jednoczesnie zlicza sume przejscia curr_sum i gdy dotrze na koniec jest min_sum = min(curr_sum, min_sum), gdzie
# min_sum to nasz wynik. Na poczatku min_sum = +inf.
from collections import deque

def kings_path(A):
    n = len(A)
    inf = float("inf")
    dist = [[inf for _ in range(n)] for _ in range(n)]

    dist[0][0] = A[0][0]
    queue = deque()
    queue.append((0,0))
    neighbours = [ [-1,0],[-1, -1], [0, -1], [1, -1], [1,0],[1,1], [0,1], [-1, 1]]

    while len(queue) != 0:
        i, j = queue.pop()
        for ngh in neighbours:
            if not 0 <= i + ngh[0] < n or not 0 <= j + ngh[1] < n:
                continue
            if dist[i + ngh[0]][j + ngh[1]] > dist[i][j] + A[i + ngh[0]][j + ngh[1]]:
                dist[i + ngh[0]][j + ngh[1]] = dist[i][j] + A[i + ngh[0]][j + ngh[1]]
                queue.append((i + ngh[0], j + ngh[1]))

    return dist[n - 1][n - 1]


if __name__ == '__main__':
    A = [
        [1, 1, 1, 5, 5],
        [5, 5, 1, 5, 5],
        [1, 1, 1, 5, 5],
        [1, 5, 5, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    print(kings_path(A))
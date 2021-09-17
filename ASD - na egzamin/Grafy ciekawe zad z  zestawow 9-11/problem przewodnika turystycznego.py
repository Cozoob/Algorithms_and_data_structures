# Created by Marcin "Cozoob" Kozub 28.06.2021
from queue import PriorityQueue
# Zadanie 5. (problem przewodnika turystycznego) Przewodnik chce przewieźć grupę K turystów z
# miasta A do miasta B. Po drodze jest jednak wiele innych miast i między różnymi miastami jeżdzą autobusy o
# różnej pojemności. Mamy daną listę trójek postaci (x, y, c), gdzie x i y to miasta między którymi bezpośrednio
# jeździ autobus o pojemności c pasażerów.
# Przewodnik musi wyznaczyć wspólną trasę dla wszystkich tursytów i musi ich podzielić na grupki tak,
# żeby każda grupka mogła przebyć trasę bez rodzielania się. Proszę podać algorytm, który oblicza na ile
# (najmniej) grupek przewodnik musi podzielić turystów (i jaką trasą powinni się poruszać), źeby wszyscy
# dostali się z A do B.

# najpierw tworze sobie graf na podstawie listy sasiedztwa
# nastepnie uzywam algorytmu Dijkstry ale zamiast odleglosci zapisuje pojemonosc trasy
# i wybieram po prostu najlepsza pojemnosc w danej chwili. W miedzy czasie zapisuje parentow

def change_to_graph(T):
    n = len(T)
    # najpierw szukam max wierzcholka
    max_v = 0
    for i in range(n):
        max_v = max(max_v, T[i][1], T[i][0])

    G = [[] for _ in range(max_v + 1)]
    for i in range(n):
        x, y, c = T[i]
        G[x].append([y, c])
        G[y].append([x, c])  # bo zakladam ze graf jest nieskierowany

    return G


def how_many_groups(T, A, B, K):
    G = change_to_graph(T)
    # for elem in G:
    #     print(elem)
    inf = float("inf")
    n = len(G)
    queue = PriorityQueue()
    queue.put([inf, A])
    capacity = [-inf for _ in range(n)]
    capacity[A] = inf
    parent = [-1 for _ in range(n)]

    while not queue.empty():
        u = queue.get()
        u = u[1]
        for elem in G[u]:
            v = elem[0]
            c = elem[1]
            if capacity[v] < min(capacity[u], c):
                capacity[v] = min(capacity[u], c)
                parent[v] = u
                queue.put([capacity[v], v])

    answer = K // capacity[B]
    if K % capacity[B] != 0:
        answer += 1

    # zostalo wyznaczyc ich trase
    res = [B]
    u = parent[B]
    while u != A:
        res.append(u)
        u = parent[u]
    res.append(A)


    return answer, res[::-1]


if __name__ == '__main__':
    T0 = [(0, 1, 10), (1, 2, 8), (1, 3, 4), (1, 4, 3), (2, 5, 2), (3, 5, 4), (4, 5, 10)]
    print(how_many_groups(T0, 0, 4, 14))
    print(how_many_groups(T0, 4, 2, 10))

    T1 = [(0, 1, 100), (0, 4, 10), (1, 2, 99), (2, 3, 98), (3, 4, 1)]
    print(how_many_groups(T1, 0, 4, 9))
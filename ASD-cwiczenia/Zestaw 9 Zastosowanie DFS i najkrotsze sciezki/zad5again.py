# Created by Marcin "Cozoob" Kozub 11.06.2021
# Zadanie 5. (problem przewodnika turystycznego) Przewodnik chce przewieźć grupę K turystów z
# miasta A do miasta B. Po drodze jest jednak wiele innych miast i między różnymi miastami jeżdzą autobusy o
# różnej pojemności. Mamy daną listę trójek postaci (x, y, c), gdzie x i y to miasta między którymi bezpośrednio
# jeździ autobus o pojemności c pasażerów.
# Przewodnik musi wyznaczyć wspólną trasę dla wszystkich tursytów i musi ich podzielić na grupki tak,
# żeby każda grupka mogła przebyć trasę bez rodzielania się. Proszę podać algorytm, który oblicza na ile
# (najmniej) grupek przewodnik musi podzielić turystów (i jaką trasą powinni się poruszać), źeby wszyscy
# dostali się z A do B.
from queue import PriorityQueue

# Pomysł: Z informacji podanych na poczatku tworze graf w reprezentacji macierzowej tzn (x,y,c) to wierzcholki x,y
# miedzy ktorymi jest krawedz o wadze c. Nastepnie przy pomocy zmodyfikowanego troche algorytmu Dijkstry wyznaczam
# trase przez ktora turysci maja jechac. Na koniec obliczac ile takich grupek trzeba utworzyc.
# Modyfikacja Dijkstry polega na zmianie w relaksacji tzn wyznaczam nie odleglosc, a "pojemnosc" trasy, gdzie
# wybieram najwieksza mozliwa "pojemnosc".

# Zlozonosc czasowa: O(V^2) (przez reprezentacje macierzowa/ w repr. list sasiedztwa jest ElogV)
# Zlozonosc pamieciowa: O(V^2)

def how_many_groups(T, A, B, K):

    # sprawdzam ile wierzcholkow musze stworzyc
    n = -1
    for i in range(len(T)):
        n = max(n, T[i][0], T[i][1])

    n += 1
    inf = float("inf")
    G = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(len(T)):
        a = T[i][0]
        b = T[i][1]
        G[a][b] = T[i][2]
        G[b][a] = G[a][b]

    # u i v to krotki/tablice wierzcholkow u oraz v
    def relax(u, capacity_u, v, capacity_v, G):

        if capacity_v < capacity_u:
            capacity_v = max(min(capacity_u, G[u][v]), capacity_v)

        v = [capacity_v, v]
        return v

    queue = PriorityQueue()
    # umieszczam wszystkie wierzcholki w kolejce priorytetowej
    # wraz z informacja o pojemnosc trasy do danego wierzcholka
    # [capacity of A, vertex]
    # dla wierzcholka A ustawiam umownie capacity = inf
    queue.put([inf, A])

    # nasz zbior wierzcholkow przetworzony z informacja o odleglosci do s
    capacity = [0 for _ in range(n)]
    capacity[A] = inf

    # dopoki sa wierzcholki w kolejce
    while not queue.empty():
        # wyjmuje wierzcholek u o minimalnym oszacowaniu pojemnosci
        u = queue.get()
        u = u[1]
        for v in range(n):
            if G[u][v] != -1:
                # dla kazdej krawedzi {u, v} wykonuje relaksacje
                new_v = relax(u, capacity[u], v, capacity[v], G)
                if new_v[0] > capacity[v]:
                    capacity[v] = new_v[0]
                    queue.put(new_v)

    c = capacity[B]
    answer = K // c
    if K % c != 0:
        answer += 1

    return answer


if __name__ == '__main__':
    T0 = [(0, 1, 10), (1, 2, 8),(1, 3, 4), (1, 4, 3), (2, 5, 2), (3, 5, 4), (4, 5, 10)]
    print(how_many_groups(T0, 0, 4, 14))
    T1 = [(0, 1, 100), (0, 4, 10), (1, 2, 99), (2, 3, 98), (3, 4, 1)]
    print(how_many_groups(T1, 0, 4, 9))
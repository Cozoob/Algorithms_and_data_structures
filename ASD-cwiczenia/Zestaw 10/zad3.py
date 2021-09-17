# Created by Marcin "Cozoob" Kozub 12.06.2021
# Zadanie 3. (wymiana walut) Dana jest tabela kursów walut. Dla każdych dwóch walut x oraz y wpis
# K[x][y] oznacza ile trzeba zapłacić waluty x żeby otrzymać jednostkę waluty y. Proszę zaproponować algorytm,
# który sprawdza czy istnieje taka waluta z, że za jednostkę z można uzyskać więcej niż jednostkę z
# przez serię wymian walut.
from queue import PriorityQueue
# Pomysł: Dla kazdego wierzcholka v uzywam Dijkstre i jesli money[v] > 1 to oznacza ze znalazlem taka serie
# wymiany walut ze uzyskalem wiecej niz przed wymiana. Jesli dla zadnego wierzcholka v takie cos nie zachodzi,
# to zwracam False.

# Zlozonosc czasowa: O(V^3)

def this_one_simple_trick_will_make_u_millionaire(G):

    # u i v to krotki/tablice wierzcholkow u oraz v
    def relax(u, money_u, v, money_v, G):

        tmp = money_u / G[u][v]
        money_v = max(money_v, tmp)

        v = [-money_v, v]
        return v

    n = len(G)

    for s in range(n):
        queue = PriorityQueue()
        # umieszczam wszystkie wierzcholki w kolejce priorytetowej
        # wraz z informacja o odleglosc do s
        # [money of s, vertex]
        # dla wierzcholka s ustawiam money = -1
        queue.put([-1, s])

        # nasz zbior wierzcholkow przetworzony z informacja o hajsie w s po wymianach
        money = [0 for _ in range(n)]
        money[s] = 1

        # dopoki sa wierzcholki w kolejce
        while not queue.empty():
            # wyjmuje wierzcholek u o maksymalnym oszacowaniu pieniedzy
            # zeby tak zrobic stosuje taka sztuczke ze w kolejce umieszczam
            # elemeny money[v] z minusem.
            u = queue.get()
            u = abs(u[1])
            for v in range(n):
                if G[u][v] != -1:
                    # dla kazdej krawedzi {u, v} wykonuje relaksacje
                    new_v = relax(u, money[u], v, money[v], G)
                    money_v = abs(new_v[0])
                    if v == s and money_v > money[v]:
                        return True
                    if money_v > money[v]:
                        money[v] = money_v
                        queue.put(new_v)

    return False

if __name__ == '__main__':
    K1 = [
        [-1, 4.50, 8, -1],
        [-1, -1, 2, -1],
        [-1, -1, -1, 0.005],
        [0.2, -1, -1, -1]
    ]
    print(this_one_simple_trick_will_make_u_millionaire(K1))
    K2 = [
        [-1, 4.50, -1, 4],
        [-1, -1, 2, -1],
        [-1, -1, -1, 5],
        [1.2, 8, -1, -1]
    ]
    print(this_one_simple_trick_will_make_u_millionaire(K2))
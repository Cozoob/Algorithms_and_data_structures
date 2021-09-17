# Created by Marcin "Cozoob" Kozub 10.06.2021
# Zadanie 1. (ścieżka Hamiltona w DAGu) Ścieżka Hamiltona to ścieżka przechodząca przez wszystkie
# wierzchołki w grafie, przez każdy dokładnie raz. W ogólnym grafie znalezienie ścieżki Hamiltona
# jest problemem NP-trudnym. Proszę podać algorytm, który stwierdzi czy istnieje ścieżka Hamiltona w acyklicznym
# grafie skierowanym.

# Pomysł: Wystarczy posortowac topologicznie ten graf i zobaczyc czy idac od poczatku do konca po posortowanych
# wierzcholkach przejdziemy przez wszystkie wierzcholki. Jesli przez jakis wierzcholek nie przeszlismy
# to oznacza ze nie istnieje taka sciezka Hamiltona w tym DAGu.

# Złożoność czasowa: O(E + V)
# Złożoność pamieciowa: O(V)

# reprezentacja list sasiedztwa
def is_Hamilton_Path(G):
    n = len(G)
    visited = [False for _ in range(n)] # t: O(n), m: O(n), n = V

    def visit(u, flag):
        nonlocal visited, stack, n, G

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                visit(v, flag)
                if flag is False:
                    break

        if flag:
            stack.append(u)


    stack = []
    for v in range(n): # sortowanie topologiczne t: O(V + E), m: O(n), n = V
        if not visited[v]:
            visit(v, True)

    stack = stack[::-1]
    visited = [False for _ in range(n)] # t: O(n), m: O(n), n = V
    visit(stack[0], False) # t: O(V + E), m: O(n), n = V


    for i in range(n): # t: O(n), n = V
        if visited[i] is False:
            return False

    return True



if __name__ == '__main__':
    if __name__ == '__main__':
        # True
        G0 = [
            [1,2],
            [2],
            [3],
            []
        ]
        print(is_Hamilton_Path(G0))
        # True (G0 tylko ze brak krawedzi z 0 do 1)
        G1 = [
            [2],
            [2],
            [3],
            []
        ]
        print(is_Hamilton_Path(G1))
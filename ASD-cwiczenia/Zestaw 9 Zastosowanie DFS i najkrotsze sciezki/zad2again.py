# Created by Marcin "Cozoob" Kozub 10.06.2021
# Zadanie 2. (dobry początek) Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli
# każdy inny wierzchołek można osiągnąć scieżką skierowaną wychodzącą z v. Proszę podać algorytm, który
# stwierdza czy dany graf zawiera dobry początek.

# Pomysł: Wrecz prawie identyczny jak w zad1 tylko bez breaka... sortuje topologicznie i sprawdzam czy z pierwszego wierzcholka
# z posortowanych wierzcholkow odwiedze kazde pozostale wierzcholki. Jesli tak to mamy dobry poczatek.

# Analiza zlozonosci taka sama jak w zad1
# Zlozonosc czasowa: O(V + E)
# Zlozonosc pamieciowa: O(V)


# reprezentacja list sasiedztwa
def the_good_start(G):
    n = len(G)
    visited = [False for _ in range(n)]

    # flaga pomaga mi w dodawaniu wierzcholkow do sortowania
    def visit(u, flag):
        nonlocal n, G, visited, stack

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                visit(v, flag)
        if flag:
            stack.append(u)



    stack = []
    for v in range(n):
        if not visited[v]:
            visit(v, True)

    stack = stack[::-1]
    visited = [False for _ in range(n)]
    visit(stack[0], False)
    for i in range(n):
        if visited[i] is False:
            return False

    return True
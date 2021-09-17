# Created by Marcin "Cozoob" Kozub 30.05.2021
# Zadanie 1. (ścieżka Hamiltona w DAGu) Ścieżka Hamiltona to ścieżka przechodząca przez wszystkie
# wierzchołki w grafie, przez każdy dokładnie raz. W ogólnym grafie znalezienie ścieżki Hamiltona
# jest problemem NP-trudnym. Proszę podać algorytm, który stwierdzi czy istnieje ścieżka Hamiltona w acyklicznym
# grafie skierowanym.

# Pomysł: Uzywam dfs gdzie breakuje w odpowiednim momencie i sprawdzam czy idac z wierzcholka 0 przechodze przez wszystkie
# pozostale wierzcholki tak ze docieram do ostatniego wierzcholka. Jesli ktorys nie odwiedze
# to oznacza ze w DAGu nie istnieje sciezka Hamiltona.
# Zlozonosc: O(V + E)

# reprezentacja list sasiedztwa
def is_Hamilton_Path_in_DAG(G):
    n = len(G)

    visited = [False] * len(G)
    # stack = []

    def dfs_visit(u):
        nonlocal G, visited

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(v)
                break

        # stack.append(u)

    dfs_visit(0)

    for i in range(n):
        if visited[i] == False:
            return False

    # return True, stack[::-1]
    return True

if __name__ == '__main__':
    # True
    G0 = [
        [1,3,2],
        [3],
        [],
        [2]
    ]
    print(is_Hamilton_Path_in_DAG(G0))
    # False
    G1 = [
        [1, 2],
        [3],
        [],
        []
    ]
    print(is_Hamilton_Path_in_DAG(G1))
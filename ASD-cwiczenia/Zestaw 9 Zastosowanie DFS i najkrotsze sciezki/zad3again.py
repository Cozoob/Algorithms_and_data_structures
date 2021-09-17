# Created by Marcin "Cozoob" Kozub 10.06.2021

# Zadanie 3. (najkrósze ścieżki w DAGu) Jak znaleźć najkrótsze ścieżki z wierzchołka s do wszystkich
# innych w acyklicznym grafie skierowanym?

# Zwykly DFS/BFS ?
# NO CHYBA ZE TO GRAF WAZONY.
# Pomysł (jesli ten DAG jest wazony): Znow korzystamy z sortowania topologicznego, a pozniej tylko
# ustawiamy/poprawiamy dystans z wierzcholka s do jakiegos wierzcholka v (wraz z rodzicami, ktorzy
# pomoga nam w odtworzeniu sciezki). Jesli dystans inf to oznacza ze nie ma sciezki z s do tego wierzcholka.

# Zlozonosc czasowa: O(V^2) (dla repr. list sasiedztwa O(V + E))
# Zlozonosc pamieciowa: O(V)

# reprezentacja macierzowa (inf oznacza brak krawedzi)
def find_shortest_path(G, s):
    n = len(G)
    inf = float("inf")
    distance = [inf for _ in range(n)]
    visited = [False for _ in range(n)]

    def visit_top_sort(u):
        nonlocal n, G, visited, stack, inf

        visited[u] = True
        for v in range(n):
            if G[u][v] != inf and visited[v] is False:
                visit_top_sort(v)
        stack.append(u)



    stack = []
    for v in range(n):
        if not visited[v]:
            visit_top_sort(v)

    stack = stack[::-1]
    distance[s] = 0

    for u in stack:
        for v in range(n): # t: byloby O(V + E) na listach sasiedztwa ale ze repr. macierzeowa to O(V^2) niestety
            if G[u][v] != inf and distance[v] > distance[u] + G[u][v]:
                distance[v] = distance[u] + G[u][v]

    return distance


if __name__ == '__main__':
    inf = float("inf")
    G = [
        [inf, inf, inf, 7, 4, 2],
        [3, inf, -1, inf, inf, inf],
        [2, inf, inf, 6, inf, inf],
        [inf, inf, inf, inf, 5, 1],
        [inf, inf, inf, inf, inf, -2],
        [inf, inf, inf, inf, inf, inf]
    ]
    print(find_shortest_path(G, 2))
    print(find_shortest_path(G, 3))
    print(find_shortest_path(G, 0))
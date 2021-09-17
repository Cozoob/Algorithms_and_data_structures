# Created by Marcin "Cozoob" Kozub 12.06.2021
# Zadanie 2. (domknięcie przechodnie) Proszę zaimplementować algorytm obliczający domknięcie przechodnie grafu
# reprezentowanego w postaci macierzowej (domknięcie przechodnie grafu G, to graf nad tym
# samym zbiorem wierzchołków, który dla każdych dwóch wierzchołków u i v ma krawędź z u do v wtedy i
# tylko wtedy, gdy w G istnieje ścieżka z u do v.

# Wykonuje DFS dla kazdego wierzcholka i zapisuje odpowiedzi. (Czyli w sumie taki Floyd-Warshall)

# Zlozonosc czasowa: O(V^3)

def function(G):
    n = len(G)
    answer = [[] for _ in range(n)]

    for s in range(n):
        visited = [False] * n

        def dfs_visit(u):
            nonlocal G, visited

            visited[u] = True
            for v in range(n):
                if G[u][v] != -1:
                    if not visited[v]:
                        answer[s].append(v)
                        dfs_visit(v)

        dfs_visit(s)

    return answer

if __name__ == '__main__':
    G = [
        [-1, 1, -1, -1, -1, -1, -1, -1],
        [1, -1, 1, -1, 1, -1, -1, -1],
        [-1, 1, -1, 1, -1, 1, -1, -1],
        [-1, -1, 1, -1, -1, -1, -1, -1],
        [-1, 1, -1, -1, -1, -1, -1, -1],
        [-1, -1, 1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, 1],
        [-1, -1, -1, -1, -1, -1, 1, -1]
    ]
    print(function(G))
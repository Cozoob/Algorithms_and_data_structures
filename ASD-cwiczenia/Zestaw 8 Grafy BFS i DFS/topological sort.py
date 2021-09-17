# Created by Marcin "Cozoob" Kozub 30.05.2021

# Zlozonosc: O(V + E)

# reprezentacja list sasiedztwa
def topological_sort(G):
    n = len(G)
    visited = [False for _ in range(n)]

    def visit(s):
        nonlocal visited, stack, n, G

        visited[s] = True
        for v in G[s]:
            if not visited[v]:
                visit(v)

        stack.append(s)

    stack = []
    for v in range(n):
        if not visited[v]:
            visit(v)

    return stack[::-1]


if __name__ == '__main__':
    G = [
        [],
        [],
        [3],
        [1],
        [1, 0],
        [2, 0]
    ]
    print(topological_sort(G))
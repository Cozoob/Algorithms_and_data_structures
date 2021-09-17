# Created by Marcin "Cozoob" Kozub 24.06.2021
# O(VE)

# LISTY SASIEDZTWA
def Bellman_Ford(G, s, t):
    n = len(G)
    inf = float("inf")
    distance = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[s] = 0

    for i in range(n):
        for u in range(n):
            for v, w in G[u]:
                if distance[v] > distance[u] + w:
                    distance[v] = distance[u] + w
                    parent[v] = u

    for u in range(n):
        for v, w in G[u]:
            if distance[u] + w < distance[v]:
                return None

    return distance[t]

if __name__ == '__main__':
    G = [
        [[1,6], [2,5],[3,5]],
     [[4,-1]],
     [[1,-2],[4,1]],
     [[2,-2],[5,-1]],
     [[6,3]],
     [[6,3]],
     []
    ]

    print(Bellman_Ford(G, 0, 6))
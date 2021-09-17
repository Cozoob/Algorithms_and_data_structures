# Created by Marcin "Cozoob" Kozub at 24.04.2021 23:29
# Znajdź długość najdłuższej ścieżki prostej w acyklicznym grafie skierowanym.
# Dodatkowo odtworz te sciezke.

# f(i) - dlugość najdluzszej sciezki konczacej sie w i
# f(i) = max(f(j)) + 1
# wynik: max(f(i))

# nie dziala idk jak implementacja

class Vertex():

    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.parent = None
        self.d = 1

def find_path(G):
    n = len(G)
    # sprawdzam dla kazdego wierzcholka jak daleko moge doisc
    # i zapisuje informacje w tablicy F
    F = [0 for _ in range(n)]
    for i in range(1, n):
        vertex = G[i]
        d = 1
        while vertex != None:
            d += 1
            vertex = vertex.next
        F[i] = d
        G[i].d = d

    return max(F)


if __name__ == '__main__':
    G = [0, Vertex(1), Vertex(2), Vertex(3), Vertex(4), Vertex(5), Vertex(6), Vertex(7), Vertex(8)]
    G[1].next = [G[2], G[6], G[4]]
    G[2].next = []
    G[3].next = [G[4], G[8]]
    G[4].next = []
    G[5].next = [G[1]]
    G[6].next = []
    G[7].next = [G[1], G[8]]
    G[8].next = [G[6]]

    print(find_path(G))
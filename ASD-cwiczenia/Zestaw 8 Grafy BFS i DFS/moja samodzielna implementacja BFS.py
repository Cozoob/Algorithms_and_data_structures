# Created by Marcin "Cozoob" Kozub at 03.05.2021 19:05

def BFS(G, s):
    # G = (V, E), s należy do V
    Q = q.Queue()

    s.d = 0
    s.visited = True
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in u.next:
            if v.visited == False:
                v.visited = True
                v.parent = u
                v.d = u.d + 1
                Q.put(v)


class Vertex():

    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.visited = False
        self.d = -1
        self.parent = None


# graf w reprezentacji listy sąsiedztwa
if __name__ == '__main__':
    # pierwszy graf G1 jest dwudzielny

    G1 = [Vertex(1), Vertex(2), Vertex(3), Vertex(4), Vertex(5)]
    G1[0].next = [G1[1]]
    G1[1].next = [G1[2]]
    G1[2].next = [G1[4]]
    G1[3].next = [G1[1]]
    G1[4].next = [G1[3]]

    BFS(G1, G1[0])
    print(G1[4].value, G1[4].parent.value, G1[4].next[0].value, G1[4].visited)
    #print(G1[3].value, G1[3].next[0].value)

    # drugi graf G2 nie jest dwudzielny

    G2 = [Vertex(1), Vertex(2), Vertex(3), Vertex(4), Vertex(5)]
    G2[0].next = G2[1]
    # przez polaczenie 2 i 5 graf staje sie nie dwudzielny
    G2[1].next = [G2[2], G2[4]]
    G2[2].next = [G2[4]]
    G2[3].next = [G2[1]]
    G2[4].next = [G2[3]]
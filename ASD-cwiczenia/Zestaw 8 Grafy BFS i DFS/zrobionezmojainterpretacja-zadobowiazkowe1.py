import queue as q
# Created by Marcin "Cozoob" Kozub at 03.05.2021 18:19
# Prosze zaimplementować algorytm sprawdzający czy graf jest dwudzielny.

# Pomysł: Wystarczy wykorzystac algorytm BFS, gdzie na poczatku wszystkie wierzcholki
# są pokolorwane na kolor neutralny (u nas None) zaś przechodzac z wierzchołka v do u
# bedziemy wierzcholek v kolorowac na czerwono (u nas reprezentacyjnie 0) a u na czarno
# (u nas reprezentacyjnie 1). Jesli uda nam sie pokolorwac wszystkie wierzcholki
# na czarno lub czerwono to mamy graf dwudzielny.

# zmodyfikowany BFS na potrzeby zadania
def BFS(G, s):
    # G = (V, E), s należy do V
    Q = q.Queue()

    s.d = 0
    s.visited = True
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in u.next:
            # jesli wierzcholki ze soba sa polaczone i oba
            # maja ten sam kolor zwracam False
            if v.visited == True and v.color == u.color:
                return False

            if v.visited == False:
                v.visited = True
                if u.color == 0:
                    v.color = 1
                else:
                    v.color = 0
                v.parent = u
                v.d = u.d + 1
                Q.put(v)

    # jesli pokoloruje wszystkie wierzcholki na 0 lub 1
    # i jestem w stanie podzelic graf na takie dwa podzbiory
    # kolorow to mam graf dwudzielny
    return True

class Vertex():

    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.visited = False
        self.d = -1
        self.parent = None
        self.color = None


# graf w reprezentacji listy sąsiedztwa
if __name__ == '__main__':
    # pierwszy graf G1 jest dwudzielny
    # tworze graf
    G1 = [Vertex(1), Vertex(2), Vertex(3), Vertex(4), Vertex(5)]
    G1[0].next = [G1[1]]
    G1[1].next = [G1[2]]
    G1[2].next = [G1[4]]
    G1[3].next = [G1[1]]
    G1[4].next = [G1[3]]

    # koloruje pierwszy wierzcholek na dowolny kolor

    G1[0].color = 0
    print(BFS(G1, G1[0]))

    print(G1[0].color)
    print(G1[1].color)
    print(G1[2].color)
    print(G1[3].color)
    print(G1[4].color)

    # print(G1[4].value, G1[4].parent.value, G1[4].next[0].value, G1[4].visited)
    # print(G1[3].value, G1[3].next[0].value)

    # drugi graf G2 nie jest dwudzielny
    G2 = [Vertex(1), Vertex(2), Vertex(3), Vertex(4), Vertex(5)]
    G2[0].next = [G2[1]]
    # przez np polaczenie 2 i 5 graf staje sie nie dwudzielny
    # ale moj algorytm koloruje tutaj w taki sposob ze (wierzcholek) "1" ma kolor 0
    # zatem kazde nastepne musza miec kolor 1; zatem w. "2" ma kolor 1 (...); zatem w. "3"
    # oraz w. "5" ma kolor 0 zatem kazde nastepne z w. "3" musza miec kolor 1 a tutaj
    # juz w. "5" ma kolor 0 !!! Wiec zwracam False.

    G2[1].next = [G2[2], G2[4]]
    G2[2].next = [G2[4]]
    G2[3].next = [G2[1]]
    G2[4].next = [G2[3]]

    G2[0].color = 0
    print(BFS(G2, G2[0]))

    print(G2[0].color)
    print(G2[1].color)
    print(G2[2].color)
    print(G2[3].color)
    print(G2[4].color)
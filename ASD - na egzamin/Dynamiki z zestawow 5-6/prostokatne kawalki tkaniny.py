# Created by Marcin "Cozoob" Kozub 28.06.2021
# Dany jest prostokątny kawałek tkaniny o wymiarach X na Y, oraz lista n produktów,
# które mogą zostać wykonane z tej tkaniny. Do wytworzenia każdego produktu i (i zmienia się od 1 do n)
# potrzebny jest prostokątny kawałek tkaniny o wymiarach ai na bi, a zysk ze sprzedaży tego produktu wynosi ci.
# Zakładamy, że ai, bi, ci są dodatnie całkowite. Mając maszynę, która może przeciąć dowolny prostokątny kawałek
# tkaniny na dwa kawałki wzdłuż linii poziomej lub pionowej, zaprojektuj algorytm, który wyznaczy taką strategię
# cięcia materiału o wymiarach X na Y, aby sprzedaż wytworzonych produktów dała łącznie jak największy zysk.

# na start dostajemy info o produktach w T pod postacia [ai, bi, ci] (wyjasnione w tresci zad)
# oraz X, Y wymiamy wlokna z ktorego mozemy ciac
# f(i,j) - maksymalny zysk z pociecia tkaniny o rozmiarach i na j
# C[a][b] - wartosc tkaniny o rozmiarach a na b
# f(i, j) = max( f(i - k, j) + f(k, j): k=[1,i], f(i, j - k) + f(i, k): k=[1,j], C[i][j])
# f(i, 0) = 0
# f(0, j) = 0

def cut_the_fabric(T, X, Y):
    n = len(T)
    inf = float("inf")

    # rozdzielam sobie tablice T dla ulatwienia na tablice W[a][b]
    W = [[0 for _ in range(Y + 1)] for _ in range(X + 1)]

    for i in range(n):
        W[T[i][0]][T[i][1]] = T[i][2]

    F = [[-inf for _ in range(Y + 1)] for _ in range(X + 1)]

    for i in range(X + 1):
        F[i][0] = 0

    for i in range(Y + 1):
        F[0][i] = 0

    for x in range(1, X + 1):
        for y in range(1, Y + 1):
            F[x][y] = max(F[x][y], W[x][y])
            for k in range(1, x + 1):
                F[x][y] = max(F[x - k][y] + F[k][y], F[x][y])
            for k in range(1, y + 1):
                F[x][y] = max(F[x][y - k] + F[x][k], F[x][y])

    return F

if __name__ == '__main__':
    Y = 10
    X = 20
    # nieograniczona ilosc moge wyprodukowac tych produktow:
    T = [ (18, 9, 10), (1,1,1) ]
    # odp poprawna to 200
    # print(cut_the_fabric(T, X, Y))
    F = cut_the_fabric(T, X, Y)
    for elem in F:
        print(elem)
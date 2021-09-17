# Created by Marcin "Cozoob" Kozub at 23.04.2021 20:50

# Rekurencyjne schody Amazona
# Cel: dana jest tablica A zawierająca liczby naturalne nie mniejsze od 1.
# początkowo stoimy na pozycji 0, wartość A[i] informuje nas jaka jest maksymalna długość skoku na następną pozycję.
#
# Przykład A = {1,3,2,1,0}
# Z pozycji 0 mogę przejść na pozycję 1. z pozycji 1 mogę przejść na 2, 3, 4.
# Należy policzyć na ile sposobów mogę przejść z pozycji 0 na pozycję n-1, przestrzegając reguł tablicy.

# f(i) - ilość sposobów na ktore moge przejsc z pozycji 0 na i
# ???
# f(i) = P[i-1] + 1
# f(0) = 1

def schody(A):
    n = len(A)
    # tworze pomocnicza tablice P ktora bedzie mi zapisywac podproblemy
    P = [0 for _ in range(n)]
    P[0] = 1

    # ide do przedostatniego elementu w tablicy A
    for i in range(1, n):
        # dodaje P[i - 1] + 1 sposobow na przejscie
        # na A[i - 1] kolejnych miejsc
        for j in range(A[i - 1]):
            P[i + j] += P[i - 1]

    # moje rozwiazanie znajdzie sie na koncu talbicy wtedy
    return P[n-1]

if __name__ == '__main__':
    A = [2, 1,3,2,1,0]
    print(schody(A))
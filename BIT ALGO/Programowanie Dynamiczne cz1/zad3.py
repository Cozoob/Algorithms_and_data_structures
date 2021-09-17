# Created by Marcin "Cozoob" Kozub at 18.04.2021 18:52
# Rekurencyjne schody Amazona
# Cel: dana jest tablica A zawierająca liczby naturalne nie mniejsze od 1.
# początkowo stoimy na pozycji 0, wartość A[i] informuje nas jaka jest maksymalna długość skoku na następną pozycję.
#
# Przykład A = {1,3,2,1,0}
# Z pozycji 0 mogę przejść na pozycję 1. z pozycji 1 mogę przejść na 2, 3, 4.
# Należy policzyć na ile sposobów mogę przejść z pozycji 0 na pozycję n-1, przestrzegając reguł tablicy.


# 1 sposob TOP-DOWN
# f(k, n) - ilość sposobów, aby przejść z pozycji k na pozycję n

# f(k, n) = suma(f(i, n) : 0 <= k < i < n "ze mozemy przejsc z i do n")
# gdzie 0 <= k < i < n

# 2 sposob BOTTOM-UP
# idk jaka funkcja....
# f(n)


# f(i) - ilosc sposobow na jaka mozemy dojsc na pozycje i
# f(i) = f(i - 1) + P[i]
def schody1(A):
    n = len(A)
    P = [0 for _ in range(n)]
    P[0] = 1
    for i in range(1, n):
        for j in range(A[i - 1]):
            P[i + j] += P[i - 1]

    return P[n - 1], P

if __name__ == '__main__':
    A = [2,1,3,2,1,0]
    print(schody1(A))


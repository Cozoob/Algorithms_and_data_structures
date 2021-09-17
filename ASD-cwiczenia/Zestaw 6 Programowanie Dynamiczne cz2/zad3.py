# Created by Marcin "Cozoob" Kozub 16.05.2021
# Zadanie 3. (ładowanie promu) Dana jest tablica A[n] z długościami samochodów, które stoją w kolejce,
# żeby wjechać na prom. Prom ma dwa pasy (lewy i prawy), oba długości L. Proszę napisać program, który
# wyznacza, które samochody powinny pojechać na który pas, żeby na promie zmieściło się jak najwięcej aut.
# Auta muszą wjeżdżac w takiej kolejności, w jakiej są podane w tablicy A.

# f(i, r, l) = { 1, pierwsze i samochdow można rozmieścić na promie tak, że zostaje l miejsca na lewym pasie i r miejsca na prawym pasie
#              { 0, w przciwnym wypadku
# wynik: max(n: f(n, r, l) = 1) ,gdzie r,l >= 0
#       n,r,l
# f(i, r, l) = f(i - 1, r + A[i], l) or f(i - 1, r, l + A[i])
# f(0, L, L) = 1

def load_ferry(A, L):
    n = len(A)
    Right = [0 for _ in range(n)]
    Left = [0 for _ in range(n)]
    # L1, Right dla prawego pasa; L2, Left dla lewego pasa

    def _rek(A, i, L1, L2):
        if i == 0:
            return True
        if L1 - A[i] >= 0 and L2 - A[i] >= 0:
            return _rek(A, i - 1, L1 - A[i], L2) or _rek(A, i - 1, L1, L2 - A[i])
        elif L1 - A[i] >= 0:
            return _rek(A, i - 1, L1 - A[i], L2)
        elif L2 - A[i] >= 0:
            return _rek(A, i - 1, L1, L2 - A[i])
        else:
            return False

    flag = _rek(A, n - 1, L, L)
    return flag

if __name__ == '__main__':
    A = [3, 2, 4, 8, 1, 2]
    print(load_ferry(A, 10))
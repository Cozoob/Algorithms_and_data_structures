# Created by Marcin "Cozoob" Kozub 27.06.2021
# Zadanie 3. (ładowanie promu) Dana jest tablica A[n] z długościami samochodów, które stoją w kolejce,
# żeby wjechać na prom. Prom ma dwa pasy (lewy i prawy), oba długości L. Proszę napisać program, który
# wyznacza, które samochody powinny pojechać na który pas, żeby na promie zmieściło się jak najwięcej aut.
# Auta muszą wjeżdżac w takiej kolejności, w jakiej są podane w tablicy A.

def _rek(i, left, right, F, A, L):
    if i < 0:
        return False
    if F[i][left][right] is not None:
        return F[i][left][right]

    flag = False
    if left + A[i - 1] <= L:
        flag = (flag or _rek(i - 1, left + A[i - 1], right, F, A, L))
    if not flag and right + A[i - 1] <= L:
        flag = (flag or _rek(i - 1, left, right + A[i - 1], F, A, L))

    F[i][left][right] = flag

    return flag


def cars(A, L):
    n = len(A)

    F = [[[None for _ in range(L + 1)] for _ in range(L + 1)] for _ in range(n + 1)]

    F[0][L][L] = True

    for i in range(n, -1, -1):
        for left in range(L + 1):
            for right in range(L + 1):
                if _rek(i, left, right, F, A, L):
                    get_solution(i, left, right, F, A, L)
                    return i

def get_solution(i, left, right, F, A, L):
    if i > 0:
        if left + A[i - 1] <= L and F[i - 1][left + A[i-1]][right]:
            get_solution(i - 1, left + A[i - 1], right, F, A, L)
            print(i, ": L", sep='')
        elif right + A[i - 1] <= L and F[i - 1][left][right + A[i - 1]]:
            get_solution(i - 1, left, right + A[i - 1], F, A, L)
            print(i, ": R", sep='')


if __name__ == '__main__':
    # dla L = 10
    A = [10, 2, 5, 8, 1, 1, 1]
    F = cars(A, 10)
    print(F)
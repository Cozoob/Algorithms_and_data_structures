# Created by Marcin "Cozoob" Kozub 15.05.2021
# Zadanie 2. (problem sumy podzbioru) Dana jest tablica n liczb naturalnych A. Proszę podać i zaimplementować algorytm,
# który sprawdza, czy da się wybrać podciąg liczb z A, które sumują się do zadanej wartości T.
# f(i, s) - czy uzywajac pierwszych i liczb jestesmy w stanie stworzyc sume s
# f(i, s) = f(i - 1, s) or f(i - 1, s - A[i]) or s == A[i]

def check_sum(A, T):
    n = len(A)
    # Indeksy wierszy w F to indeksy liczb w A
    F = [[False for _ in range(T + 1)] for _ in range(n)]
    # sprawdzam czy w tablicy A jest element rowny 0
    for i in range(n):
        if A[i] == 0:
            F[i][0] = True
    # sprawdzam gdzie w sa ciagi dlugocsi 1
    for i in range(T + 1):
        if A[0] == i:
            if A[0] == T:
                return True
            else:
                F[0][i] = True

    for i in range(1, n):
        for s in range(1, T + 1):
            F[i][s] = (F[i - 1][s] or A[i] == s)
            if s - A[i] >= 0:
                F[i][s] = (F[i][s] or F[i - 1][s - A[i]])


    return F[n - 1][T]

if __name__ == '__main__':
    A = [4, 234, 5, 6346, 45, 745, 7, 45, 7, 0, 2]
    B = [2, 4, 6]
    T = 8
    print(check_sum(B, T), T)
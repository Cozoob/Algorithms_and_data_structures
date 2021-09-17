# Created by Marcin "Cozoob" Kozub 23.06.2021
# Rozwiazanie dynamiczne
# Przyjmujemy ze rozwiazaniem moze byc pusty ciag rowny 0.

# f(i) - maksymalna wartosc rozwiazan konczacych sie na elemencie i
# f(i) = max( f(i - 1) + A[i], 0)

def ssp(T):
    n = len(T)
    res = 0
    partial = 0
    for i in range(n):
        partial += T[i]
        partial = max(partial, 0)
        res = max(res, partial)
    return res

if __name__ == '__main__':
    T = [7, -10, 2, 5, 3, -1, 8, -100, 2]
    print(ssp(T))
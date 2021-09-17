# Created by Marcin "Cozoob" Kozub 16.05.2021
# Zadanie 6. (wydawanie monet) Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T.
# Proszę podać algorytm, który oblicza minimalną ilość monet potrzebną do wydania kwoty T (algorytm zachłanny,
# wydający najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda kwotę 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5).

# f(i) - minimalna ilosc monet jaka musze uzyc aby wydac kwote i
# f(i) = min( f(i - c1) + 1, f(i - c2) + 1, ..., f(i - cn) + 1 : i >= c1, c2, ... , cn), gdzie c1, c2, ..., cn to monety
# f(0) = 0

# Do obliczenia zlozonosci len(A) = n
# Calkowicie zlozonosc:
# 1. czasowa O(T*n) ALE T >> n wiec mozna zalozyc ze O(T)
# 2. pamieciowa O(T)
def count_coins(A, T):
    # czasowa: O(n)
    inf = T + sum(A)
    # czasowa: O(T)
    # pamieciowa: O(T)
    F = [inf for _ in range(T+1)]
    F[0] = 0

    # czasowa: O(T*n)
    # uzupelniam reszte tablicy F
    for i in range(1, T + 1):
        # sprawdzam ktorego coina moge uzyc
        for coin in A:
            if i - coin >= 0:
                F[i] = min(F[i], F[i - coin] + 1)

    # czasowa: O(n)
    get_solution(T, A, F)
    print()

    return F[T]

def get_solution(i, A, F):
    if i == 0:
        return
    for coin in A:
        if F[i] == F[i - coin] + 1:
            print(coin, end=' ')
            get_solution(i - coin, A, F)
            break



if __name__ == '__main__':
    A1 = [1, 5, 8]
    T1 = 15
    print(count_coins(A1, T1))
    A2 = [1, 2, 5]
    T2 = 18
    print(count_coins(A2, T2))
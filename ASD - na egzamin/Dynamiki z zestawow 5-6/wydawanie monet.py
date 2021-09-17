# Created by Marcin "Cozoob" Kozub 27.06.2021
# Zadanie 6. (wydawanie monet) Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju,
# oraz kwotę T. Proszę podać algorytm, który oblicza minimalną ilość monet potrzebną do wydania
# kwoty T (algorytm zachłanny, wydający najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda
# kwotę 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5).

# XD coins2 zakladaja ze jest ograniczona ilosc monet
# f(i, T) - minimalna ilosc monet (gdzie ilosc monet jest ograniczona) z przedzialu od 0 do i potrzebna do wydania kwoty T.
# f(i, T) = min( f(i - 1, T), f(i - 1, T - A[i]) + 1) : T - A[i] >=0 )
# f(i, 0) = 0
# f(i, A[i]) = 1

def coins2(A, T):
    n = len(A)
    T_max = max(A)
    T_max = max(T_max, T)
    inf = float("inf")
    F = [[inf for _ in range(T_max + 1)] for _ in range(n)]
    S = [[-1 for _ in range(T_max + 1)] for _ in range(n)]


    for i in range(n):
        F[i][0] = 0
        F[i][A[i]] = 1
        S[i][0] = 0
        S[i][A[i]] = 0

    for i in range(1, n):
        for t in range(1, T_max + 1):
            F[i][t] = min(F[i-1][t], F[i][t])


            if t - A[i] >= 0 and F[i][t] > F[i - 1][t - A[i]] + 1:
                F[i][t] = F[i - 1][t - A[i]] + 1
                S[i][t] = t - A[i]

    res = get_solution2(A, T, S)

    if F[n - 1][T] == inf:
        F[n - 1][T] = "Nie da sie"

    return F[n - 1][T], res


def get_solution2(A, T, S):
    n = len(A)
    res = []

    k = -1
    for i in range(n - 1, -1, -1):
        if S[i][T] != -1:
            k = i
            break

    if k == -1:
        return []


    while k > - 1 and T > 0:
        res.append(A[k])
        T -= A[k]
        k -= 1
        while k > -1 and S[k][T] == -1:
            k -= 1

    return res[::-1]

# f(T) - minimalna ilosc monet potrzebna do wydania T
# f(0) = 0
# f(T) = min( f(T - A[0]), f(T - A[1]), ... f(T - A[i]) : T - A[i] >= 0)
# f(A[i]) = 1

def coins1(A, T):
    n = len(A)
    T_max = max(A)
    T_max = max(T_max, T)
    inf = float("inf")
    F = [ inf for _ in range(T_max + 1)]
    S = [-1 for _ in range(T_max + 1)]

    F[0] = 0
    for i in range(n):
        F[A[i]] = 1


    for t in range(T_max + 1):
        for i in range(n):
            if t - A[i] >= 0 and F[t] > F[t - A[i]] + 1:
                F[t] = F[t - A[i]] + 1
                S[t] = t - A[i]

    res = get_solution1(T, S)
    if F[T] == inf:
        return "Nie da sie"

    return F[T], res


def get_solution1(T, S):
    res = []

    if S[T] == -1:
        return [T]

    while T > 0:
        if S[T] != -1:
            elem = T - S[T]
        else:
            elem = T
        res.append(elem)
        T = S[T]


    return res

if __name__ == '__main__':
    A = [1,5,8]
    print(coins1(A, 2))
    print(coins1(A, 6))
    print(coins1(A, 7))
    print(coins1(A, 9))
    print(coins1(A, 13))
    print(coins1(A, 14))
    print(coins1(A, 15))
    print(coins1(A, 47))
    # F, H = coins1(A, 47)
    #
    # print(F)
    # print()
    # print(H)


    # print(coins2(A, 2))
    # print(coins2(A, 6))
    # print(coins2(A, 7))
    # print(coins2(A, 9))
    # print(coins2(A, 13))
    # print(coins2(A, 14))
    # print(coins2(A, 15))
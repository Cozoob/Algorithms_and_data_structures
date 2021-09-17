# Created by Marcin "Cozoob" Kozub 16.05.2021
# Zadanie 5. (maximin) Rozważmy ciąg (a0, . . . , an−1) liczb naturalnych. Załóżmy, że został podzielony
# na k spójnych podciągów: (a0, . . . , a`1), (a`1+1, . . . , a`2), . . . , (a`k−1+1, . . . , an−1). Przez wartość i-go podciągu
# rozumiemy sumę jego elementów a przez najgorszy podciąg rozumiemy podciąg o najmniejszej wartości (rozstrzygając remisy w dowolny sposób).
# Wartością podziału jest wartość jego najgorszego podciągu. Zadanie
# polega na znalezienie podziału ciągu (a0, . . . , an−1) o maksymalnej wartości.

# f(k) - podział i-tego ciągu na k spójnych podciągów tak, że i-ty ciąg ma maksymalną wartość
# f(1) = sum(A), tzn. wartosc ciagu A przy podziale na 1 spojny podciag to po prostu suma wszystkich jego elementow
# f(k) = max( min( f(k - 1) - x1, x1), min( f(k - 1) - (x1 + x2), x1 + x2), ..., min( f(k - 1) - (x1 + x2 + .. +xn), x1 + x2 + .. +xn ),
# min( f(k - 1) - xn, xn), min( f(k - 1) - (xn-1 + xn), xn-1 + xn), ... ) : f(k - 1) >= (x1 + x2 + .. +xn) )
# gdzie x1, x2, ... , xn to kolejne wyrazu w ciagu A

def sum_range(A, i, j):
    curr_sum = 0
    for a in range(i, j + 1):
        curr_sum += A[a]
    return curr_sum

def _rec(i, t, F, A, inf):
    if F[i][t] != -1:
        return F[i][t]

    best = -inf
    # sprawdzam wartosci gdy podzialow bylo o 1 mniej dla ciagu dlugosci i - j
    for j in range(1, i):
        q = min(_rec(i-j, t - 1, F, A, inf), sum_range(A, i - j + 1, i))
        if best < q:
            best = q

    F[i][t] = best
    return best

def maximin(A, k):
    n = len(A)
    inf = 2 * sum(A)
    F = [[-1 for _ in range(k + 1)]for _ in range(n)]
    # uzupelniam moja tablice F poczatkowymi wartosciami
    curr_sum = 0
    for i in range(n):
        curr_sum += A[i]
        F[i][1] = curr_sum

    # rekurencyjnie szukam najlepszego podzialu ciagu
    # dlugosci n-1, na k podzialow
    best = _rec(n - 1, k, F, A, inf)


    return F, best

if __name__ == '__main__':
    A = [2, 5, 7, 3, 1, 8, 10]
    k = 3
    print(maximin(A, k))
    # A = [5, 2, 7, 1, 6, 3, 8, 4, 2, 7]
    # k = 4
    # print(maximin(A, k))
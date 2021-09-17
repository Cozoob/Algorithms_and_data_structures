# Created by Marcin "Cozoob" Kozub 27.06.2021

# Zadanie 5. (maximin) Rozważmy ciąg (a0, . . . , an−1) liczb naturalnych. Załóżmy, że został podzielony
# na k spójnych podciągów: (a0, . . . , a`1
# ), (a`1+1, . . . , a`2
# ), . . . , (a`k−1+1, . . . , an−1). Przez wartość i-go podciągu
# rozumiemy sumę jego elementów a przez najgorszy podciąg rozumiemy podciąg o najmniejszej wartości
# (rozstrzygając remisy w dowolny sposób). Wartością podziału jest wartość jego najgorszego podciągu.
# Zadanie polega na znalezienie podziału ciągu (a0, . . . , an−1) o maksymalnej wartości.


# f(i, k) - maksymalna wartosc podzialu ciagu od 0 do i na k spojnych podciagow
# f(i,k) = max( min( f(i - 1, k - 1 ), A[i]) , f(i - 1, k) + A[i] )
# f(i, 0) = 0
# f(0, 1) = A[0]
# f(i,1) = A[i] + f(i - 1, 1), i > 0



def max_and_min(A, k):
    n = len(A)

    F = [[0 for _ in range(k + 1)] for _ in range(n)]
    F[0][1] = A[0]
    for i in range(n):
        F[i][1] = F[i - 1][1] + A[i]

    for i in range(1, n):
        for j in range(2, k + 1):
            if j == i + 1:
                F[i][j] = min(F[i][j - 1], A[i])
            if j > i + 1:
                continue

            F[i][j] = max(min(F[i - 1][j - 1], A[i]), F[i - 1][j] + A[i])


    return F

if __name__ == '__main__':
    A = [1, 5, 3, 8, 9, 10 ,11]
    H = max_and_min(A, 3)
    for elem in H:
        print(elem)
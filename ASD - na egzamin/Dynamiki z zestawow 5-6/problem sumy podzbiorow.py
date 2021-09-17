# Created by Marcin "Cozoob" Kozub 27.06.2021
# Zadanie 2. (problem sumy podzbioru) Dana jest tablica n liczb naturalnych A.
# Proszę podać i zaimplementować algorytm, który sprawdza, czy da się wybrać podciąg liczb z A,
# które sumują się do zadanej
# wartości T.

# f(i,T) - czy da sie zsumowac (niespojny moze byc) podciag liczb z przedzialu od 0 do i
# tak, aby uzyskac sume T
# f(i, T) = f(i - 1, T - A[i]) or f(i-1, T) , gdy T-A[i] >= 0

# f(i, A[i]) = True
# f(i, 0) = True

def is_there_the_sum(A, T):
    n = len(A)
    T_max = max(A)
    T_max = max(T, T_max)
    F = [[False for _ in range(T_max + 1)] for _ in range(n)]

    for i in range(n):
        F[i][A[i]] = True
        F[i][0] = True

    for i in range(1, n):
        for t in range(1, T_max + 1):
            F[i][t] = F[i - 1][t] or F[i][t]

            if t - A[i] >= 0:
                F[i][t] = F[i][t] or F[i - 1][t - A[i]]


    return F[n - 1][T]

if __name__ == '__main__':
    A = [1, 2, 5, 10, 99]
    H = is_there_the_sum(A, 104)

    print(H)
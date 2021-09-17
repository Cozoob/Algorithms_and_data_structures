# Created by Marcin "Cozoob" Kozub 19.05.2021

# Zadanie 2. (problem sumy podzbioru) Dana jest tablica n liczb naturalnych A. Prosze podac i zaimplementowac
# algorytm, który sprawdza, czy da sie wybrac podciag liczb z A, które sumuja sie do zadanej
# wartosci T.

# f(i, x) - czy istnieje podciąg liczb w tablicy o dlugosci x, ktory sumuje sie do i
# f(i, x) = f(i - A[0]) or f(i - A[1]) or ... or f(i - A[x]), gdzie x != i
# f(O, x) = True
# f(A[x], x) = True
# wynik: f(T, x)


def find_subsequence(A, T):
    n = len(A)
    max_S = sum(A)
    if T > max_S:
        return False
    if T == max_S:
        return True, A

    F = [False for _ in range(max_S + 1)]
    F[0] = True
    for i in range(n):
        F[A[i]] = True

    for s in range(max_S + 1):
        for i in range(n):
            if s - A[i] != A[i] and s - A[i] > -1:
                F[s] = F[s] or F[s - A[i]]

    if F[T] == False:
        return False

    # res = get_solution(A, F, T)

    return F

def get_solution(F, A, i):
    if i == 0:
        return []

    for x in range(len(A)):
        if F[i - A[x]] == True:
            return get_solution(F, A, i - A[x]) + [A[x]]


if __name__ == '__main__':
    A0 = [3, 2, 8]
    print(find_subsequence(A0, 10))

    # A = [7, 6, 4, 5, 9, 10, 8]
    # print(find_subsequence(A, 8))
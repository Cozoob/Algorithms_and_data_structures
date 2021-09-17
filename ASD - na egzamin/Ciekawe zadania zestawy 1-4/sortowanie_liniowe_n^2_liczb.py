# Created by Marcin "Cozoob" Kozub 25.06.2021
# Zadanie 1. Proszę zaproponować algorytm, który w czasie liniowym sortuje tablicę A zawierającą n liczb
# ze zbioru 0, . . . , n2 − 1.

# Zauwazmy ze kazda liczbe i z tego zbioru mozemy podzielic na i = a * n + b, gdzie a = i // n , b = i % n
# Np. n = 6, n^2 - 1 = 35, dla i = 25, mamy a = 4, b = 1, czyli i = 4 * 6 +  1 = 25

# Dzieki temu mozemu uzyc radixsorta ktory posortuje nam liczby po ich skladnikach tzn. po b a pozniej po a.

# O(n)

def amazing_sort(A):
    n = len(A)

    # wiec najpierw sortuje po b przy uzyciu countingsorta
    C = [0 for _ in range(n)]
    B = [0 for _ in range(n)]

    for i in range(n):
        C[A[i] % n] += 1

    for i in range(1, n):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        C[A[i] % n] -= 1
        B[C[A[i] % n]] = A[i]

    for i in range(n):
        A[i] = B[i]

    # to samo tylko ze po a
    C = [0 for _ in range(n)]
    B = [0 for _ in range(n)]

    for i in range(n):
        C[A[i] // n] += 1

    for i in range(1, n):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        C[A[i] // n] -= 1
        B[C[A[i] // n]] = A[i]

    for i in range(n):
        A[i] = B[i]

if __name__ == '__main__':
    # dla n = 6 tzn wartosci: 0, ..., 35
    T1 = [5, 1, 4, 5, 25, 35]
    T2 = [9, 3, 4, 2, 5, 18]
    T3 = [6, 21, 20, 15, 17, 31]
    amazing_sort(T1)
    print(T1)
    amazing_sort(T2)
    print(T2)
    amazing_sort(T3)
    print(T3)
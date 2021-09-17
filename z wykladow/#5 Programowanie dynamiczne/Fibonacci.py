# Created by Marcin "Cozoob" Kozub at 10.04.2021 18:32

def Fib(n):
    if n <= 1:
        return 1
    return Fib(n - 1) + Fib(n - 2)

def FibDP(n):
    arr = [1 for _ in range(n + 1)]
    for j in range(2, n + 1):
        arr[j] = arr[j - 1] + arr[j - 2]
    return arr[n]

def FibBetterDP(n):
    if n <= 1:
        return 1
    F1 = 1
    F2 = 1
    for j in range(2, n + 1):
        F = F1 + F2
        F1 = F2
        F2 = F
    return F

def FibMem(n):
    arr = [0 for _ in range(n + 1)]
    arr[0] = 1
    arr[1] = 1

    def rec_FibMem(n, arr):
        if arr[n] > 0:
            return arr[n]
        arr[n] = rec_FibMem(n - 1, arr) + rec_FibMem(n - 2, arr)
        return arr[n]

    return rec_FibMem(n, arr)

if __name__ == '__main__':
    # Przyjmujemy, że Fib0 = 1, Fib1 = 1
    print(FibBetterDP(10))
    print(FibMem(10))
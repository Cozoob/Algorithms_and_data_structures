# Created by Marcin "Cozoob" Kozub at 03.04.2021 18:57

def bottom_up_fib(n):
    if n == 0: return 0
    if n == 1 or n == 2: return 1
    r = [0 for _ in range(n + 1)]
    r[1], r[2] = 1, 1
    for i in range(3, n + 1):
        r[i] = r[i - 1] + r[i - 2]
    return r[n]


if __name__ == '__main__':
    print(bottom_up_fib(11))
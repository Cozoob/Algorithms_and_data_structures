# Created by Marcin "Cozoob" Kozub at 03.04.2021 18:34

def extended_bottom_up_cut_rod(p, n, c):
    r = [0 for _ in range(n + 1)]
    s = [0 for _ in range(n + 1)]
    r[0] = 0
    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            if i == len(p):
                break
            if q < p[i] + r[j-i] - c:
                q = p[i] + r[j - i] - c
                s[j] = i
        if q != -1:
            r[j] = q
    return r, s

def print_cut_rod_solution(p, n, c):
    r, s = extended_bottom_up_cut_rod(p, n, c)
    while n > 0:
        if s[n] == 0:
            break
        print(s[n], end=' ')
        n = n - s[n]

if __name__ == '__main__':

    # tablica p; i-ty indeks to dlugosc i;
    # pod i-tym indeksem cena preta dlugosci i
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    # n liczba calkowita/ dlugosc preta ktory ma byc pociety
    for i in range(3, 16):
        print("Na podział ",i)
        print_cut_rod_solution(p, i, 3)
        print()
        print("--------")
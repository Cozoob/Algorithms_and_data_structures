
def memoized_cut_rod(p, n):
    # r nowa tablica ktora bedzie zapamietywac wyniki
    r = [0 for _ in range(n + 1)]
    for i in range(n + 1):
        r[i] = -1
    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p ,n ,r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1, n + 1):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, r))
    r[n] = q
    return q


if __name__ == '__main__':
    # tablica p; i-ty indeks to dlugosc i;
    # pod i-tym indeksem cena preta dlugosci i
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    # n liczba calkowita/ dlugosc preta ktory ma byc pociety
    for i in range(1, 11):
        print(i)
        print(memoized_cut_rod(p, i))
        print("---")
    # od 11 zaczyna sie problem
    # maximum rec...
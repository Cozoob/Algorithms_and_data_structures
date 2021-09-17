# rekurencyjna implementacja rozcninania pręta
# blad... maximum rec depth

def cut_rod(p, n):
    if n == 0:
        return 0
    q = -1
    for i in range(n + 1):
        q = max(q, p[i] + cut_rod(p, n - i))
    return q

if __name__ == '__main__':

    # tablica p; i-ty indeks to dlugosc i;
    # pod i-tym indeksem cena preta dlugosci i
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    # n liczba calkowita/ dlugosc preta ktory ma byc pociety
    print(cut_rod(p,1))
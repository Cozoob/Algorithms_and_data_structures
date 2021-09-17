# cosik nie dziala xd

def bottom_up_cut_rod(p, n):
    r = [0 for _ in range(n + 1)]
    r[0] = 0
    for j in range(1, n + 1):
        q = -1

        if j == 1:
            q = max(q, p[j] + r[0])

        for i in range(1, j + 1):
            if i == len(p):
                break
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]

if __name__ == '__main__':

    # tablica p; i-ty indeks to dlugosc i;
    # pod i-tym indeksem cena preta dlugosci i
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    # n liczba calkowita/ dlugosc preta ktory ma byc pociety
    for i in range(1, 15):
        print("Dla podzialu na",i)
        print(bottom_up_cut_rod(p, i))
        print("--------")

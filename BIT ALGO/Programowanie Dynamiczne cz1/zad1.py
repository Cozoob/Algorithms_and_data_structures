# Created by Marcin "Cozoob" Kozub at 16.04.2021 22:47

# Firma kupuje długie stalowe pręty i tnie je na kawałki, które sprzedaje.
# Kawałki mają długość w metrach wyrażoną zawsze liczbą naturalną.
# Dla kawałka długości n metrów znane są ceny kawałków długości 1, 2, …, n metrów.
# Firma chce znać maksymalny zysk, który może uzyskać z pocięcia i sprzedania pręta długości n.

# f(i,j) - max zysk jaki mozna uzyskac z pociecia preta o dlugosci i ucinajac go o j dlugosci
# f(i, j) = max( f(i - j), f(i - j) + C[j])
# 0 <= i < j
# f(0) = 0

# Dane:
# n - dlugosc preta do pociecia
# C - tablica zyskow
# Liczone:
# P - tablica w ktorej zapisywane beda odpowiedzi do podproblemow
# dla preta o dlugosci n
# P[n] szukana wartosc
def cut_rod(n, C, P):
    if n <= 0:
        return 0
    for i in range(1, n + 2):
        curr_price = -1
        for k in range(i):
            if curr_price < P[i - k - 1] + C[k]:
                curr_price = P[i - k - 1] + C[k]
        P[i - 1] = curr_price

    return P[n]

def cut_rod2(n, C):
    if n <= 0:
        return 0
    max_price = 0
    for i in range(1, n + 1):
        max_price = max(max_price, cut_rod2(n - i, C) + C[i])

    return max_price


if __name__ == '__main__':
    C = [0, 3, 5, 8, 9, 10, 17, 17, 20]
    A = [0, 1, 5, 8, 9, 10, 17, 17, 20]
    n = 8
    P = [0 for _ in range(n + 1)]
    print(cut_rod(n, A, P))
    print(cut_rod2(n, C))
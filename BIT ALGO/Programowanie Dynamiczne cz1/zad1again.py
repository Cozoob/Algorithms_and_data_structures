# Created by Marcin "Cozoob" Kozub at 21.04.2021 01:09
# Firma kupuje długie stalowe pręty i tnie je na kawałki, które sprzedaje.
# Kawałki mają długość w metrach wyrażoną zawsze liczbą naturalną.
# Dla kawałka długości n metrów znane są ceny kawałków długości 1, 2, …, n metrów.
# Firma chce znać maksymalny zysk, który może uzyskać z pocięcia i sprzedania pręta długości n.


# f(i,j) - max zysk jaki mozna uzyskac z pociacia preta o dlugosci i ucinajac go o j dlugosci
# f(i, j) = max( f(i - j), f(i - j) + C[j])
# 0 <= i < j
# f(0) = 0

def cut_rod(n, C):
    # tworze sobie pomocnicza tablice do ktorej bede spisywac
    # rozwiazania podproblemow
    P = [0 for _ in range(n+1)]

    # uzupelniam tablice podproblemow
    for i in range(1, n+1):
        # ustawiam profit na najmniejsza wartosc
        profit = -1
        # ide po tablicy zyskow i wybieram opcje ktora
        # da mi najwiekszy profit po odcieciu od preta  o dlugosci
        # i dlugosc j
        for j in range(i + 1):
            if profit < P[i-j] + C[j]:
                # jesli mi sie oplaca to przypisuje
                profit = P[i-j] + C[j]
        # po przejsciu calej petli wiem ze znalazlem
        # najwiekszy profit jaki moglem wiec przypisuje
        # go jako rozwiazania podproblemu dla preta o dlugosci i
        P[i] = profit

    # odpowiedz znajde na koncu tablicy P
    return P[n]

if __name__ == '__main__':
  C = [0, 3, 5, 8, 9, 10, 17, 17, 20]
  A = [0, 1, 5, 8, 9, 10, 17, 17, 20]
  n = 5
  print(cut_rod(n, A))
  print(cut_rod(n, C))
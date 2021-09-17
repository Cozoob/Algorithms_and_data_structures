# Created by Marcin "Cozoob" Kozub at 22.04.2021 23:44

# Zmodyfikuj rozwiązanie problemu cięcia stalowych prętów tak, aby konstruowało
# i zwracało także rozwiązanie, tj. listę długości prętów o największej cenie.
# Podpowiedź: bottom-up będzie łatwiej

def cut_rod(n, C):
    # tworze sobie pomocnicza tablice do ktorej bede spisywac
    # rozwiazania podproblemow
    P = [0 for _ in range(n+1)]
    # tworze dodatkowa tablice result ktora bedzie
    # zapisywac pod indektem i jaka dlugosc j ucialem
    # gdy pret mial dlugosc i
    result = [0 for _ in range(n+1)]


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
                # zapisuje dodatkowo do result jaka dlugosc j ucialem z tego preta dlugosci i
                result[i] = j

        # po przejsciu calej petli wiem ze znalazlem
        # najwiekszy profit jaki moglem wiec przypisuje
        # go jako rozwiazania podproblemu dla preta o dlugosci i
        P[i] = profit


    # przed zwroceniem wartosci wypisuje jescze dlugosci pocietych czesci pretu
    i = n
    while i > 0:
        print(result[i], end=',')
        i -= result[i]
    print()

    # odpowiedz znajde na koncu tablicy P
    return P[n]

if __name__ == '__main__':
  C = [0, 3, 5, 8, 9, 10, 17, 17, 20]
  A = [0, 1, 5, 8, 9, 10, 17, 17, 20]
  n = 5
  print(cut_rod(n, A))
  print(cut_rod(n, C))
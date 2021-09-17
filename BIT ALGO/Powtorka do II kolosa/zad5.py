# Created by Marcin "Cozoob" Kozub 17.05.2021
# Cersei i Jaime mają 3 - letniego syna. Przygotowali listę N aktywności podanych jako pary, reprezentujące czas rozpoczęcia
# i zakończenia danej aktywności. Zaimplementuj algorytm, który przyporządkuje każdej aktywności literę C lub J, oznaczającą,
# że daną aktywność z synem wykona odpowiednio Cersei lub Jaime, w taki sposób, że żaden rodzic nie wykonuje pokrywających się czasowo aktywności.
# Jeżeli takie przyporządkowanie nie istnieje, to algorytm zwraca “IMPOSSIBLE”, a jeśli istnieje, to zwraca odpowiedniego stringa.
# Przykładowo: (99, 150), (1, 100), (100, 301), (2,5), (150, 250) - odpowiedź to JCCJJ (lub CJJCC).
#
# Pomysł: Sortujemy kazda katywnosc po poczatkach i idac od lewej do prawej przypisujemy jednemu rodzicow jedna aktywnosc,
# gdy przetna sie dwie aktywnosci to druga aktywnosc dostaje drugi rodzic, zas gdy przetna sie 3 aktywnosci na raz mozemy wypisac
# IMPOSSIBLE, bo nie jest mozliwe zeby dwaj rodzice 3 aktywnosciami na raz sie zajeli.

def activities(A):
    n = len(A)
    A.sort(key=lambda x: x[0])
    answer = ['' for _ in range(n)]

    # niech pierwsza aktywnosc zawsze zaczyna Cersei
    answer[0] = 'C'
    # timeC oraz timeJ oznacza czas zakonczenia aktywnosci ktora aktualnie robia
    # Cersei albo Jaime; -1 oznacza ze nie zajmuje sie niczym
    timeC = A[0][1]
    timeJ = -1
    for i in range(1, n):
        activity = A[i]
        if activity[0] >= timeC:
            # to oznacza ze Cersei moze sie zajac ta aktywnoscia
            timeC = activity[1]
            answer[i] = 'C'
        elif activity[0] >= timeJ:
            # to oznacza ze Jaime moze sie zajac ta aktywnoscia
            timeJ = activity[1]
            answer[i] = 'J'
        else:
            # jesli zaden rodzic nie moze sie zajac aktywnoscia bo musze
            # sie zajmowac innymi to mamy 3 przecinajace sie aktywnosci
            # i zwracamy IMPOSSIBLE
            return 'IMPOSSIBLE'

    return answer

if __name__ == '__main__':
    # OK
    A = [(99, 150), (1, 100), (100, 301), (2,5), (150, 250)]
    print(activities(A))
    # IMPOSSIBLE
    A = [(99, 150), (1, 100), (100, 301), (2, 5), (105, 108), (150, 250)]
    print(activities(A))
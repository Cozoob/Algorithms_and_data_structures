# Created by Marcin "Cozoob" Kozub at 25.04.2021 15:52

# Mamy dany pewien rozkład pociągów, dany jako tablica n krotek (arrival_time, departure_time),
# przy czym są one posortowane niemalejąco według arrival_time. Chcemy wiedzieć, czy nasza stacja mająca m peronów
# jest w stanie bezkonfliktowo obsłużyć te pociągi, tzn. w żadnym momencie nie będzie “rywalizacji” pociągów o dostępne perony.
# Przedstaw algorytm, który poda odpowiedź True lub False na powyższe pytanie.

# Pomysł: liczę ile pociagow znajduje sie na stacji w czasie od t_i do t_i+1, gdzie 0 <= i

# zlozonosc czasowa: O(nlgn) - sortowanie (S.sort())
# zlozonosc pamieciowa: O(n)

def check_perons(A, m):
    n = len(A)
    # rozdzielam arr_time oraz dep_time kazdego pociagu do krotek gdzie: (arr_time, 1), (dep_time, -1)
    # do tablicy S rozmiarze 2n
    S = [0 for _ in range(2*n)]
    j = 0
    for i in range(n):
        S[j] = (A[i][0], 1)
        j += 1
        S[j] = (A[i][1], -1)
        j += 1
    # sortuje kroti w tablicy S
    S.sort()
    # dzieki temu caly czas bede w stanie zliczac ile pociagow sie znajduje na peronach
    # po prostu do countera dodaje caly czas drugi element z krotek
    counter = 0
    for i in range(2*n):
        counter += S[i][1]
        if counter > m:
            return False

    return True

if __name__ == '__main__':
    m = 2
    A = [(1,3), (1.2, 2), (1.5, 3.3), (2,6)] # dla m <= 2 False dla m > 2 True
    print(check_perons(A, m))
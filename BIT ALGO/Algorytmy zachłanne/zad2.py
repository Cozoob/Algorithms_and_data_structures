# Created by Marcin "Cozoob" Kozub at 25.04.2021 14:37

# W problemie coin change mamy daną kwotę X i chcemy ją rozmienić na monety o wartości 1, 5, 10, 25 i 100.
# Podaj algorytm, który obliczy, ile minimalnie monet trzeba użyć do wydania reszty oraz ile sztuk każdej monety będzie trzeba użyć.
# Można założyć, że każdej monety mamy nieskończenie wiele sztuk.
# Czy algorytm zachłanny działa dla zestawu monet 1, 2, 7, 10? Jeśli tak, uzasadnij dlaczego. Jeśli nie, podaj kontrprzykład.

# działa wtw gdy dla kazdego i-ego elementu w tablicy A istnieje stosunek A[i + 1] / A[i] >= 2
# np dla tablicy [1,5,10,25,100]: 5/1 ok, 10/5 ok 25/10 ok 100 / 25 ok
# np dla tablicy [1,2,7,10]: 2/1 ok, 7/2 ok 10/7 NIE OK - tu alg niepoprawny

# zlozonosc czasowa: O(n)
# zlozonosci pamieciowa: O(1)

def coin_change(A, x):
    counter = 0
    n = len(A) - 1

    while x > 0:
        while x >= A[n]:
            x -= A[n]
            counter += 1
        n -= 1
    return counter

if __name__ == '__main__':
    A = [1,5,10,25,100]
    x = 1126
    print(coin_change(A, x)) # alg daje poprawny wynik

    B = [1,2,7,10]
    d = 126
    print(coin_change(B, d)) # alg daje nieporawny wynik
# Cyfra jednokrotna to taka, która wystepuje w danej liczbie dokładnie jeden raz.
# Cyfra wielokrotna to taka, która w liczbie wystepuje wiecej niz jeden raz.
# Mowimy ze liczba naturalna A jest ladniejsza od liczby naturalnej B, jezeli
# W liczbe A wystepuje wiecej cyfr jednokrotnych niz w B, a jezeli cyfr
# jednokrotnych jest tyle samo to ładniejsza jest ta liczba, ktora posiada
# mniej cyfr wielokrotnych.
# Na przykład: liczba 123 jest ladniejsza od 455, liczba 1266 jest ladniejsza
# od 114577, a liczby 2344 i 67333 sa jednakowo ladne.

# Dana jest tablica T zawierajaca liczby naturalne. Prosze zaimplementowac
# funkcje pretty_sort(T), ktora sortuje elementy tablicy T od najładniejszych
# do najmniej ładnych. Użyty algorytm powinien byc mozliwie jak najszybszy.
# Prosze w rozwiazaniu umiescic 1-2 zdaniowy opis algorytmu oraz prosze
# oszacowac jego zlozonosc czasowa.

# Zapisuje w pomocniczej tablicy w tuplach liczbe z talbicy T oraz liczbe
# zbudowana z dwoch cyfr gdzie cyfra dziesiatek odpowiada ilosci cyfr
# jednokrotnych w liczbe z tablicy T zas cyfra jednosci odpowiada
# ilosci cyfr wielokrotnych w liczbie z tablicy T.
# Wykorzystuje radixsorta sortujac najpiew po cyfrach jednosci(wielokrotnych)
# a pozniej dziesiatek(jednokrotnych) i na koniec pod odpowiedni indeks
# przepisuje liczbe z tablicy T z tupli w odpowiednim miejscu do tablicy T.

import random

def pretty_sort(T):

    def count_digits(num):
        count = [0 for _ in range(10)]
        while num > 0:
            count[num % 10] += 1
            num //= 10
        # c1 zlicza jednokrotne cyfry
        # c2 zlicza wielokrotne cyfry
        c1 = 0
        c2 = 0
        for i in range(10):
            if count[i] == 1:
                c1 += 1
            elif count[i] > 1:
                c2 += 1

        return c1*10 + c2

    def countingsort(arr, exp1):
        n = len(arr)

        # The output array elements that will have sorted arr
        output = [0] * (n)

        # initialize count array as 0
        count = [0] * (10)

        # Store count of occurrences in count[]
        for i in range(0, n):
            index = (arr[i][1] // exp1)
            count[index % 10] += 1

        # Change count[i] so that count[i] now contains actual
        # position of this digit in output array
        for i in range(1, 10):
            count[i] += count[i - 1]

            # Build the output array
        i = n - 1
        while i >= 0:
            index = (arr[i][1] // exp1)
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        # Copying the output array to arr[],
        # so that arr now contains sorted numbers
        for i in range(0, len(arr)):
            arr[i] = output[i]

    def radixsort(array):
        # sortujemy najpierw od mniejszy waznych po wazniejsze cyfry w tym sortowaniu np
        # najpierw jednosci pozniej, dziesiatki, pozniej setki itd

        # Najwiecej cyfr to moze byc 2 (bo max od gornie to 100 kiedy bedzie 9876543210)
        biggest = 100


        # dokonuje countingsorta dla kazdej cyfry.
        exp = 1
        while biggest // exp > 0:
            countingsort(array, exp)
            exp *= 10

    A = [0 for _ in range(len(T))]
    for i in range(len(T)):
        A[i] = (T[i], count_digits(T[i]))

    radixsort(A)
    # i na sam koniec musze skopiowac elementy z A do T
    j = len(A) - 1
    for i in range(len(T)):
        T[i] = A[j]
        j -=1


if __name__ == '__main__':
    n = 10
    T = [random.randint(100,10000) for _ in range(n)]
    print(T)
    pretty_sort(T)
    print(T)


    A = [123, 455, 1266, 114577,2344,67333, 9876543210, 11002233445566778899]
    pretty_sort(A)
    print(A)
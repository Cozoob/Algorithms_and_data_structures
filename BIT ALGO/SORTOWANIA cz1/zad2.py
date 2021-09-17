# Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
# podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
# wzrostu. Proszę zaimplementować funkcję:
# section(T,p,q)
# która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową.

# Uzywam najpierw radixsorta z wykorzystaniem countingsorta do posortowania wzrostu
# zolnierzy a pozniej kopiuje do nowej tablicy wzrosty zolnierzy od p do q i zwracam nowa tablice.
# Zlozonosc to O(n)
import random

def countingsort(arr, exp1):
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i] // exp1)
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

        # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp1)
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

    # szukam najwieksze liczby zeby wiedziec ile maksymalnie moze byc cyfr w liczbach do sortowania
    biggest = 0
    for i in range(len(array)):
        if biggest < array[i]:
            biggest = array[i]

    # dokonuje countingsorta dla kazdej cyfry.
    exp = 1
    while biggest // exp > 0:
        countingsort(array, exp)
        exp *= 10

    # teraz tylko kopiuje do nowej tablicy i do array tak zeby
    # bylo posortowanie nierosnaco
    tmp = [0 for _ in range(len(array))]
    for k in range(len(array)):
        tmp[k] = array[k]
    j = len(array) - 1
    for i in range(len(array)):
        array[i] = tmp[j]
        j -= 1




def section(T, p, q):
    # sortuje tablice ze wzrostami zolnierzy
    radixsort(T)
    newT = [0 for _ in range(q - p + 1)]
    i = 0
    while p <= q:
        newT[i] = T[p]
        p += 1
        i += 1
    return newT

if __name__ == '__main__':
    n = 14
    T = [random.randint(99,300) for _ in range(n)]
    print(T)
    radixsort(T)
    print(T)
    print(section(T, 2, 6))
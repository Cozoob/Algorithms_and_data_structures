# Dana jest tablica A zawierajaca n parami róznych liczb. Prosze zaproponowac algorytm, który
# znajduje takie dwie liczby x i y z A, ze y − x jest jak najwieksza oraz w tablicy nie ma zadnej liczby z takiej,
# ze x < y < z (innymi słowy, po posortowaniu tablicy A rosnaco wynikiem byłyby liczby A[i] oraz A[i+1] dla
# których A[i + 1] − A[i] jest najwieksze).
import random

def function(A):

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

    # po posortowaniu liniowo tablicy radixsortem liniowo szukamy najwiekszej wartosci A[i + 1] - A[i]
    # i zapisujemy ich indeksy
    radixsort(A)
    maxval = 0
    idx = 0
    for i in range(len(A) - 1):
        if A[i + 1] - A[i] > maxval:
            maxval = A[i + 1] - A[i]
            idx = i

    return maxval, idx, idx + 1

if __name__ == '__main__':
    n = 12
    T = [random.randint(0,20) for _ in range(n)]
    print(T)
    print(function(T))
    print(T)
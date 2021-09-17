# Dana jest tablica A oraz liczba k. Znaleźć liczbę roznych par elementow z tablicy A
# o roznicy rownej k.

# sortuje radix sortem liniowo a pozniej przechodze liniowo po tablicy
# i sprawdzam czy dwa nastepne elementy maja roznice rowna k. Po posortowaniu
# na pewno bedzie to tez para roznych elementow
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

def findthepair(A, k):
    radixsort(A)
    counter = 0
    for i in range(len(A) - 1):
        if A[i + 1] - A[i] == k:
            counter += 1
    return counter

if __name__ == '__main__':
    n = 6
    T = [random.randint(0,5) for _ in range(n)]
    print(T)
    print(findthepair(T, 1))
    radixsort(T)
    print(T)
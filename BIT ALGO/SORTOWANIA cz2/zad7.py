# Mamy tablice puntkow (krotki z intami x,y). Punkt 1 dominuje punkt 2 gdy
# x1 > x2 i y1 > y2. Podaj liczność najmniejszego zbioru z nicg by wybrane punkty
# dominowały wszystkie pozostałe (ale nie siebie nawzajem).

# zlozonosc O(n)
# pomysl taki:
# 1. Sortujemy radixsortem liniowo po x-ach w tablicy krotki
# 2. Tworzymy zmienna start = 0 ktora sprawdza y-ki.
# 3. Idziemy od tylu tablicy i wiemy ze mamy najwiekszego x-a
# 4. Musimy sprawdzic czy element wczesniejszy ma rownego x i wiekszego y
# wtedy taki element dominuje element ostatni.
# 5. Element ktory ostatecznie dominuje (narazie) sprawdzamy czy start < y
# jesli tak to element NA PEWNO DOMINUJE start = y a element dopisuje do zbioru
# elementow ktore dominuja.
# 6. I tak przechodze az do konca tablicy.

def countingsort(arr, exp1):
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i][0] // exp1)
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

        # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i][0] // exp1)
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
        if biggest < array[i][0]:
            biggest = array[i][0]

    # dokonuje countingsorta dla kazdej cyfry.
    exp = 1
    while biggest // exp > 0:
        countingsort(array, exp)
        exp *= 10

def findtheset(A):
    radixsort(A)
    result = []
    start = 0
    for i in range(len(A) - 1, -1, -1):
        if i > 0 and A[i - 1][0] == A[i][0]:
            result.append(A[i])
            if A[i-1][1] < A[i][1] and A[i-1][1] > start:
                start = A[i-1][1]
            continue
        if start <= A[i][1]:
            start = A[i][1]
            result.append(A[i])

    return result



if __name__ == '__main__':
    A = [(3,2), (1,4), (2,8),(3,3),(4,2)]
    print(findtheset(A))
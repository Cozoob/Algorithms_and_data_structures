# Created by Marcin "Cozoob" Kozub 26.06.2021
# Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie jeden raz.
# Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz.
# Mówimy, że liczba naturalna A jest ładniejsza od liczby naturalnej B, jeżeli
# w liczbie A występuje więcej cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych
# jest tyle samo to ładniejsza jest ta liczba, która posiada mniej cyfr wielokrotnych.
# Na przykład: liczba 123 jest ładniejsza od 455, liczba 1266 jest ładniejsza od 114577,
# a liczby 2344 i 67333 są jednakowo ładne.
# Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
# pretty_sort(T), która sortuje elementy tablicy T od najładniejszych do najmniej ładnych.
# Użyty algorytm powinien  być  możliwie  jak  najszybszy.  Proszę  w  rozwiązaniu  umieścić
# 1-2  zdaniowy  opis algorytmu oraz proszę oszacować jego złożoność czasową.

# Na poczatku zapisujemy dodatkowe informacje w krotkach dla kazdej liczby tzn ile ma
# cyfr jednokrotnych i wielokrotnych. Nastepnie sortujemy przy pomocy radix sorta z pomoca countingsorta
# najpierw po ilosci wielokrotnych a pozniej po jednokrotnych. Zloznosc czasowa O(n). Pamieciowa O(n)


def countingsort(arr, exp1):
    n = len(arr)
    output = [0 for _ in range(n)]
    count = [0 for _ in range(10)]

    for i in range(0, n):
        index = (arr[i] // exp1)
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]


    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp1)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    for i in range(0, n):
        arr[i] = output[i]

def pretty_sort(arr):
    n = len(arr)

    for i in range(n):
        tmp = arr[i]
        counter1 = 0
        counter2 = 0
        count = [0 for _ in range(10)]
        while tmp > 0:
            count[tmp % 10] += 1
            tmp //= 10

        for j in range(10):
            if count[j] == 1:
                counter1 += 1
            if count[j] > 1:
                counter2 += 1

        arr[i] = (arr[i], counter1, counter2)

    #print(arr)
    output = [0 for _ in range(n)]
    count = [0 for _ in range(11)]

    for i in range(0, n):
        count[arr[i][2]] += 1

    for i in range(9, -1, -1):
        count[i] += count[i + 1]


    for i in range(n - 1, -1, -1):
        output[count[arr[i][2]] - 1] = arr[i]
        count[arr[i][2]] -= 1

    for i in range(0, n):
        arr[i] = output[i]
    #print(arr)

    output = [0 for _ in range(n)]
    count = [0 for _ in range(11)]

    for i in range(0, n):
        count[arr[i][1]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        output[count[arr[i][1]] - 1] = arr[i]
        count[arr[i][1]] -= 1

    for i in range(0, n):
        arr[n - i - 1] = output[i][0]
        #arr[n - i - 1] = output[i]





    return arr


if __name__ == '__main__':
    T = [123, 455, 1266, 114577, 2344, 67333]
    print(pretty_sort(T))
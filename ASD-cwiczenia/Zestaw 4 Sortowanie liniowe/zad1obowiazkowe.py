# Prosze zaproponowac jak najszybszy algorytm sortujacy
# n elementowa tablice zawierajaca liczby ze zbioru
# [0, 1, 2, ..., n^2 - 1]

# kazda k-ta liczbe w zbiorze moge przedstawic jako
# k = a*n^1 + b*n^0 gdzie a = k // n, b = k % n
# sortuje radixsortem przy pomocy countingsorta najpierw
# po b pozniej po a

# exp jako expansion
def radixsort(arr):
    # Zaczynam od szukania po mniej waznych wartosciach
    # tutaj mniej wazna wartoscia jest b
    n = len(arr)
    # Szukam najwiekszej liczby jaka moze byc w b jak i w a
    # a bedzie to po prostu n - 1 bo a i b moga przyjac wartosc
    # od 0 do n - 1
    biggest = n - 1

    # dokonuje counting sorta dla czesci b
    # liczby z tablicy
    exp = 1
    while biggest // exp > 0:
        # Countsortuje po b
        # Tworze tablice output
        output = [0 for _ in range(n)]
        # Oraz tworze tablice count do zliczania cyfr
        count = [0 for _ in range(10)]

        # Zliczam jest jest miejsc na odpowiednim miejscu
        # przy pomocy exp
        for i in range(n):
            # musze za kazdym razem obliczyc b
            b = arr[i] % n
            index = b // exp
            count[index % 10] += 1

        # Teraz tworze ta wlasnosc tablicy
        # count ze i-ty element zawiera info ile jest liczb
        # mniejszych badz rownych i
        for j in range(1, 10):
            count[j] += count[j - 1]

        # buduje tablice output przegladajac od tylu
        i = n - 1
        while i>= 0:
            b = arr[i] % n
            index = b // exp
            # od count[..] musze odjac 1 bo to indeksy w output
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -=1

        # Kopiuje tablice output do arr
        for a in range(n):
            arr[a] = output[a]

        exp *= 10


    # robie dokladnie to samo wszystko tylko ze dla  czesci a liczby
    biggest = n - 1
    exp = 1
    while biggest // exp > 0:
        # Countsortuje po b
        # Tworze tablice output
        output = [0 for _ in range(n)]
        # Oraz tworze tablice count do zliczania cyfr
        count = [0 for _ in range(10)]

        # Zliczam jest jest miejsc na odpowiednim miejscu
        # przy pomocy exp
        for i in range(n):
            # musze za kazdym razem obliczyc a
            a = arr[i] // n
            index = a // exp
            count[index % 10] += 1

        # Teraz tworze ta wlasnosc tablicy
        # count ze i-ty element zawiera info ile jest liczb
        # mniejszych badz rownych i
        for j in range(1, 10):
            count[j] += count[j - 1]

        # buduje tablice output przegladajac od tylu
        i = n - 1
        while i >= 0:
            a = arr[i] // n
            index = a // exp
            # od count[..] musze odjac 1 bo to indeksy w output
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        # kopiuje tablice output do arr
        for a in range(n):
            arr[a] = output[a]

        exp *= 10



if __name__ == '__main__':
    # tablica na 8 elementow wiec liczby [0,...,63]
    T = [59, 63, 1, 62, 58, 0, 8, 21]
    radixsort(T)
    print(T)
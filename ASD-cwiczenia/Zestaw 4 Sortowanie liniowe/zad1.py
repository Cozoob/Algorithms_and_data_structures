# Prosze zaproponowac algorytm, który w czasie liniowym sortuje tablice A zawierajaca n liczb
# ze zbioru 0, . . . ,n2 − 1.

# Kazda k-ta liczbe mozna podzielic na liczbe skladajaca sie ze skladnikow k = a*n^1 + b*n^0
# tzn b = k % n zas a = k // n po czym mozemy posotyowac radix sortem najpierw po skladniku
# b liczby a pozniej po skladniku a wszystko w czasie liniowym O(n).
import random

def mysort(A):
    n = len(A)

    # Tablica output bedzie posiadac posortowane liczby
    output = [0 for _ in range(n)]

    # Tablica count bedzie zliczac pod odpowiednimi indekami ilosc danych liczb od 0 do n - 1
    count = [0 for _ in range(n)]

    # Najpierw sortuje po b

    # Zliczam liczbe wystapien liczb 0,...,n - 1
    for i in range(n):
        index = A[i] % n
        count[index] += 1

    # Zmieniam count[i] tak zeby i-ty indeks zawieral informacje o ilosci liczby wystapien
    # i-tej liczby i ilosc wszystkich liczb mniejszych od i-tej
    for j in range(1, n):
        count[j] += count[j - 1]

    # Tworze posortowana output tablice
    i = n - 1
    while i >= 0:
        index = A[i] % n
        output[count[index] - 1] = A[i]
        count[index] -= 1
        i -= 1

    # Kopiuje posortowane output tablice do tablicy A
    for k in range(n):
        A[k] = output[k]

    # Pozostalo mi posortowac po skladniku a kazda liczbe w A
    # "czyszcze" tablice output i count
    output = [0 for _ in range(n)]
    count = [0 for _ in range(n)]

    # Zliczam liczbe wystapien liczb 0,...,n - 1
    for i in range(n):
        index = A[i] // n
        count[index] += 1

    # Zmieniam count[i] tak zeby i-ty indeks zawieral informacje o ilosci liczby wystapien
    # i-tej liczby i ilosc wszystkich liczb mniejszych od i-tej
    for j in range(1, n):
        count[j] += count[j - 1]

    # Tworze posortowana output tablice
    i = n - 1
    while i >= 0:
        index = A[i] // n
        output[count[index] - 1] = A[i]
        count[index] -= 1
        i -= 1

    # Kopiuje posortowane output tablice do tablicy A
    for k in range(n):
        A[k] = output[k]

if __name__ == '__main__':
    n = 10
    T = [random.randint(0,n*n - 1) for _ in range(n)]
    print(T)
    mysort(T)
    print(T)
# zlozonosc czasowa O(n) ale pamieciowa duza...
# dziala dla liczb naturalnych

def countingsort(array):
    # array tablica ktora chcemy posortowac
    # sortedarray tablica w ktorej zapiszemy posortowane elementy
    sortedarray = [0 for _ in range(len(array))]
    # tablica numbers zachowuje pod odpowiednim indeksem (indeks przedstawia liczbe)
    # to ile jest danych liczb tzn jesli sa dwie 4 to numbers[4] = 2
    # zatem aby utworzyc tablice numbers potrzebujemy wiedziec jaka jest najwieksza liczba w array
    maxnumber = 0
    for i in range(len(array)):
        if array[i] > maxnumber:
            maxnumber = array[i]
    numbers = [0 for _ in range(maxnumber + 1)]
    # zliczamy ile jest danych liczb i zapisujemy ich ilosc w tablicy numbers
    for j in range(1, len(array)):
        numbers[array[j]] += 1
    # teraz kazdy element numbers[i] zawiera teraz liczbe elementow mniejszych badz rownych i
    for k in range(1, maxnumber + 1):
        numbers[k] += numbers[k - 1]
    # wreszcze umieszam elementy do sortedarray w odpowiedni sposob
    for a in range(len(array) - 1, -1, -1):
        sortedarray[numbers[array[a]]] = array[a]
        numbers[array[a]] -= 1
    return sortedarray



if __name__ == '__main__':
    array = [2, 110, 3, 0, 2, 3, 0, 3]
    print(countingsort(array))
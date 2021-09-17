# Marcin Kozub

# Najpierw tworze pomocnicza tablice tmp ktora sortuje rosnaco quicksortem a nastepnie znajduje
# N razy mediany za kazdym razem nie biorac pod uwage wczesniej znalezionej mediany.
# Dzieki temu wiem w jakiej kolejnosci maja sie znajdowac mediany w przekatnej oraz
# liczby wieksze i mniejsze od liczb w przekatnych.

# Zlozonosc czasowa to: O(n^2)
# ZLozonosc pamieciowa to: O(n^2)

def Median(T):
    # najpierw tworze tablice pomocnicza ktora posortuje quicksortem
    n = len(T)
    tmp = [0 for _ in range(n*n)]
    # przepisuje kazda wartosc z podtablic T do tablicy tmp
    idx = 0
    for i in range(len(T)):
        for j in range(len(T)):
            tmp[idx] = T[i][j]
            idx += 1
    # sortuje tablice tmp
    quicksort(tmp, 0, len(tmp) - 1)
    # N razy szukam mediany w tablicy
    # za kazdym razem zamieniajac ja z ostatnim elementem w tablicy tmp
    # i zmniejszajac zakres sortowania tablicy tmp
    idx = len(tmp) - 1
    for k in range(len(T)):
        # mediana to element srodkowy w posortowanej tablicy
        tmp[idx // 2], tmp[idx] = tmp[idx], tmp[idx // 2]
        idx -= 1
        quicksort(tmp, 0, idx)
    # dzieki temu mamy mediany ktore musza sie znalezc na przekatnej
    # w takiej kolejnosci takiej jakiej sie znajduja
    idx += 1
    # teraz idx wskazuje na 1 mediane
    # przepisuje do tablicy T mediany
    # na lewo od median po kolei najpierw najmniejsze elementy
    # a na prawo od median najwieksze elementy
    # j wskazuje na najwiekszy element z zakresu [0, idx - 1]
    # k wskazuje na miejsce mediany
    j = idx - 1
    k = 0
    for a in range(len(T)):
        T[a][k] = tmp[idx]
        idx += 1
        k += 1
    # wstawiam najwieksze wartosci po prawej stronie
    # przekatnej
    for a in range(len(T) - 1):
        for b in range(len(T) - 1, a, -1):
            T[a][b] = tmp[j]
            j -= 1

    # podobnie wstawiam pozostale najwieksze wartosci po lewej
    # stronie przekatnej
    for a in range(1, len(T)):
        for b in range(a):
            T[a][b] = tmp[j]
            j -= 1



def quicksort(A, left, right):
    while left < right:
        mid = partition(A, left, right)
        if mid - left < right - mid:
            quicksort(A, left, mid - 1)
            left = mid + 1
        else:
            quicksort(A, mid + 1, right)
            right = mid - 1

def partition(A, left, right):
    elem = A[right]
    i = left
    for j in range(left, right):
        if A[j] <= elem:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[right] = A[right], A[i]
    return i
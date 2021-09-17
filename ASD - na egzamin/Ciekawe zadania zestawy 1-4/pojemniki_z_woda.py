# Created by Marcin "Cozoob" Kozub 24.06.2021
# Zadanie 4. (Pojemniki z wodą) Mamy serię pojemników z wodą, połączonych (każdy z każdym) rurami.
# Pojemniki maja kształty prostokątów, rury nie maja objetosci (powierzchni). Każdy pojemnik opisany jest
# przez współrzędne lewego górnego rogu i prawego dolnego rogu.
# Wiemy, ze do pojemników nalano A “powierzchni” wody (oczywiście woda rurami spłynęła do najniźszych
# pojemników). Proszę zaproponować algorytm Obliczający ile pojemników zostało w pełni zalanych.

# Nope nie dziala

# Pomysl: Najpierw tworze tablice tupli (x, y ,nr pojemnika, gorne czy dolne wspolrzedne, dlugosc pojemnika)
# Nastepnie sortuje po y tuple w tablicy tupli. Zaczynajac od pierwszego dolnego indeksu
# przechodze do kolejnego indeksu w tablicy. Odpowiednio na biezaco aktualizuje stan L (z zadania A).
# Jesli trafie na gorny indeks i L >= 0 to inkrementuje counter i zapisuje ktory pojemnik zostal zalany.


# Musze rozwazyc skrajny przypadek gdy trafie na gorny indeksy i bedzie tez inny gorny indeks
# na tej samej "wysokosci-y" i wtedy musze sprawdzic czy zaleje 2,3,... pojemniki czy zaden z nich.

# Musze tez uwazac zeby nie zalec "pustego obszaru" tzn gdy obliczam L musze tez sprawdzac
# czy roznica sumy gornych - dolnych > 0 jesli rowna 0 tzn ze nie odejmuje od L niczego
# bo pojemniki zostaly napelnione.

# przyjmuje tablice A krotek (x1,y1,x2,y2) gdzie x1,y1 to wspolrzedne lewego gornego rogu
# a x2, y2 to wspolrzedne prawego dolnego rogu
def water_tanks(A, L):
    res = []
    T = []
    # counter to suma ilosci dolnych indeksow - suma ilosci gornych indeksow w danym momencie
    counter = 0
    n = len(A)

    for i in range(n):
        T.append((A[i][0], A[i][1], i, "G", A[i][2] - A[i][0]))
        T.append((A[i][2], A[i][3], i, "D", A[i][2] - A[i][0]))

    QuickSort1(T, 0, len(T) - 1)
    # jeszcze kolejny edge case jesli zle sie posortuje
    # to indeks Dolny kolejnego pojemnika moze byc
    # przed Gornym poprzedniego pojemnika na tej samej wysokosci - y
    # A gorne zawsze musza byc przed!
    i = 0
    n = len(T)
    while i < n - 1:
        while i + 1 < n and T[i][1] == T[i + 1][1] and T[i][3] == "D":
            if T[i + 1][3] == "G":
                T[i], T[i + 1] = T[i + 1], T[i]
            i += 1
        i += 1

    #print(T)

    last = T[0]
    counter += 1
    i = 1
    while i < n and L > 0:

        if counter > 0:

            # skrajny przypadek
            if i + 1 < n and T[i][3] == "G" == T[i + 1][3]:
                c = 0
                new_res = []
                area = 0

                while i + 1 < n and T[i][3] == "G" == T[i + 1][3]:
                    h = T[i + 1][1] - T[i][1]
                    area += (h * T[i][4] + h * T[i + 1][4])
                    c += 1
                    new_res.append(i)
                    new_res.append(i + 1)

                    i += 1


                last = T[i + 1]

                if L - area >= 0:
                    L -= area
                    counter -= c
                    for elem in new_res:
                        res.append(elem)
                else:
                    break

            else:
                # tak to normalnie
                h = T[i][1] - last[1]
                area = h * last[4]
                if T[i][3] == "G":
                    area += (h * T[i][4])

                L -= area

                if L < 0:
                    break


        if T[i][3] == "D":
            counter += 1
        else:
            res.append(T[i][2])
            counter -= 1

        i += 1


    return L, res, counter

def partition1(arr, left, right):
    pivot = arr[right][1]
    i = left
    for j in range(left, right):
        if arr[j][1] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]

    return i


def QuickSort1(arr, left, right):
    while left < right:
        mid = partition1(arr, left, right)
        QuickSort1(arr, left, mid - 1)
        left = mid + 1

if __name__ == '__main__':
    A = [(1, 3, 2, 1), (3, 4, 4, 1), (4, 5, 6, 4), (2, 7, 4, 6)]
    print(water_tanks(A, 50))
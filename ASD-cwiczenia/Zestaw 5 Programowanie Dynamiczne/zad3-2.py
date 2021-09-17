# Created by Marcin "Cozoob" Kozub 15.05.2021
# Zadanie 3.2 (najdłuższy podciąg rosnący) Należy znaleźć
# długość najdłuższego podciągu rosnącego.
# Na wykładzie podaliśmy algorytm działający w czasie O(n^2). Proszę podać algorytm o złożoności
# O(nlog n).

# Uzywam patience sorta. Tzn ustawiam liczby jak najbardziej na lewo. Jesli nie moge polozyc "liczby"
# na zaden stos to tworze nowy stos z ta liczba. Ukladam tak n kart i uzywam binsearch (logn) w poszukiwaniu
# gdzie mam polozyc liczbe. Ilosc stosow zwraca mi dlugosc najdłuższego podciągu rosnącego
# f(i, k) - ???


def bin_search(A, left, right, target):
    if left > right:
        return -1
    # strzelam w srodek patrze czy A[mid] > target, wtedy ok
    # jesli nie to strzelam bardziej na lewo
    mid = (left + right) // 2
    if A[mid] <= target:
        return bin_search(A, mid + 1, right, target)
    elif A[mid] > target:
        # spogladam tylko czy moge go umiescic jeszcze bardziej na lewo
        if mid > 0 and A[mid - 1] > target:
            return bin_search(A, left, mid - 1, target)
        else:
            return mid


def LIS(A):
    n = len(A)
    # w tablicy res zapisuje stosy liczb
    res = [A[0]]
    for i in range(1, n):
        checker = bin_search(res, 0, len(res) - 1, A[i])
        if checker == -1:
            res.append(A[i])
        else:
            res[checker] = A[i]

    return res, len(res)

if __name__ == '__main__':
    T = [10, 5, 8, 3, 9, 4, 12, 11]
    print(LIS(T))
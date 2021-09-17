# Proszę zaproponować algorytm, który dla tablicy liczb całkowitych rozstrzyga czy każda liczba z tablicy jest sumą dwóch innych liczb z tablicy. Zaproponowany
# algorytm powinien być możliwie jak najszybszy. Proszę oszacować jego złożoność obliczeniową.

# O(n^2)
# Wystarczy posortowac quicksortem O(nlgn) a pozniej idac po calej tablicy ustawic dwa
# indeksy i, j jeden na poczatek tablicy drugi na koniec ktory bedzie sprawdzal czy
# zachodzi rownosc x = A[i] + A[j] gdzie x != A[i] i x != A[j]. Jesli A[i] + A[j] > x
# to dekrementujemy j, jesli A[i] + A[j] < x to inkrementujemy i. Dodatkowe uwagi :
# i < j; i != a; j != a.

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

def findthesum(T):
    quicksort(T, 0, len(T) - 1)
    for a in range(len(T)):
        i = 0
        j = len(T) - 1
        # flag pomoze mi wyjsc z petli oraz okreslic
        # czy kazdy element w tablicy spelnia warunki zadania
        flag = False
        while i < j:
            if a == i:
                i += 1
                continue
            if j == a:
                j -= 1
                continue
            if A[i] + A[j] == A[a]:
                flag = True
                break
            elif A[i] + A[j] > A[a]:
                j -= 1
            else:
                i += 1

        if flag == False:
            return False

    return True

if __name__ == '__main__':
    A = [0, 0, 0, 1, 1, 1, 2]
    print(findthesum(A))
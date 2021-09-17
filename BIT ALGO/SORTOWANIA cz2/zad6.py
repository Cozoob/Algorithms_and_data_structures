# Dana jest posortowana rosnąco tablica A wielkości n zawierająca
# parami rozne liczby naturalne. Podaj algorytm, ktory sprawdzi, czy
# jest taki indeks i, ze A[i] == i.
# Co zmieni sie, jezeli liczby beda calkowite, niekoniecznie naturalne?

# 1. Gdy liczby sa naturalne wystarczy sprawdzic czy A[0] == 0 bo gdy A[0] > 0 to A[i] > i
# dla kazdego i indeksu w A.
# 2. Gdy liczby calkowite trzeba szukac binary searchem.

def findwhennat(A):
    if A[0] == 0:
        return True
    return False

def bin_search(A, left, right):
    if left <= right:
        mid = (left + right) // 2
        if A[mid] == mid:
            return True
        elif A[mid] > mid:
            bin_search(A, left, mid - 1)
        else:
            bin_search(A, mid + 1, right)

    return False

def findwhenint(A):
    return bin_search(A, 0, len(A) - 1)

if __name__ == '__main__':
    T = [-7,-6,2,4,5,6]
    print(findwhenint(T))
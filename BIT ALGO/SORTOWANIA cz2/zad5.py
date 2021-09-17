# Dana jest nieskończona tablica A, gdzie pierwsze n pozycji zawiera posortowane liczby naturalne, a reszta tablicy ma
# wartości None. Nie jest dana wartosc n. Przedstaw algorytm, ktory dla danej liczby naturalnej x znajdzie indeks
# w tablicy, pod którym znajduje sie wartosc x. Jezeli nie ma jej w tablicy, to nalezy zwrocic None.

# Skacze sobie co 2^k po indeksach gdzie na poczatku k = 0 a pozniej k inkrementuje podczas kazdego skoku
# i dopoki jest rozny od None i element A[2^k] < x. Dzieki temu pozniej wyszukuje binarnie wartosc x
# wyszukiwaniem binarnym pomiedzy 2^(k-1) a 2^k. Wszystko to ma zlozonosc O(lgn)

def bin_search(A, left, right, target):
    if left <= right:
        mid = (left + right) // 2
        if A[mid] == target:
            return True
        elif A[mid] > target:
            bin_search(A, left, mid - 1, target)
        else:
            bin_search(A, mid + 1, right, target)

    return False

def findthex(A,x):
    k = 0
    while A[2**k] != None and A[2**k] < x:
        k += 1
    if A[2**k] == None:
        idx = 2**(k-1)
        while A[idx] != None and A[idx] < x:
            idx += 1
        if bin_search(A, 2**(k-1), idx, x):
            return True
        else:
            return None
    else:
        if bin_search(A, 2**(k-1), 2**k, x):
            return True
        else:
            return None
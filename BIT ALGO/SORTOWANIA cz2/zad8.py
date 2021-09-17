# Dane jest n punktow na osi liczbowej jednowymiarowej.
# Napisz algorytm, ktory stwierdzi, w ktorym z nim nalezy
# wybudowac dom, tak aby suma euklidesowych odleglosci
# od tego punktu do wszystkich pozostalych byla minimalna.
# Nalezy zwrocic te sume. Algorytm powinien byc jak najszybszy.

# Odp bedzie mediana
# Wiec mozna wyszukac mediane median dzieki magicznym piatkom
# O(n)

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

def magicfives(A, left, right):
    if len(A) == 1:
        return A

    # dziele sobie tablice na 5 grup i na ostatnia grupe ktora
    # jako ostatnia ma 0,1,2,3 lub 4 elementy
    # last to indeks pierwszego elementu ostatniej grupy
    last = (((right - left + 1) // 5) * 5 + left)

    a = 0
    medians =[]
    # szukam mediane w kazdej z grup
    for j in range(left, right):
        idx = left + j * 5
        if idx > right:
            break
        quicksort(A,idx, idx + 4)
        A[left + j * 3], A[a] = A[a], A[left + j * 3]
        a += 1

    # mediana ostatniej grupy
    if right - last < 2 and right - last > 0:
        # 1 element mediana
        A[last], A[a] = A[a], A[last]
        a += 1
    else:
        # 2 element mediana
        A[last + 1], A[a] = A[a], A[last + 1]
        a += 1

    # szukamy mediany median
    return magicfives(A,left, a - 1)

# zostalo policzyc te sume liniowo no i juz...

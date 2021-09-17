# Prosze zaproponować algorytm, ktory dla tablicy liczb calkowitych rozstrzyga czy kazda liczba z
# tablicy jest sumą dwóch innych liczb z tablicy. Zaproponowany algorytm powinien byc mozliwie jak
# najszybszy. Prosze oszacowac jego zlozonosc obliczeniowa.

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

# cos nie dziala : (
# 1 pomysl O(n^2logn) tzn dwie petle for i wyszukiwanie binarne
# to jest 1/2 pkt na kolosie
def findthesum1(A):
    quicksort(A, 0, len(A) - 1)
    for a in range(len(A)):
        flag = False
        for b in range(len(A)):
            if a == b:
                continue
            if bin_search(A, 0, len(A) - 1, A[a] + A[b]):
                flag = True
                break
        if flag == False:
            return False

    return True

# dziala xd
# 2 pomysl O(n^2) najpierw posortowac nlgn a pozniej
# dwoma indeksami z poczatku i konca isc np i na poczatku
# j na koncu i jesli A[i] + A[j] > x to j-- zas jesli
# A[i] + A[j] < x to i ++

def findthesum2(A):
    quicksort(A, 0, len(A) - 1)
    for x in range(len(A)):
        i = 0
        j = len(A) - 1
        flag = False
        while i < j:
            if i == x:
                i += 1
                continue
            elif j == x:
                j -= 1
                continue
            if A[i] + A[j] == A[x]:
                flag = True
                break
            elif A[i] + A[j] > A[x]:
                j -= 1
            else:
                i += 1
        if flag == False:
            return False

    return True

if __name__ == '__main__':
    A = [0,0,0,1, 1, 1, 2]
    print(findthesum2(A))
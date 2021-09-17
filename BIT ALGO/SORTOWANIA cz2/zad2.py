# Dana jest tablica 2n liczb rzeczywistych. Zaproponuj algorytm, który podzieli te
# liczby na n par w taki sposob, ze podzial bedzie mial najmniejsza maksymalna
# sume liczb w parze. Przykladowo, dla liczb (1,3,5, 9) mozemy miec podzialy
# ((1,3),(5,9)), ((1,5),(3,9)) oraz ((1,9),(3,5)). Sumy par dla tych podziałow
# to (4,14), (6,12) oraz (10,8), w związku z tym maksymalne sumy to 14, 12 oraz 10.
# Wynika z tego, że ostatni podział ma najmniejsza maksymalna sume.

# Najpierw musimy posortowac quicksortem tablice i dzieki temu bedziemy mogli
# zabrac pierwszy i ostatni element jako elementy najmniejszej maksymalnej sumy,
# ktora moze powstac. A reszte liczb mozna podzielic losowo w pary.

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

def function(A):
    quicksort(A, 0, len(A) - 1)
    return (A[0], A[len(A) - 1])

if __name__ == '__main__':
    T = [3,9,5,1]
    print(function(T))
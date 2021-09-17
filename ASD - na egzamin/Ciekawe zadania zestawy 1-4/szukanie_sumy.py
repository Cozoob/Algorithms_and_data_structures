# Created by Marcin "Cozoob" Kozub 24.06.2021
# Zadanie 7. (szukanie sumy) Dana jest posortowana tablica A[1...n] oraz liczba x.
# Proszę napisać program, który stwierdza czy istnieją indeksy i oraz j takie, że A[i] + A[j] = x.

def find_the_sum(A, x):
    n = len(A)
    i = 0
    j = n - 1
    while i < j:
        if A[i] + A[j] == x:
            return True, i, j
        elif A[i] + A[j] < x:
            i += 1
        else:
            j -= 1

    return False



if __name__ == '__main__':
    T = [9, 5, 2, 1, 4, 6,7 ,3, 1,3 ,5]
    T.sort()
    print(T)
    print(find_the_sum(T, 11))
    print(find_the_sum(T, 50))
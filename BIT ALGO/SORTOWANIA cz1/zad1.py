# Mamy dane n punktów (x, y) w okregu o promieniu k (liczba naturalna), tzn. 0 <= x^2 + y^2 <= k, ktore sa
# w nim rownomiernie rozlozone, tzn. prawdopodobienstwo znalezienia punktu na danym obszarze jest proporcjonalne
# do pola tego obszaru. Napisz algorytm, ktory w czasie O(n) posortuje punkty po ich odleglosci od punktu (0,0)
#, tzn. d = sqrt(x^2 + y^2).

# kubelki podzielone na promienie gdzie kazdy kolejny promien jest 2 razy wiekszy od poprzedniego
# sortowanie kubelkowe
import math

def quicksort(A, left, right):
    while left < right:
        mid = partition(A, left, right)
        if mid - left < right - mid:
            quicksort(A,left, mid - 1)
            left = mid + 1
        else:
            quicksort(A, mid + 1, right)
            right = mid - 1

def partition(A, left, right):
    elem = A[right][2]
    i = left
    for j in range(left, right):
        if A[j][2] <= elem:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[right] = A[right], A[i]
    return i

def bucket_sort(A, k):
    tmp = k
    rnge = 1
    while tmp > 0 and tmp >= 2:
        tmp //= 2
        rnge += 1

    buckets = [[] for _ in range(rnge)]
    for i in range(len(A)):
        idxbucket = 1
        tmp = A[i][2]
        while tmp > 0 and tmp >= 2:
            tmp //= 2
            idxbucket += 1
        buckets[idxbucket - 1].append(A[i])

    a_index = 0
    for bucket in buckets:
        quicksort(bucket, 0, len(bucket) - 1)
        for i in range(len(bucket)):
            A[a_index] = bucket[i]
            a_index += 1

def sortpoints(A, k):
    # musze policzyc odleglosc kazdego punktu od srodka okregu
    # iii zapisac w krotce wraz ze wspolrzednymi do tablicy pomocniczej
    # a pozniej juz z posortowanej tablicy spisac wspolrzedne tylko do koncowej A
    tab = [0 for _ in range(len(A))]
    for i in range(len(A)):
        x = A[i][0]
        y = A[i][1]
        d = math.sqrt(x**2 + y**2)
        tab[i] = (x, y, d)
    # sortuje po d
    bucket_sort(tab, k)
    for j in range(len(A)):
        x = tab[j][0]
        y = tab[j][1]
        A[j] = (x, y)

if __name__ == '__main__':
    k = 8
    A = [(2,2),(1,0),(0,1),(7,6),(4,5),(2,8), (8,8), (0,0), (1,6)]
    sortpoints(A, k)
    print(A)
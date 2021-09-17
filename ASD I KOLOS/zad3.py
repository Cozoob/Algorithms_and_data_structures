# Marcin Kozub


def SortTab(T, P):
    # ci mowi nam ile miejsc zajmuje w T
    # tworze kubelki w ktorych bede sortowac bucketsortem
    # liczby z podanych przedzialow
    # K tablica kubelkow
    n = len(P)
    K = [[] for _ in range(n)]
    for i in range(len(T)):
        for j in range(len(P)):
            if T[i] >= P[j][0] and T[i] <= P[j][1]:
                K[j].append(T[i])
    # kazda podtablice w K sortuje bucket sortem
    for i in range(len(K)):
        bucket_sort(K[i])
    # zostaje przepisac odpowiednio wartosci do tablicy T
    idx = 0
    i = 0
    for j in range(len(K)):
        T[idx] = K[0][j]
        idx += 1



    return T, K



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
    elem = A[right]
    i = left
    for j in range(left, right):
        if A[j] <= elem:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[right] = A[right], A[i]
    return i

def bucket_sort(A):
    n = len(A)
    min_val = min(A)
    max_val = max(A)
    rnge = (max_val-min_val)/n

    buckets = [ [] for _ in range(n) ]
    for i in range(len(A)):
        diff = (A[i] - min_val) / rnge - int((A[i] - min_val) / rnge)

        if diff == 0 and A[i] != min_val:
            buckets[int((A[i] - min_val) / rnge) - 1].append(A[i])
        else:
            buckets[int((A[i] - min_val) / rnge)].append(A[i])

    a_index = 0
    for bucket in buckets:
        quicksort(bucket, 0, len(bucket) - 1)
        for i in range(len(bucket)):
            A[a_index] = bucket[i]
            a_index += 1

if __name__ == '__main__':
    P = [(1, 5, 0.75), (4, 8, 0.25)]
    T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
    print(SortTab(T,P))
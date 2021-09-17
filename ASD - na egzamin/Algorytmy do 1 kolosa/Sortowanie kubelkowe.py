# Created by Marcin "Cozoob" Kozub 24.06.2021
# Sortujemy tablice n liczb pochodzacych z rozkladu
# jednostajnego nad [0, 1)!
# Musi byc ten warunek spelniony zeby sortowanie dzialalo poprawnie!
from math import floor
# TWORZYMY ZAWSZE N KUBELKOW! // tzn list jednokierunkowych w tablicy

# O(n), gdy spelnia warunki


def partition(T, p, r):
    pivot = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[j], T[i] = T[i], T[j]

    i += 1
    T[i], T[r] = T[r], T[i]
    return i

def quick_sort(T, p , r):
    while p<r:
        q = partition(T, p, r)
        quick_sort(T, p, q - 1)
        p = q + 1


def bucket_sort(A):
    n = len(A)
    min_val = min(A)
    max_val = max(A)
    value_range = (max_val-min_val)/n

    buckets = [ [] for _ in range(n) ]
    for i in range(len(A)):
        ratio = (A[i] - min_val) / value_range
        diff = ratio - int(ratio)

        if diff == 0 and A[i] != min_val:
            buckets[int(ratio)-1].append(A[i])
        else:
            buckets[int(ratio)].append(A[i])
    a_index = 0
    for bucket in buckets:
        quick_sort(bucket, 0, len(bucket)-1)
        for i in range(len(bucket)):
            A[a_index] = bucket[i]
            a_index += 1


if __name__ == '__main__':
    T = [9, 1, 4, 56, 23, 5, 1, 0, 23, 12, 7, -100, -23, 5]
    bucket_sort(T)
    print(T)

    T = [0.41, 0.42, 0.13, 0.07, 0.21, 0.91, 0.13, 0.37]
    bucket_sort(T)
    print(T)
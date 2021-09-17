# bucket sort działa dla liczb ktore maja rowny rozklad...
import random

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
    n = 10
    arr = [random.randint(0,20) for _ in range(n)]
    print(arr)
    bucket_sort(arr)
    print(arr)

# (Select) Prosze zaimplementowac algorytm znajdowania k-go co do wielkosci elementu w tablicy
# n elementowej w “spodziewanym” czasie O(n) na podstawie randomizowanego Partition z QuickSort’a

def partition(A, left, right):
    elem = A[right]
    i = left
    for j in range(left, right):
        if A[j] <= elem:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[right] = A[right], A[i]
    return i

def select(A, left, right, k):
    if left == right:
        return A[left]
    mid = partition(A, left, right)
    i = mid - left + 1
    if k == i:
        # wynikiem jest element rozdzielajacy
        return A[mid]
    elif k < i:
        return select(A, left, mid - 1, k)
    else:
        return select(A, mid + 1, right, k - i)

if __name__ == '__main__':
    T = [5,3,6,7,1,8]
    print(select(T, 0, len(T) - 1, 4))
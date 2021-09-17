# Created by Marcin "Cozoob" Kozub 26.06.2021
from random import randint
# f(i) - dlugosc najdluzszego podciagu rosnacego konczacego sie na A[i]
# f(i) = 1 + max{ f(j) : j < i and A[j] < A[i] }

# O(n^2) !
def LIS1(A):
    n = len(A)
    F = [1 for _ in range(n)]
    # tablica parentow P
    P = [-1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if A[j] < A[i] and F[i] < F[j] + 1:
                F[i] = F[j] + 1
                P[i] = j

    i = 0
    biggest = F[0]
    for k in range(n):
        if biggest < F[k]:
            biggest = F[k]
            i = k

    ans = get_LIS(A, P, i, [])
    return ans[::-1]

def get_LIS(A, P, i, ans):
    if P[i] >= 0:
        ans.append(A[i])
        get_LIS(A, P, P[i], ans)
    else:
        ans.append(A[i])

    return ans


# O(nlogn) wykorzystujac metode sortowania pasjansowego patience sort
# z wykorzystaniem binary saerch do wybrania odpowiedniego stosu
def LIS2(A):
    n = len(A)
    T = [[(A[0], -1, -1)]]
    P = [-1 for _ in range(n)]

    for i in range(1, n):
        idx = BinarySearch(T, 0, len(T) - 1, A[i])
        if idx == -1:
            c = 0

            for elem in T[len(T) - 1]:
                if elem[1] != -1:
                    idx = c
                    break
                c += 1

            T.append([(A[i], len(T) - 1, idx)])
        else:
            T[idx].append((A[i], -1, -1))

    ans = []

    for i in range(len(T) - 1, 0, -1):
        tab = T[i]
        the_best = -1
        for elem in tab:
            if len(ans) > 0 and elem[0] < ans[len(ans) - 1]:
                the_best = max(the_best, elem[0])
            elif elem[0] >= the_best and len(ans) == 0:
                the_best = elem[0]

        ans.append(the_best)

    for elem in T[0]:
        if elem[0] < ans[len(ans) - 1]:
            ans.append(elem[0])
            break

    return ans[::-1]



def BinarySearch(arr, left, right, elem):
    if left > right:
        return -1

    mid = left + (right - left) // 2
    if arr[mid][len(arr[mid]) - 1][0] >= elem and mid == 0:
        return mid
    elif arr[mid][len(arr[mid]) - 1][0] >= elem and mid > 0 and arr[mid - 1][len(arr[mid-1]) - 1][0] < elem:
        return mid
    elif arr[mid][len(arr[mid]) - 1][0] >= elem and mid > 0 and arr[mid - 1][len(arr[mid-1]) - 1][0] >= elem:
        return BinarySearch(arr, left, mid - 1, elem)
    else:
        return BinarySearch(arr, mid + 1, right, elem)


if __name__ == '__main__':
    A = [3,1,5,7,2,4,9,3,17,3]
    print(LIS1(A))
    print(LIS2(A))
    T = [10,5,8,3,9,4,12,11]
    print(LIS1(T))
    print(LIS2(T))

    H = [17, 29, 18, 18, 14, 23, 34, 21, 14, 21, 29, 21, 33, 9, 12, 6, 10, 14, 16, 6]
    print(LIS1(H))
    print(LIS2(H))


    # RANDOM TESTY XD

    for i in range(50):
        T = [randint(0,40) for _ in range(20)]
        ans1 = LIS1(T)
        ans2 = LIS2(T)
        if ans1 != ans2:
            print("BLAD : (")
            print("Tablica:", T)
            print("LIS1:", ans1)
            print("LIS2:", ans2)
            exit()

    print("JEST OK")
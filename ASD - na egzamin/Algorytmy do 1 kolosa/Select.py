# Created by Marcin "Cozoob" Kozub 24.06.2021

# O(n)
# Wyznacza element ktory po posortowaniu tablicy znalazlby sie na k-tym miejscu

# Przyklady elementarne
# k = 0 -> minimum
# k = n - 1 -> maksimum

def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]

    return i


def select(arr, left, right, k):
    if left == right:
        return arr[left]

    pivot = partition(arr, left, right)
    if pivot == k:
        return arr[pivot]
    elif k < pivot:
        return select(arr, left, pivot - 1, k)
    else:
        return select(arr, pivot + 1, right, k)

if __name__ == '__main__':
    T = [26, 20, 43, 39, 51, 13, 1, 76, 47, 31]
    print(len(T))
    print(select(T, 0, len(T) - 1, 7))
    T.sort()
    print(T)
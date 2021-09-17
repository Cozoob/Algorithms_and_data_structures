# Created by Marcin "Cozoob" Kozub 24.06.2021
# BinarySearch dziala na posortowanej tablicy!
# O(logn)


def BinarySearch(arr, left, right, elem):
    if left > right:
        return -1

    mid = left + (right - left) // 2
    if arr[mid] == elem:
        return mid
    elif arr[mid] > elem:
        return BinarySearch(arr, left, mid - 1, elem)
    else:
        return BinarySearch(arr, mid + 1, right, elem)

if __name__ == '__main__':
    T = [0, 1, 8, 21, 58, 59, 62, 63]
    print(BinarySearch(T, 0, len(T) - 1, 8))
# Created by Marcin "Cozoob" Kozub 24.06.2021

# O(d(n + k))
# stabilne


def countingsort(arr, exp1):
    n = len(arr)
    output = [0 for _ in range(n)]
    count = [0 for _ in range(10)]

    for i in range(0, n):
        index = (arr[i] // exp1)
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]


    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp1)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    for i in range(0, n):
        arr[i] = output[i]

def radixsort(arr):
    n = len(arr)
    biggest = 0
    for i in range(n):
        if biggest < arr[i]:
            biggest = arr[i]

    exp = 1
    while biggest // exp > 0:
        countingsort(arr, exp)
        exp *= 10


if __name__ == '__main__':
    T = [59, 63, 1, 62, 58, 0, 8, 21, 100]
    radixsort(T)
    print(T)
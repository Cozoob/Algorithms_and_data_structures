# Dana jest posortowana tablica A[1...n] oraz liczba x. Prosze napisac program,
# który stwierdza czy istnieja indeksy i oraz j takie, ze A[i] + A[j] = x.

def bin_search(arr, target):

    def rek_bin_search(arr, left, right, target):
        if left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                return rek_bin_search(arr, left, mid - 1, target)
            else:
                return rek_bin_search(arr, mid + 1, right, target)

    return rek_bin_search(arr, 0, len(arr) - 1, target)

def function(arr, x):
    for i in range(len(arr)):
        if bin_search(arr, x - arr[i]) != None:
            return True
    return False

if __name__ == '__main__':
    A = [1, 3, 5, 6, 7, 8, 9, 11, 15]
    print(function(A,21))
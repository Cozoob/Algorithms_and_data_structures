# Proszę zaproponować/zaimplementować algorytm scalający k posortowanych tablic o łącznej
# długości n w jedną posortowaną tablicę w czasie O(n ∗ log(k)).

def merge_lists(arg1, arg2, *args):

    def rek_merge(arr1, arr2, arrs, idx):
        if idx < 0:
            return arr1
        tmp = [0 for _ in range(len(arr1) + len(arr2))]
        n1 = len(arr1)
        n2 = len(arr2)
        i, j = 0, 0
        for k in range(len(tmp)):
            if i == n1:
                # array1 has ended then I copy the left elements in arr2 to tmp
                tmp[k] = arr2[j]
                j += 1
            elif j == n2:
                # array2 has ended then I copy the left elements in arr1 to tmp
                tmp[k] = arr1[i]
                i += 1
            elif arr1[i] <= arr2[j]:
                tmp[k] = arr1[i]
                i += 1
            elif arr1[i] > arr2[j]:
                tmp[k] = arr2[j]
                j += 1
        # at the end I've got the sorted array named as tmp
        # and I sort tmp with another sorted array in args
        # I do this until the args end
        return rek_merge(tmp, arrs[idx], arrs, idx - 1)

    # I am counting how many arrays there are
    counter = 0
    for _ in args:
        counter += 1
    # I am saving those arrays into the one
    arrs = [0 for _ in range(counter)]
    i = 0
    for arg in args:
        arrs[i] = arg
        i += 1
    print(arrs)


    return rek_merge(arg1, arg2, arrs, counter - 1)


if __name__ == '__main__':
    t1 = [7,9]
    t2 = [-1,4,6]
    t3 = [1,10]
    t4 = [8,99]
    t5 = [86,3]
    print(merge_lists(t1,t2,t3,t4,t5))
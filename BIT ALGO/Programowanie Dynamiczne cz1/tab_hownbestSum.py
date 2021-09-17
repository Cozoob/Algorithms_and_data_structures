# Created by Marcin "Cozoob" Kozub at 21.04.2021 00:50

# f(x, A) - sprawdzam czy moge zsumowac liczby w tablicy tak aby otrzymac
# sume x, uzywajac jak najmniej elementow z tablicy A

# n = len(A)
# f(x, A) = min(f(x-A[0],A) or f(x-A[1],A) or ... or f(x-A[n-1],A))
# f(0, A) = []

def bestSum(target, numbers):
    tab = [None for _ in range(target + 1)]
    tab[0] = []

    for curr_target in range(1, target + 1):
        for j in range(len(numbers)):
            if curr_target - numbers[j] >= 0 and tab[curr_target - numbers[j]] != None:
                tmp = tab[curr_target - numbers[j]].copy()
                tmp.append(numbers[j])
                if tab[curr_target] == None:
                    tab[curr_target] = tmp
                else:
                    if len(tab[curr_target]) > len(tmp):
                        tab[curr_target] = tmp
    return tab[target]
if __name__ == '__main__':
    print(bestSum(5, [2,3,5])) # 5
    print(bestSum(7, [5, 3, 4, 7])) # 7
    print(bestSum(8, [2, 3, 5])) # 3, 5
    print(bestSum(8, [1, 4, 5])) # 4, 4
    print(bestSum(100, [1, 2, 5, 25])) # 25, 25, 25, 25
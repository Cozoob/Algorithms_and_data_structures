# Created by Marcin "Cozoob" Kozub at 21.04.2021 00:25

# f(x, A) - sprawdzam, czy moge zsumowac liczby z tablicy A tak aby otrzymac sume x
# f(x, A) = f(x - A[0]) or f(x - A[1]) or... or f(x - A[n]) gdzie n to ostatni
# indeks w tablicy A
# f(0,A) = True

# n = len(numbers)
# zlozonosc pamieciowa: O(target)    (nie target + n bo n to dane wejsciowe)
# zlozonosc czasowa: O(target*n)

def canSum(target, numbers):
    A = [False for _ in range(target + 1)]
    A[0] = True
    for i in range(1, target + 1):
        for j in range(len(numbers)):
            if i - numbers[j] >= 0 and A[i - numbers[j]] == True:
                A[i] = True
    return A[target]




if __name__ == '__main__':
    print(canSum(1,[2,3])) # F
    print(canSum(7, [2, 3]))  # T
    print(canSum(7, [5, 3, 4, 7]))  # T
    print(canSum(7, [2, 4]))  # F
    print(canSum(8, [2, 3, 5]))  # T
    print(canSum(300, [7, 14]))  # F
# Created by Marcin "Cozoob" Kozub at 18.04.2021 20:55

def canSum(target_sum, numbers):
    memo = [None for _ in range(target_sum + 1)]

    def rec_canSum(target_sum, numbers, memo):
        if target_sum < 0:
            return False
        if memo[target_sum] != None:
            return memo[target_sum]
        if target_sum == 0:
            return True

        for i in range(len(numbers)):
            if rec_canSum(target_sum - numbers[i], numbers, memo) == True:
                memo[target_sum] = True
                return True

        memo[target_sum] = False
        return False

    return rec_canSum(target_sum, numbers, memo)

def howSum(target_sum, numbers):

    memo = [0 for _ in range(target_sum + 1)]

    def rec_howSum(target_sum, numbers, memo):
        if target_sum < 0:
            memo[target_sum] = None
            return None
        if target_sum == 0:
            memo[target_sum] = []
            return []
        if memo[target_sum] != 0:
            return memo[target_sum]

        for i in range(len(numbers)):
            remainderResult = rec_howSum(target_sum - numbers[i], numbers, memo)
            if remainderResult != None:
                tab = remainderResult.copy()
                tab.append(numbers[i])
                memo[target_sum] = tab
                return tab
        memo[target_sum] = None
        return None

    return rec_howSum(target_sum, numbers, memo)




if __name__ == '__main__':
    print(canSum(7, [2,3])) # T
    print(canSum(7, [5, 3, 4, 7])) # T
    print(canSum(7, [2, 4])) # F
    print(canSum(8, [2, 3, 5])) # T
    print(canSum(300, [7, 14])) # F

    print(howSum(7, [2, 3]))  # 3,2,2
    print(howSum(7, [5, 3, 4, 7]))  # 4,3
    print(howSum(7, [2, 4]))  # None
    print(howSum(8, [2, 3, 5]))  # 2,2,2,2
    print(howSum(300, [7, 14])) # None
# Created by Marcin "Cozoob" Kozub at 18.04.2021 21:34

def bestSum(target_sum, numbers):

    memo = [0 for _ in range(target_sum + 1)]
    memo[0] = []

    def rec_bestSum(target_sum, numbers, memo):
        if target_sum < 0:
            return None
        # if target_sum == 0:
        #     return []
        if memo[target_sum] != 0:
            return memo[target_sum]

        shortest_combination = None

        for i in range(len(numbers)):

            remainder_combination = rec_bestSum(target_sum - numbers[i], numbers, memo)

            if remainder_combination != None:
                tab = remainder_combination.copy()
                tab.append(numbers[i])

                if shortest_combination == None:
                    shortest_combination = tab

                if len(tab) < len(shortest_combination):
                    shortest_combination = tab

        memo[target_sum] = shortest_combination
        return shortest_combination


    return rec_bestSum(target_sum, numbers, memo)



if __name__ == '__main__':
    print(bestSum(7, [5, 3, 4, 7])) # 7
    print(bestSum(8, [2, 3, 5])) # 3, 5
    print(bestSum(8, [1, 4, 5])) # 4, 4
    print(bestSum(100, [1, 2, 5, 25])) # 25, 25, 25, 25
# Created by Marcin "Cozoob" Kozub at 18.04.2021 19:56
# Say that you are a traveler on a 2D grid. You begin in the top-left
# corner and your goal is to travel to the bottom-right corner.
# You may only move down or right.
# In how many ways can you travel to the goal on a grid
# with dimensions m*n?

# 1 rozw. rekurencyjne
# g(m,n) - ilosc sposonow aby przejscz top-left do bottom-right w tablicy m*n
# g(0, n) = g(n, 0) = 0
# g(1,1) = 1
# g(m, n) = g(m - 1, n) + g(m, n - 1)

def gridTraveler1(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return gridTraveler1(m-1, n) + gridTraveler1(m, n-1)

def gridTraveler2(m, n):
    DP = [[-1 for _ in range(n)]for _ in range(m)]
    DP[0][0] = 1
    def rec_gT(m, n, DP):
        if m == -1 or n == -1:
            return 0
        if DP[m][n] != -1:
            return DP[m][n]

        DP[m][n] = rec_gT(m - 1, n, DP) + rec_gT(m, n - 1, DP)
        return DP[m][n]

    rec_gT(m - 1, n - 1, DP)
    return DP[m - 1][n - 1]


if __name__ == '__main__':
    print(gridTraveler2(1,1)) # 1
    print(gridTraveler2(2, 3))  # 3
    print(gridTraveler2(3, 2))  # 3
    print(gridTraveler2(3,3))  # 6
    print(gridTraveler2(18,18))  # 2333606220

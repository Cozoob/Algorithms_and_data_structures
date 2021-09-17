# Created by Marcin "Cozoob" Kozub at 21.04.2021 00:00
# f(m,n) - ilosc sposobow na przejsce na planszy m*n
# f(m,n) = f(m - 1, n) + f(m, n - 1)
# f(m,0) = f(0,n) = 0
# f(1,m) = f(1,n) = 1

# zlozonosc czasowa: O(m*n)
# zlozonosc pamieciowa: O(m*n)

def grid_traveller(m, n):
    tab = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        tab[i][1] = 1

    for i in range(1, n + 1):
        tab[1][i] = 1

    for i in range(2, m + 1):
        for j in range(2, n + 1):
            tab[i][j] = tab[i - 1][j] + tab[i][j - 1]

    return tab[m][n]

if __name__ == '__main__':
    print(grid_traveller(3,2))
    print(grid_traveller(3, 3))
    print(grid_traveller(18, 18))  # 2333606220


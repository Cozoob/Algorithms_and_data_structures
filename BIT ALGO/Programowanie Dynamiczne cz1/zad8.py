# Created by Marcin "Cozoob" Kozub at 24.04.2021 22:24

# Dostając na wejściu string złożony z liter a-z, zwrócić najdłuższy jego fragment, który jest palindromem.
# Palindrom to ciąg znaków, który wygląda tak samo czytany zarówno od lewej, jak i od prawej strony.

# f(i, j) - najdluzszy palindrom znajdujacy sie pomiedzy pozycjami i oraz j

# f(i,j) = f(i + 1, j - 1), gdy A[i] == A[j]
# f(i,j) = False, gdy i > j
# f(i,j) = True, gdy i == j
# f(i, i + 1) = True, gdy A[i] = A[i + 1]

def is_palindrom(word):
    # tworze pomocnicza tablice do zapamietywania wynikow
    n = len(word)
    P = [[False for _ in range(n)] for _ in range(n)]

    # zapisuje wartosci startowe
    j = 0
    for i in range(n):
        if i + 1 < n and word[i] == word[i + 1]:
            P[i][i + 1] = True
        P[i][j] = True
        j += 1
    print(P)

    # w miedzy czasie zapisuje indeksy gdzie znajduje sie najdluzszy
    # jak narazie znaleziony palindrom
    biggest = (0, 0)
    # wartosc poczatkowa to jedna litera po prostu

    for i in range(1, n):
        y = i
        x = 0
        while y < n:
            if word[x] == word[y] and P[x][y] == False:
                P[x][y] = P[x + 1][y - 1]

            if P[x][y] == True and y - x > biggest[1] - biggest[0]:
                # dluzszy palidnrom znaleziony
                biggest = (x, y)

            y += 1
            x += 1

    # teraz zostalo tylko wypisac najdluzszy palindrom
    a = biggest[0]
    b = biggest[1]
    while a <= b:
        print(word[a], end='')
        a += 1
    print()


    return biggest, P

if __name__ == '__main__':
    word1 = "adsadaaabbaaadsds"
    print(is_palindrom(word1))
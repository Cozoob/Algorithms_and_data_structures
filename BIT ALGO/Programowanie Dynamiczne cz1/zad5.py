# Created by Marcin "Cozoob" Kozub at 23.04.2021 21:46
#
# Dostajemy tablicę (M x N) wypełnioną wartościami. Mamy za zadanie znaleźć najdłuższą ścieżkę w tej tablicy
# (możemy przechodzić na pola sąsiadujące krawędziami), o rosnących wartościach (to znaczy, że z pola o wartości 3,
# mogę przejść na pola o wartości większej bądź równej 4).

# Na początku wprowadzimy ponownie pewne ułatwienie:
# Mamy dany punkt początkowy

# f(i,j) - najdłuższa ścieżka w tablicy jaką można przejść z punktu 0,0 do i,j

#          { max( f(i-1,j) , f(i,j-1) ) + 1, gdy A[i][j] > A[i-1][j] i A[i][j] > A[i][j-1]
# f(i,j) = { f(i-1,j) + 1, gdy A[i][j] <= A[i-1][j] i A[i][j] > A[i][j-1]
#          { f(i, j-1) + 1, gdy A[i][j] > A[i-1][j] i A[i][j] <= A[i][j-1]
#          { 1, gdy A[i][j] <= A[i-1][j] i A[i][j] <= A[i][j-1]

def find_the_longest_path(A):
    # !zakładam ze zawsze zaczynam od 0,0!
    m = len(A)
    n = len(A[0])

    # tworze pomocnicza tablice P w ktorej bede trzymac wyniki
    P = [[0 for _ in range(n)] for _ in range(m)]

    # uzupelniam poczatkowe wartosci
    P[0][0] = 1
    for i in range(1, m):
        if A[i][0] > A[i - 1][0]:
            P[i][0] = P[i - 1][0] + 1
        else:
            P[i][0] = 1
    for i in range(1, n):
        if A[0][i] > A[0][i - 1]:
            P[0][i] = P[0][i - 1] + 1
        else:
            P[0][i] = 1

    # uzupelniam reszte
    for i in range(1, m):
        for j in range(1, n):
            if A[i][j] > A[i][j - 1] and A[i][j] > A[i - 1][j]:
                P[i][j] = max(P[i][j-1], P[i-1][j]) + 1
            elif A[i][j] > A[i][j - 1]:
                P[i][j] = P[i][j - 1] + 1
            elif A[i][j] > A[i-1][j]:
                P[i][j] = P[i-1][j] + 1
            else:
                P[i][j] = 1

    # teraz tylko szukam w tablicy najwiekszej wartosci
    # ktora zwroci nam dlugosc najdluzszej sciezki w tablicy A
    result = P[0][0]
    for i in range(m):
        for j in range(n):
            result = max(result, P[i][j])

    return result



if __name__ == '__main__':
    A = [[3, 4, 5, 2, 1], [1, 2, 13, 7, 8], [3, 1, 4, 6, 5], [2, 8, 11, 10, 3], [3, 5, 1, 6, 2]]
    print(find_the_longest_path(A))

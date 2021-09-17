# Created by Marcin "Cozoob" Kozub 27.06.2021
# Zadanie 7. (wędrówka po szachownicy) Dana jest szachownica A o wymiarach n × n. Szachownica
# zawiera liczby wymierne. Należy przejść z pola (1, 1) na pole (n, n) korzystając jedynie z ruchów “w dół”
# oraz “w prawo”. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm
# znajdujący trasę o minimalnym koszcie.

# czyli trzeba dojsc z (0,0) do (n - 1, n - 1) na tablicy 2D

# f(i, j) - minimalny koszt dojscia na pole i,j idac tylko w dol lub w prawo od pola 0,0
# f(i, j) = min( f(i, j - 1) , f(i - 1, j) ) + A[i][j]; i,j > 0
# f(0,0) = A[0][0]
# f(0, j) = A[0][j] + f(0,j - 1) , j > 0
# f(i, 0) = A[i][0] + f(i - 1,0) , i > 0

def the_chess(A):
    n = len(A)

    for i in range(1, n):
        A[0][i] += A[0][i - 1]
        A[i][0] += A[i - 1][0]

    for i in range(1, n):
        for j in range(1, n):
            A[i][j] = min(A[i - 1][j], A[i][j - 1]) + A[i][j]

    return A[n - 1][n - 1]

if __name__ == '__main__':
    A = [
        [1, 5, 3, 7],
        [2, 6, 4, 8],
        [10, 5, 1, 2],
        [3, 2, 1, 1]
    ]
    print(the_chess(A))
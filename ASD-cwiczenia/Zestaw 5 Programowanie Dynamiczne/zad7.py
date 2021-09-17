# Created by Marcin "Cozoob" Kozub 15.05.2021
# Zadanie 7. (wędrówka po szachownicy) Dana jest szachownica A o wymiarach n × n. Szachownica
# zawiera liczby wymierne. Należy przejść z pola (1, 1) na pole (n, n) korzystając jedynie z ruchów “w dół”
# oraz “w prawo”. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm
# znajdujący trasę o minimalnym koszcie.
# f(i,j) - minimalny koszt przejscia z pozycji (0,0) na (i, j)
# f(i,j) = min( f(i, j - 1) + A[i][j], f(i - 1, j) + A[i][j] : i > 0 and j > 0)
# f(0,0) = A[0][0]
# f(0,j) = (od k=1 do j) suma f(0, k)
# f(i, 0) = (od k = 1 do i) suma f(k, 0)

def find_min_cost(A):
    n = len(A)
    # wstawiam poczatkowe wartosc w tablicy A
    curr_sum1 = A[0][0]
    curr_sum2 = A[0][0]
    for i in range(1, n):
        curr_sum1 += A[i][0]
        A[i][0] = curr_sum1
        curr_sum2 += A[0][i]
        A[0][i] = curr_sum2

    for i in range(1, n):
        for j in range(1, n):
            A[i][j] = min(A[i - 1][j] + A[i][j], A[i][j - 1] + A[i][j])

    return A[n - 1][n - 1], A

if __name__ == '__main__':
    A = [
        [1, 5, 3, 7],
        [2, 6, 4, 8],
        [10, 5, 1, 2],
        [3, 2, 1, 1]
    ]
    print(find_min_cost(A))
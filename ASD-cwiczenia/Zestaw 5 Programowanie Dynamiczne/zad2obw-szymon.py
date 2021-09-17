# Created by Marcin "Cozoob" Kozub at 11.04.2021 23:25
# f(i,v) = czy uzywajac pierwszych i liczb mozemy uzyskac sume v
# f(i,v)={ f(i - 1, v) or A[i] == v or f(i - 1, v - A[i]) }
# Jesli A[i] == v tzn ze istnieje podciag dlugosci 1 gdzie A[i] = v
# jesli f(i-1, v) tzn ze nie bierzemy A[i] do podciagu ktory da nam sume v
# jesli f(i - 1, v - A[i]) tzn ze bierzemy A[i] do podciagu ktory da nam sume v
# u nas v = T
# O(n*T)



def print_2d(T):
    for elem in T:
        print(elem)
    print()

def zo2(A, T):
    # sprawdzam czy istnieje podciag dlugosci 1 o sumie rownej 0
    # tzn czy w A jest element rowny 0
    if T == 0:
        for i in range(len(A)):
            if A[i] == 0:
                return 1, []
        return 0, []

    n = len(A)
    # ustawiam na F[0][0..n] 1 jako info ze da
    # sie stworzyc podciag sumujacy sie do 0
    F = [[1] + [0] * T for _ in range(n)]

    # sprawdzam czy pierwszy wyraz w tablicy A
    # jest mniejszy badz rowny T
    if A[0] <= T:
        F[0][A[0]] = 1

    # indeksy w wierszach (i) odpowiadaja indeksom w tablicy A
    # indeksy w kolumnach (j) odpowiadaja czy danej sumie v
    # gdzie 0<= v <= T istnieje podciag sumujacy sie do tego v
    # stad nasza odpowiedz znajdzie sie w F[n-1][T]
    for i in range(1, n):
        for j in range(1, T + 1):
            # zapisze 1 jesli juz wczesniej sprawdzilem ze da sie stworzyc taki podciag
            F[i][j] = F[i - 1][j]
            # jesli 0 to sprwadzam czy o sumie j - A[i] moge stworzyc taki podciag
            # sumujacy sie do j
            if A[i] <= j and F[i][j] == 0:
                F[i][j] = F[i - 1][j - A[i]]

    # moge tez zwrocic tablice F zeby zobaczyc jak sie uzupelnia
    return F[n-1][T], F

if __name__ == '__main__':
    A = [4, 234, 5, 6346, 45, 745, 7, 45, 7, 0, 2]
    B = [3, 2, 6]
    T = 0
    res1, res2 = zo2(B, T)
    print(res1)
    print_2d(res2)
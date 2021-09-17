# Created by Marcin "Cozoob" Kozub at 12.04.2021 17:46

def NWP(A, B):
    n = len(A)
    m = len(B)
    C = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
                # znalezlismy kolejny element NWP
            else:
                C[i][j] = max(C[i-1][j-1], C[i][j-1])

    return C[n - 1][m - 1], C


if __name__ == '__main__':
    A = [1,3,4,7,3]
    B = [2,4,3,4,7,9,10]
    res, tab = NWP(A,B)
    print(res)
    for i in range(len(tab)):
        print(tab[i])
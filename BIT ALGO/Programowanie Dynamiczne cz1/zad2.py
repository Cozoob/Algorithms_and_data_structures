# Created by Marcin "Cozoob" Kozub at 18.04.2021 18:09
# Zmodyfikuj rozwiązanie problemu cięcia stalowych prętów tak,
# aby konstruowało i zwracało także rozwiązanie, tj. listę długości prętów o największej cenie.
# Podpowiedź: bottom-up będzie łatwiej


def cut_rod(C, P, n, S):
    if n <= 0:
        return 0
    for i in range(1, n + 2):
        curr_price = -1
        for j in range(i):
            if curr_price < P[i - j - 1] + C[j]:
                curr_price = P[i - j - 1] + C[j]
                S[i - 1] = j
        P[i - 1] = curr_price

    # dodatkowo wypisanie dlugosci ktore bralem do ciecia preta
    i = n
    while i > 0:
        print(S[i], end = ',')
        i -= S[i]
    print()

    return P[n], S

if __name__ == '__main__':
    C = [0, 3, 5, 8, 9, 10, 17, 17, 20]
    A = [0, 1, 5, 8, 9, 10, 17, 17, 20]
    n = 5
    P = [0 for _ in range(n + 1)]
    S = [0 for _ in range(n+1)]
    print(cut_rod(A, P, n, S))
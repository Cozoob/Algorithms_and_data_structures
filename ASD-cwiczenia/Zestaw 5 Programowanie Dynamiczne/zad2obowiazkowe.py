# Created by Marcin "Cozoob" Kozub at 11.04.2021 22:10

# f(i,v) = czy uzywajac pierwszych i liczb mozemy uzyskac sume v
# f(i,v)={ f(i - 1, v) or A[i] == v or f(i - 1, v - A[i])

def print_2d(T):
    tab = [ T[i] for i in range(len(T)) ]
    for subtab in tab:
        for j in range(len(subtab)):
            if subtab[j] is True: subtab[j] = 1
            else: subtab[j] = 0

    for i in range(len(tab)): print(tab[i])

def check(A, T):
    n = len(A)
    # Indeksy wierszy tablicy F to indeksy liczb z tablicy A
    #
    F = [ [False]*(T+1) for _ in range( n )]
    # sprawdzam czy w tablicy A jest 0 jesli tak to wpisuje w odp miejsce True
    for i in range( n ):   F[i][0] = (A[i] == 0)
    # sprawdzam czy w tablicy A jest podciag dlugosci 1 tzn czy szuk
    for v in range( T+1 ):
        # F[0][v] = (A[0] == v)
        if A[0] == v:
            if T == v:
                # tzn ze znalazlem podciag dlugosci 1
                return True
            else:
                F[0][v] = True

    for i in range( 1, n ):
        for v in range( 1, T+1 ):

            F[i][v] = ( F[i-1][v] or A[i] == v )

            if v-A[i] >= 0:
                F[i][v] = ( F[i][v] or F[i-1][v-A[i]] )

    # print_2d(F)
    return F[n-1][T]





A = [ 4, 234 ,5 ,6346 ,45 ,745 ,7 ,45 ,7, 0, 2]
B = [2, 4, 6]
T = 17
print(check(A, T), T)
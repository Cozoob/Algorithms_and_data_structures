# Created by Marcin "Cozoob" Kozub at 03.05.2021 23:03
# ZAD Z EGZAMINU 2020

# Asystent znanego profesora otrzymał polecenie wyliczenia sumy pewnego ciągu liczb (liczby mogą być zarówno dodatnie jak i ujemne).
# Aby zminimalizować błędy zaokrągleń asystent postanowił wykonać powyższe dodawania w takiej kolejności, by największy co do wartości
# bezwzględnej wynik tymczasowy (wynik każdej operacji dodawania; wartość końcowej sumy również traktujemy jak wynik tymczasowy) był możliwie jak najmniejszy.
#
# Aby ułatwić sobie zadanie, asystent nie zmienia kolejności liczb w sumie a jedynie wybiera kolejność dodawań. Napisz funkcję opt sum,
# która przyjmuje tablicę liczb n1, n2, . . . , nk (w kolejności w jakiej występują w sumie; zakładamy, że tablica zawiera co najmniej dwie liczby)
# i zwraca największą wartość bezwzględną wyniku tymczasowego w optymalnej kolejności dodawań.

# Na przykład dla tablicy wejściowej: [1,−5, 2] funkcja powinna zwrócić wartość 3, co odpowiada dodaniu −5 i 2 a następnie dodaniu 1 do wyniku.
# Uzasadnij poprawność zaproponowanego rozwiązania i oszacuj jego złożoność obliczeniową.


# f(i, j) - dodanie liczby i oraz j takich, ze ich wartosc bezwzgledna sumy jest najmniejsza.
# f(i, j) = min( abs(i + j): i != j)
# wynik: max(f(i,j))

def opt_sum(A):
    n = len(A)
    # tworze tablice kwadratowa F w ktorej bede zapisywac wyniki
    F = [[None for _ in range(n)] for _ in range(n)]
    # uzupelniam tablice F tzn dla liczby i szukam
    # takiej j a zeby miała ona najmniejsza suma bezwzgledna
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if F[0][i] == None:
                F[0][i] = abs(A[i] + A[j])
            F[0][i] = max(A[i] + A[j], F[0][i])

    for a in range(1, n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if F[a][i] == None:
                    F[a][i] = abs(F[a][i] + A[j])
                F[a][i] = max(A[i] + A[j], F[a][i])


    return F



if __name__ == '__main__':
    A = [1, -5, 2]
    print(opt_sum(A))
# Created by Marcin "Cozoob" Kozub 27.06.2021
# Zadanie 4. (Głodna żaba) Pewna żaba skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc
# wyłącznie w kierunku większych liczb. Skok z liczby i do liczby j (j > i) kosztuje ją j − i jednostek energii, a
# jej energia nigdy nie może spaść poniżej zera. Na początku żaba ma 0 jednostek energii, ale na szczęście na
# niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej (wartość przekąki
# dodaje się do aktualnej energii Zbigniewa). Proszę zaproponować algorytm, który oblicza minimalną liczbę
# skoków potrzebną na dotarcie z 0 do n − 1 majać daną tablicę A z wartościami energetycznymi przekąsek na
# każdej z liczb.


# f(i, T) - minimalna liczba skokow jaka zaba Zbigniew musi wykonac by dotrzec z pola 0 do i-ego pola majac
# T energii na i-tej pozycji
# A[i] - ilosc jednostek energii na i-tym polu
# na poczatku T = A[0]
# f(i,0) = inf
# f(0, T) = 0
# bo j oznacza o ile sie cofam wiec obliczam energie T_i-j !
# f(i, T) = min( f(i - j, T + j - A[i]) + 1 : n > i > j >= 1, T + j  - A[i] >= 0)

def _rek(i, t, A, F):
    inf = float("inf")
    if t <= 0 or t > len(F):
        return inf
    if F[i][t] != inf:
        return F[i][t]

    best = inf
    if t - A[i] >= 0:
        for j in range(1, i + 1):
            c = i - j
            # print(c)
            # if j > t + j - A[i]:
            #     break
            best = min(best, _rek(i - j, t + j - A[i], A, F) + 1)

    F[i][t] = best
    return F[i][t]

def frog(A):
    n = len(A)
    inf = float("inf")
    T_max = sum(A)

    F = [[inf for _ in range(T_max + 1)] for _ in range(n)]
    F[0][A[0]] = 0


    best_energy = 0
    for t in range(T_max + 1):
        if _rek(n - 1, best_energy, A, F) > _rek(n - 1, t, A, F):
            best_energy = t

    get_solution(n - 1, best_energy, A, F)
    print()
    return F[n - 1][best_energy]

def get_solution(i, t, A, F):
    if i > 0:
        for k in range(1, i + 1):
            if t + k - A[i] <= 0:
                continue
            if F[i][t] == F[i - k][t + k - A[i]] + 1:
                get_solution(i - k, t + k - A[i], A, F)
                break
    print(i, end=' ')


if __name__ == '__main__':
    A = [2, 1, 1, 1, 4, 2, 3, 1, 1, 1, 1, 1, 1]
    print(frog(A))
    A = [5, 2, 1, 8, 9, 1, 3, 2, 0]
    print(frog(A))
    # for elem in F:
    #     print(elem)

    # print(frog(A))
    # A = [5, 2, 1, 8, 9, 1, 3, 2, 0]
    # print(frog(A))
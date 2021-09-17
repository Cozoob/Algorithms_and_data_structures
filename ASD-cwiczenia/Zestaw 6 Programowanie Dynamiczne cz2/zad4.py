# Created by Marcin "Cozoob" Kozub 16.05.2021
# Zadanie 4. (Głodna żaba) Pewna żaba skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc
# wyłącznie w kierunku większych liczb. Skok z liczby i do liczby j (j > i) kosztuje ją j − i jednostek energii, a
# jej energia nigdy nie może spaść poniżej zera. Na początku żaba ma 0 jednostek energii, ale na szczęście na
# niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej (wartość przekąki
# dodaje się do aktualnej energii Zbigniewa). Proszę zaproponować algorytm, który oblicza minimalną liczbę
# skoków potrzebną na dotarcie z 0 do n − 1 majać daną tablicę A z wartościami energetycznymi przekąsek na
# każdej z liczb.

# Pomysl i wzor w jamboardzie ASD - ZESTAW 7

def _rek(i, energy, A, F, inf):
    # len(F) == n; i tak wiecej niz n energii potrzebowac nie bedziemy
    if energy <= 0 or energy > len(F):
        return inf
    # ta wartosc zostala juz obliczona wczesniej
    if F[i][energy] != inf:
        return F[i][energy]

    best = inf
    # sprawdzam jeszcze czy wystarczy energii na skok, tzn. czy e + k - A[i] >= k wtw, gdy e - A[i] >= 0
    if energy - A[i] >= 0:
        for k in range(1, i + 1):
            best = min(best, _rek(i - k, energy + k - A[i], A, F, inf) + 1)

    F[i][energy] = best
    return F[i][energy]

def frog(A):
    n = len(A)
    max_energy = sum(A)
    # moglo by wystarczy nawet n + 1 ale mniejsza z tym
    inf = n + max_energy

    # w F trzymam minimalna ilosc skokow zeby dotrzec na koniec tablicy A
    F = [[inf for _ in range(max_energy + 1)] for _ in range(n)]
    F[0][A[0]] = 0

    best_index = 0
    for energy in range(max_energy + 1):
        if _rek(n - 1, best_index, A, F, inf) > _rek(n - 1, energy, A, F, inf):
            best_index = energy

    return F[n - 1][best_index]

A = [ 2, 1, 1, 1, 4, 2, 3, 1, 1, 1, 1, 1, 1 ]
print(frog(A))
A = [5, 2, 1, 8, 9, 1, 3, 2, 0]
print(frog(A))
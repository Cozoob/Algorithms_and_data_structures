# Created by Marcin "Cozoob" Kozub 16.05.2021
# Zadanie 2. (spadające klocki) Każdy klocek to przedział postaci [a, b]. Dany jest ciąg klocków [a1, b1],
# [a2, b2], . . ., [an, bn]. Klocki spadają na oś liczbową w kolejności podanej w ciągu. Proszę zaproponować
# algorytm, który oblicza ile klocków należy usunąć z listy tak, zeby każdy kolejny spadajacy klocek mieścił
# się w całości na tym, który spadł tuż przed nim.
# Chcemy jak najwieksza ilosc tych klockow?(chyba tak)

# f(i) - ilosc klockow, ktore tworza wieze tak (po usunieciu klockow ktore nie miescly sie w wiezy),
# ze kazdy kolejny spadajacy klocek miesci sie w calosci na tym, ktory spadl tuz przed nim.
# f(i) = ?

def A_contains_B(i, j, x, y):
    if i >= x and j <= y:
        return True
    return False

def blocks(A):
    n = len(A)
    F = [1 for _ in range(n)]

    # sprawdzam dla kazdego i-tego klocka
    for i in range(n):
        # ile najwiecej j klockow moze na niego spasc
        best = 1
        for j in range(n):
            if i != j and A_contains_B(A[i][0], A[i][1], A[j][0], A[j][1]):
                # to jest tyle ile juz spadlo na j + ten i-ty klocek
                q = F[j] + 1
                # sprawdzam czy jest to najwiecej ile moze jesli tak to zapisuje najlepszy wynik
                if best < q:
                    best = q
        F[i] = best

    result = max(F)
    return n - result, F

if __name__ == '__main__':
    S = [[-1, 3], [0, 5], [1, 11], [2, 4], [2, 9], [5, 8], [6, 7], [-10, -5], [-10,-9]]
    print(blocks(S))
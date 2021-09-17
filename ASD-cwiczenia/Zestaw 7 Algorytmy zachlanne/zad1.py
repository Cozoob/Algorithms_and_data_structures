# Created by Marcin "Cozoob" Kozub 15.05.2021
# Zadanie 1. (pokrycie przedziałami jednostkowymi) Dany jest zbiór punktów X = {x1, . . . , xn} na
# prostej. Proszę podać algorytm, który znajduje minimalną liczbę przedziałów jednostkowych domkniętych,
# potrzebnych do pokrycia wszystkich punktów z X. (Przykład: Jeśli X = {0.25, 0.5, 1.6} to potrzeba dwóch
# przedziałów, np. [0.2, 1.2] oraz [1.4, 2.4]).

# Pomysł: Kazdy poczatek przedzialu jednostkowego jest takim xi, ktory nie zostal jeszcze pokryty zadnym
# innym przedzialem jednostkowym. Tzn. dla X1 = {0.25, 0.5, 1.6} przedziały to [0.25, 1.25], [1.6, 2.6],
# zaś dla X2 = {0.25, 0.3, 0.4, 1.25, 1.256, 2.257} przedzialy to [0.25, 1.25], [1.256, 2.256], [2.257, 3.257]

# zakladam ze X jest posortowany rosnaco
def count(X):
    # ustalam pierwszy przedział: a - poczatek przedzialu, b - koniec przedzialu, taki ze b = a + 1
    # w sumie i bez tego a by sie obeszlo
    counter = 1
    res = []
    a = X[0]
    b = a + 1
    res.append([a,b])
    for elem in X:
        if elem > b:
            counter += 1
            b = elem + 1
            res.append([elem, b])

    return counter, res

if __name__ == '__main__':
    X1 = [0.25, 0.5, 1.6]
    X2 = [0.25, 0.3, 0.4, 1.25, 1.256, 2.257]
    print(count(X1))
    print(count(X2))
# Created by Marcin "Cozoob" Kozub at 23.04.2021 22:16

# Dostajemy liczbę naturalną n. Naszym zadaniem jest policzenie wszystkich binarnych (0/1) stringów o długości n bez jedynek obok siebie

# f(i) - liczba wszystkich binarnych stringow o dlugosci i bez jedynek obok siebie
# f(i) = f(i - 1) + f(i - 2)
# f(0) = 0
# f(1) = 2

def seq(n):
    if n <= 0:
        return 0
    if n == 1:
        return 2

    a1 = 0
    a2 = 2
    for i in range(1, n):
        new = a1 + a2
        a1 = a2
        a2 = new

    return new

if __name__ == '__main__':
    print(seq(2))
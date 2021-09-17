# Created by Marcin "Cozoob" Kozub at 25.04.2021 13:31

# W problemie tankowania paliwa nasz pojazd musi przemieścić się z punktu 0 do punktu F, a po drodze ma stacje do tankowania paliwa si,
# przy czym 0 < s1 < s2 < ... < sn < F. Każda stacja jest identyfikowana przez jej odległość od punktu 0, tzn. si to odległość pomiędzy
# i-tą stacją a punktem 0. Pojazd potrafi przejechać odległość d bez potrzeby tankowania.
# Podaj algorytm, który obliczy, na ilu minimalnie stacjach musi zatrzymać się pojazd na drodze od punktu 0 do punktu F.
# Uwaga: jeżeli zdarzy się, że odległość d jest zbyt mała, żeby dojechać do kolejnej stacji, to należy zwrócić wartość None.

# Pomysł na algorytm: jadę jak najdalej (tak zeby nie zabraklo mi paliwa) i tankuję do pełna.

# zlozonosc czasowa: O(n)
# zlozonosc pamieciowa: O(1)

def fuel(S, d):
    # S odleglosci od pkt 0 do stacji si
    # d pojemnosc zbiornika paliwa
    n = len(S)
    # zapisuje max pojemnosc baku paliwa
    # (chyba niepotrzebnie)
    d_max = d

    # j mowi o tym gdzie stoi obecnie czołg
    j = 0
    counter = 0
    for i in range(1, n - 1):
        # wybieram stacje do ktorej dojade najdalej
        if S[i] - j <= d and S[i + 1] - j > d:
            # tankuje czołg na tej stacji si
            j = S[i]
            d = d_max
            # i doliczam stacje
            counter += 1
    # sprawdzam jeszcze czy moge dojechac do punktu F
    if S[n - 1] - j <= d:
        j = S[n - 1]
    else:
        # jesli nie to zwracam None
        return None

    return counter, j


if __name__ == '__main__':
    A = [0, 2, 3, 5, 7, 9, 13, 17, 21]
    d = 6
    print(fuel(A, d))
# Created by Marcin "Cozoob" Kozub at 25.04.2021 18:45

# ???

# Dany jest zbiór przedziałów otwartych. Zaproponuj algorytm, który znajdzie podzbiór tego zbioru, taki że:
# 1) jego rozmiar wynosi dokładnie k
# 2) przedziały są rozłączne
# 3) różnica między najwcześniejszym początkiem, a najdalszym końcem jest minimalna.
# Jeśli rozwiązanie nie istnieje, to algorytm powinien to stwierdzić.
# Algorytm powinien być w miarę możliwości szybki, ale przede wszystkim poprawny.

# p - poczatek przedzialu k - koniec przedzialu
# pomysł: dla posortowago zbioru niemalejąco po pocztkach przedziałow sprawdzam
# dla kazdego i-ego przedzialu, czy istnieje taki j-ty przedział, ze zaczyna sie on
# najwczesniej, ale k_i <= p_j oraz czy nie istnieje taki j+1 przedzial, że
# k_j+1 - k_i < k_j - k_i. I kontynuuje takie szukanie dalej. Zapisuje w tablicy T
# o rozmiarze n pod odpowiednim indeskem krotki zawierajace rozmiary podzbiorow i numery przedziałow.

# zlozonosc czasowa:
# zlozonosc pamieciowa:

def find_subset(A, k):
    n = len(A)
    # sortuje talice A po poczatkach
    A.sort(key=lambda x: x[0])

    # tworze tablice w ktorej bede zapisywac odpowiedzi
    T = [0 for _ in range(n)]

    for i in range(n):



if __name__ == '__main__':
    Z = [(6,11), (1,5), (13,17), (4,8), (11,19), (9,11), (7,8)]
    k = 4
    print(find_subset(Z, k)) # odp dla k = 4 to (1,5), (7,8), (9,11), (13,17)
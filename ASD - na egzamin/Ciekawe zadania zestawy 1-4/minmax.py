# Created by Marcin "Cozoob" Kozub 24.06.2021
# Zadanie 4. (min/max) Proszę zaimplementować funkcję, która mając na wejściu tablicę n elementów
# oblicza jednocześnie jej największy i najmniejszy element wykonując 1.5n porównań.



def minmax(T):
    n = len(T)
    min_val = T[0]
    max_val = T[0]
    counter = 0
    for i in range(1, n):
        if min_val > T[i]:
            min_val = T[i]
            counter += 1
        elif max_val < T[i]:
            max_val = T[i]
            counter += 1

    return min_val, max_val, counter / n



if __name__ == '__main__':
    T = [8, 3, 2, 5, 7, 1, 3, 68]
    print(minmax(T))
# Created by Marcin "Cozoob" Kozub 24.06.2021
# Zadanie 5. (Lider ciągu) Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm o złożoności
# O(n), który stwierdza, czy istnieje liczba x (tzw. lider A), która występuje w A na ponad połowie pozycji.



def leader(A):
    n = len(A)

    # szukam potencjalnego lidera
    counter = 0
    k = 0
    for i in range(n):
        if counter == 0:
            counter = 1
            k = i
        elif A[i] == A[k]:
            counter += 1
        else:
            counter -= 1

    # sprawdzam czy na pewno jest liderem
    counter = 0
    for i in range(n):
        if A[i] == A[k]:
            counter += 1

    if counter > n // 2:
        return A[k]

    return None


if __name__ == '__main__':
    A = [2, 1, 2, 2, 4, 2, 8, 2]
    print(leader(A))
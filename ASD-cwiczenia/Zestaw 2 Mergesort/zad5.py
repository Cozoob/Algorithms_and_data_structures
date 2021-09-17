# (Lider ciagu) Mamy dana tablice A z n liczbami. Prosze zaproponowac algorytm o złozonosci
# O(n), który stwierdza, czy istnieje liczba x (tzw. lider A), która wystepuje w A na ponad połowie pozycji.

def findleader(A):

    # szukam potencjalnego lidera
    licz = 0
    idx = 0
    for i in range(len(A)):
        if licz == 0:
            licz = 1
            idx = i
        elif A[i] == A[idx]:
            licz += 1
        else:
            licz -=1

    # sprawdzam czy napewno tym liderem jest
    counter = 0
    for i in range(len(A)):
        if A[i] == A[idx]:
            counter += 1
        if counter > len(A) // 2:
            return A[idx]

    return "Brak lidera"


if __name__ == '__main__':
    T1 = [1,3,4,3,2,1,1]
    T2 = [1,2,2,3,3,3,3,2,3]
    T3 = [2,3,1,1,1,4]
    T4 = [2,2,2,2,3,3,3,3,3,3]
    print(findleader(T1))
    print(findleader(T2))
    print(findleader(T3))
    print(findleader(T4))
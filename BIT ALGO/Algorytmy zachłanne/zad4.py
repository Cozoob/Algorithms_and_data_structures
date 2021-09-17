# Created by Marcin "Cozoob" Kozub at 25.04.2021 17:24

# W jednej z chińskich prowincji postanowiono wybudować serię maszyn chroniących ludność przed koronawirusem.
# Prowincję można zobrazować jako tablicę wartości 1 i 0, gdzie arr[i] = 1 oznacza, że w mieście i można zbudować maszynę,
# a wartość 0, że nie można. Dana jest również liczba k, która oznacza, że jeśli postawimy maszynę w mieście i,
# to miasta o indeksach j takich, że abs(i-j) < k są przez nią chronione. Należy zaproponować algorytm, który stwierdzi
# ile minimalnie maszyn potrzeba aby zapewnić ochronę w każdym mieście, lub -1 jeśli jest to niemożliwe.

# Pomysł: ustawiam maszynę na 1 najlepszym miejscu tzn. tak aby maszyna chroniła jak najwiekszy obszar niechroniony

# zlozonosc czasowa: O(n)
# zlozonosc pamieciowa: O(1)

def build_machines(A, k):
    # robie 1-szy skok o k - 1 i jesli A[k-1] != 1 to ide do tylu szukajac 1,
    # jesli nie znadje to zwracam -1; jesli znajde na j to stawiam tam maszyne
    # i robie skok o i = j + 2k-1 sprawdzam czy A[i] == 1, jesli nie to szukam
    # czy nie stoi 1 wczesniej taka ktora ma indeks != j oraz stawiam maszyne i
    # robie dalej skok o 2k - 1. Bo jesli indeks == j to zwracam -1
    counter = 0
    n = len(A)
    # szukam miejsca dla pierwszej maszyny
    if A[k-1] == 1:
        counter += 1
        idx = k - 1
    else:
        idx = k - 2
        while idx > -1 and A[idx] == 0:
            idx -= 1

        if idx == -1:
            return -1
        else:
            counter += 1

    # stawiam reszte maszyn
    prev = idx
    idx += (2*k - 1)
    if idx >= n:
        idx = n - 1

    while idx < n:
        # sprawdzam czy moge postawic maszyne
        if idx != prev and A[idx] == 1:
            counter += 1
        else:
            while idx != prev and A[idx] == 0:
                idx -= 1
            if idx == prev:
                return -1
            else:
                counter += 1
        # robie skok o 2k - 1
        prev = idx
        idx += (2*k - 1)
        if idx >= n and prev + k - 1 >= n - 1:
            # wszystko chroni wiecej maszyn nie mozna postawic
            break
        elif idx >= n:
            idx = n - 1

    return counter

if __name__ == '__main__':
    A = [1,0,1,0,1,1,1,0,0,1,0]
    k = 3
    print(build_machines(A,k))
# Created by Marcin "Cozoob" Kozub at 25.04.2021 20:37

# Trzy problemy (czołg zawsze startuje z pełnym bakiem):
# a) obliczyć minimalną liczbę tankowań, żeby dotrzeć do punktu t
# b) obliczyć minimalny koszt dotarcia do punktu t:
#    b1) na każdej stacji można tankować, tyle ile się chce
#    b2) jeśli tankujemy to do pełna

# L - pojemność baku czołgu (w litrach)
# s_i - odleglosc stacji i od punktu 0 (w km)
# p_i - cena paliwa za litr na stacji i
# czołg spala 1l/1km

# f(i) - min koszt aby dojechac na pole i, pod warunkiem ze zawsze tankujemy do pelna
# f(i) = min{ f(i-v)+(S[i]-S[i-v])*P[i] | S[i]-S[i-v] <= L and i-v >= 0 }
# min{ f(k) | S[n-1]-S[k] <= L } 0<=k<n-1 - rozw
# rozw zapisze sobie w F[n-1] dla wygody, bo i tak nie uzywalem tego pola


# rozwiazanie dynamiczne
def tank_b2(P, S, L):
    n = len(P)
    inf = sum(S) * sum(P)
    F = [inf] * n

    F[0] = L * P[0]
    for i in range(1, n - 1):
        # jesli nie jestesmy w stanie dojechac do najblizszej stacji z pelbym bakiem zwracam false
        if S[i] - S[i - 1] > L:
            return False
        F[i] = F[i - 1] + (S[i] - S[i - 1]) * P[i]
        v = 2
        while i - v >= 0 and S[i] - S[i - v] <= L:
            q = F[i - v] + (S[i] - S[i - v]) * P[i]
            if q < F[i]:
                F[i] = F[i - v] + (S[i] - S[i - v]) * P[i]
            v += 1

    v = 2
    i = n - 1
    if S[i] - S[i - 1] > L:
        return False
    F[i] = F[i - 1]
    while i - v >= 0 and S[i] - S[i - v] <= L:
        if F[i - v] < F[i]:
            F[i] = F[i - v]
        v += 1

    return F[n - 1]

if __name__ == '__main__':
    S = [0, 2, 3, 7, 11, 12, 14]
    P = [0, 1, 10, 7, 5, 2, 11]
    L = 7
    print(tank_b2(P,S,L))
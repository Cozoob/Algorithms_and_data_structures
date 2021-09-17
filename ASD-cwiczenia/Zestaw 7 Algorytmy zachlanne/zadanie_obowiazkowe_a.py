# Created by Marcin "Cozoob" Kozub at 25.04.2021 19:07

# Trzy problemy (czołg zawsze startuje z pełnym bakiem):
# a) obliczyć minimalną liczbę tankowań, żeby dotrzeć do punktu t
# b) obliczyć minimalny koszt dotarcia do punktu t:
#    b1) na każdej stacji można tankować, tyle ile się chce
#    b2) jeśli tankujemy to do pełna

# L - pojemność baku czołgu (w litrach)
# s_i - odleglosc stacji i od punktu 0 (w km)
# p_i - cena paliwa za litr na stacji i
# czołg spala 1l/1km

# Problem a): Pomysł: czołg jedzie do jak najdalszej stacji może (na tyle ile mu paliwa wystarczy)
# i tankuje do pełna i jedzie tak dalej. Jesli nie da sie dojechac do punktu t zwracam -1.

# zakładam ze t >= 0
def problem_a(S, L, t):
    # jesli dojade bez tankowania
    if t <= L:
        return 0
    # jeśli punkt t jest za daleko nawet gdybym zatankowal
    # na ostatniej stacji
    elif t > S[len(S) - 1] + L:
        return -1

    n = len(S)
    # j mowi o tym gdzie obecnie stoi czołg
    j = 0
    counter = 0
    while j < n - 1:
        k = 1
        # sprawdzam czy w ogole moge dojechac do nastepnej najblizszej stacji
        if S[k + j] - S[j] > L:
            return -1

        # sprawdzam do ktorej najdalszej stacji moge dojechac
        while j + k + 1 <= n - 1 and S[j + k + 1] - S[j] <= L:
            k += 1
        # sprawdzam czy musze tankowac czy przypadkiem nie dojechalem
        # juz do punktu t
        if S[j] + L >= t:
            return counter
        # jesli jeszcze nie dojechalem to tankuje do pełna na stacji S[j + k]
        counter += 1
        j += k

    return counter


if __name__ == '__main__':
    L = 5
    t = 22
    S1 = [0, 2, 3, 7, 11, 12, 17] # dla t=17 odp to 3; dla t=12 odp to 2; dla t = 18 (lub 22) odp to 4; dla t = 23 odp -1
    print(problem_a(S1,L,t))
    t = 18
    S2 = [0, 2, 3, 7, 11, 12, 18]  # dla t = 18 odp to -1 (bo nie da sie)
    print(problem_a(S2,L,t))
    S = [0, 5, 7, 9, 12, 13, 20]
    L = 8
    t = 20
    print(problem_a(S,L,t)) # odp to 2
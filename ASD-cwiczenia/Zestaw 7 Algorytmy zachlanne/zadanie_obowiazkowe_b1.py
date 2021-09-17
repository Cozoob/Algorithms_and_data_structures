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

def tank_b1(P, S, L):

    # funkcja pomocznica szukajaca najtaniszej stacji w okolicy
    def min_index_in_range(P, i, j):
        result = i
        for x in range(i + 1, j + 1):
            if P[result] > P[x]:
                result = x
        return result

    current_fuel = L
    total_cost = 0
    n = len(P)
    i = 0
    while i < n - 1:
        # jesli nie jestesmy w stanie dojechac do najblizszej stacji
        # tankujac do pelna zwracam False
        if i + 1 < n and S[i + 1] - S[i] > L:
            return False
        # our_range - to maksymalnie o ile stacji jestesmy w stanie pojechac do przodu
        our_range = 1
        while i + our_range + 1 <= n - 1 and S[i + our_range + 1] - S[i] <= L:
            our_range += 1

        # szukam najtanszej stacji w okolicy
        min_prize = min_index_in_range(P, i, i + our_range)

        # jesli koniec w zasiegu i nie trzeba juz robic przystankow i tankowac aby dotrzec do celu
        # to jedziemy na sam koniec
        if i + our_range >= n - 1 and min_prize == i:
            total_cost += max(0, ((S[n - 1] - S[i]) - current_fuel) * P[i])
            current_fuel = max(current_fuel, S[n - 1] - S[i])
            destination = n - 1

        # jesli u nas najtaniej to tankuje do pelna i jade do nastepnej najtanszej
        elif min_prize == i:
            total_cost += (L - current_fuel) * P[i]
            current_fuel = L
            destination = min_index_in_range(P, i + 1, i + our_range)

        # w przeciwynym razie tankuje tyle zeby dojechac do najtanszej stacji
        else:
            total_cost += max(0, (((S[min_prize] - S[i]) - current_fuel) * P[i]))
            current_fuel = max(current_fuel, S[min_prize] - S[i])
            destination = min_prize

        current_fuel -= S[destination] - S[i]
        i = destination

    return total_cost

if __name__ == '__main__':
    S = [0, 2, 3, 7, 11, 12, 14]
    P = [99999, 1, 10, 7, 5, 2, 11]
    L = 7
    print(tank_b1(P,S,L))
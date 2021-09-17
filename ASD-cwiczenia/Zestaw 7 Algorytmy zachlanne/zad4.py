# Created by Marcin "Cozoob" Kozub 15.05.2021

# Zadanie 4. (wieże) Grupa m dzieci bawi się w układanie możliwie jak największej wieży. Każde dziecko
# ma klocki różnej wysokości. Pierwsze dziecko ma klocki o wysokościach w(1,1) , . . . , w(1, n1)
# , drugie dziecko klocki o wyskościach w(2, 1) , . . . , w(2,n2), itd.
# Dzieci właśnie poszły zjeść deser zanim ułożą swoje wieże, ale jedno dziecko
# zostało. Ma teraz jedyną okazję, żeby podebrać kilka klocków innym dzieciom tak, żeby jego wieża była
# najwyższa. Proszę podać możliwie najszybszy algorytm rozwiązujący ten problem, który zabiera minimalną
# ilość klocków. (Proszę zwrócić uwagę, że liczby w(i, j) mogą być bardzo duże.)

# Pomysł: Sumuje wysokosci wszystkich klockow dla kazdego dziecka trzymajac to jako dodatkowa informacje. Niech Hi oznacza wysokosc najwiekszej wiezy dziecka i.
# Dopoki moje dziecko k ma najwieksza wieze mniejsza niz dziecko j (ktore ma najwieksza wieze ze wszystkich dzieci) to zabieram
# dziecku j najwiekszy klocek (LUB zabieram mozliwy najwiekszy klocek ze wszystkich dostepnych klockow jesli wyjde na tym lepiej).
# Aktualizuje wysokosci Hk oraz Hj. Sprawdzam dalej czy jest takie dziecko t ze Hk < Ht. Jesli tak to z t robie podobnie jak z j itd...
# Jesli nie ma juz takiego dziecka to zabralem najmniejsza ilosc klockow jaka moglem zeby moje dziecko miala najwyzsza wieze.
# Zlozonosc czasowa: O(n^2logn)

# my_child - moje dziecko ktore zabiera klocki
# W - tablica tablic w ktorej sa wysokosci klockow kazdego dziecka
def steal(my_child, W):
    # mamy m dzieci, gdzie kazde ma n klockow
    m = len(W)
    n = len(W[0])
    # w tablic H zapisuje wysokosci najwyzszych wiez jakie dzieci moga stworzyc
    H = [0] * m
    for i in range(m):
        curr_h = 0
        for j in range(n):
            curr_h += W[i][j]
        H[i] = curr_h
        # sortuje rosnaco klocki kazdego dziecka
        W[i].sort()


    # teraz zajmujemy sie kradzieza klockow
    counter = 0
    while True:
        new_sum1 = H[my_child]
        new_sum2 = H[my_child]
        # sprawdzam jaka wysokosc bedzie miala wieza mojego dziecka gdy wezmie ono najwiekszy klocek
        # ze wszystkich dostepnych
        biggest1 = -1
        stolen_child1 = -1
        for i in range(m):
            if i == my_child:
                continue
            if biggest1 < W[i][n - 1]:
                biggest1 = W[i][n - 1]
                stolen_child1 = i
        new_sum1 += biggest1
        # sprawdzam teraz jaka wyskosc bedzie miala moja wieza gdy wezme najwiekszy klocek dziecku z najwyzsza wieza
        stolen_child2 = -1
        biggest2 = -1
        for i in range(m):
            if i == my_child:
                continue
            if biggest2 < H[i]:
                biggest2 = H[i]
                stolen_child2 = i

        biggest2 = W[stolen_child2][n - 1]
        new_sum2 += biggest2
        # teraz sprawdzam czy w ogole oplaca mi sie krasc wiecej klockow
        if H[my_child] > H[stolen_child2]:
            break
        else:
            # sprawdzam ktoremu dziecku bardziej mi sie oplaca podkradac klocka
            counter += 1
            if new_sum1 >= new_sum2 and new_sum2 <= H[stolen_child2] - biggest2:
                # to kradne pierwszemu dziecku klocuszka
                H[my_child] = new_sum1
                W[my_child][n - 1] += biggest1
                W[stolen_child1][n - 1] = -1
                W[stolen_child1].sort()
                H[stolen_child1] -= biggest1
            else:
                # to kradne drugiemu dziecku klocuszka
                H[my_child] = new_sum2
                W[my_child][n - 1] += biggest2
                W[stolen_child2][n - 1] = -1
                W[stolen_child2].sort()
                H[stolen_child2] -= biggest2
    return H, W, counter






if __name__ == '__main__':
    W = [
        [2, 3, 5, 7],
        [8, 8, 8, 8],
        [10, 1, 2, 3],
        [1, 1, 2, 5]
    ]
    print(steal(3, W))
    W2 = [
        [7, 0],
        [5, 6],
        [2, 0]
    ]
    print(steal(2, W2))
    W3 = [
        [5, 4, 3],
        [11, 0, 0],
        [2, 0, 0]
    ]
    print(steal(2, W3))
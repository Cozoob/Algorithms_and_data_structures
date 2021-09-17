# (najwiekszy przedział). Dany jest ciag przedziałów domknietych [a1, b1], . . . , [an, bn]. Prosze
# zapropnowac algorytm, który znajduje taki przedział [at, bt], w którym w całosci zawiera sie jak najwiecej
# innych przedziałów.

# BRUTAL FORCE 1/2 PKT NA KOLOSIE
def findrange(A):
    # sprawdzamy kazdy przedzial po kolei ile zawiera
    # w sobie innych przedzialow i zapisujemy index
    # jesli zawiera w calosci przedzialow wiecej niz poprzedni
    # tu wersja w calosci wiec jak mamy przedzial [1,6]
    # to w calosci zawieraja sie: [1,5], [3,4]
    # ale juz [0,6] nie
    biggest = 0
    idx = 0
    for i in range(1, len(A)):
        counter = 0
        for j in range(len(A)):
            if i != j and A[i][0] <= A[j][0] and A[i][1] >= A[j][1]:
                counter += 1
        if counter > biggest:
            biggest = counter
            idx = i

    return A[idx]

# 2/2 pkt na kolosie (chyba); zlozonosc nlgn
def find(A):
    # mamy przdzial <a,b>
    # f(x) - liczba przedzialow ktore zaczynaja sie na pozycji
    # x lub wczesniej
    # g(x) - liczba przedzialow ktore koncza sie na pozycji
    # x lub wczesniej
    # obliczamy g(b) - f(a)

    pass



if __name__ == '__main__':
    T = [[1,2],[1,3],[2,8],[3,4],[4,7],[3,5],[2,9]]
    print(findrange(T))
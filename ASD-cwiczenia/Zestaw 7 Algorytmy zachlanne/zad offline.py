# Created by Marcin "Cozoob" Kozub at 25.04.2021 21:15
import queue as Q

def huffman(S, F):
    n = len(F)
    # tworze kolejke priorytetowa
    q = Q.PriorityQueue()
    # wsadzam do niej wszystkie czestotliwosci i indeksy symobli
    for i in range(n):
        q.put((F[i], [i]))

    # tablica R posluzy mi do zapisania wynikow w postaci tablic
    R = [[] for _ in range(n)]


    # dopoki nie dotrzemy do korzenia
    while not q.qsize() == 1:
        # laczymy dwa najmniejsze symbole
        # w tablicy R zapisuje od razu wynik w postaci stringa
        item1 = q.get()
        # dla kazdego symbolu w item1 appenduje 1 w tablicy
        for i in item1[1]:
            R[i].append(1)
        item2 = q.get()
        # dla kazdego symbolu w item2 appenduje 0 w tablicy
        for i in item2[1]:
            R[i].append(0)
        # lacze item1 oraz item2 i wrzucam do kolejki
        T = item1[1]
        T.extend(item2[1])
        newitem = (item1[0] + item2[0], T)
        q.put(newitem)

    # counter to dlugosc napisu
    # wypisuje symbole i ich kod liczac dlugosc napisu
    counter = 0
    for i in range(n):
        print(S[i], ":", end=' ')
        for elem in R[i]:
            print(elem, end='')
        print(end='\n')
        counter += (len(R[i]) * F[i])
    print("dlugosc napisu:", counter)


if __name__ == '__main__':
    print("1 test")
    S = ["a", "b", "c", "d", "e", "f"]
    F = [10, 11, 7, 13, 1, 20]
    # symbol "a" ma czestosc 10, symbol "b" ma czestosc 11 itd.
    huffman(S,F) # 150
    print()
    print("2 test")
    S = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p", "r", "s", "t", "u", "w", "y", "z",
         "q"]
    F = [865, 395, 777, 912, 431, 42, 266, 989, 524, 498, 415, 941, 803, 850, 311, 992, 489, 367, 598, 914, 930, 224,
         517]
    huffman(S,F) # 61477
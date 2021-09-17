# Prosze zaproponowac algorytm, który majac dane dwa słowa A i B o długosci n, kazde nad
# alfabetem długosci k, sprawdza czy A i B sa swoimi anagramami.
# 1. Prosze zaproponowac rozwiazanie działajace w czasie O(n + k).
# 2. Prosze zaproponowac rozwiazanie działajace w czasie O(n) (prosze zwrócic uwage, ze k moze byc duzo
# wieksze od n—np. dla alfabetu unicode; złozonosc pamieciowa moze byc rzedu O(n + k)).
# Prosze zaimplementowac oba algorytmy.

# 1. Wersja O(n+k)
import random

# alloc to imitacja dzialania funkcji w C ktora alokuje tablice
# o wielkosci n w czasie O(1) z randomowymi wartosciami
# w Pythonie niestety tworzenie tablicy o dlg n to zawsze O(n)
def alloc(n):
    return [random.randint(0, 1000000000) for _ in range(n)]

def checkanagrams1(word1, word2, alphabet):
    if len(word1) != len(word2):
        return False

    # tworze tablice ktora pod odpowiednim indeksem
    # zapisuje ile jest liter
    count = [0 for _ in range(len(alphabet))]

    for i in range(len(word1)):
        letter = word1[i]
        for j in range(len(alphabet)):
            if alphabet[j] == letter:
                count[j] += 1

    for a in range(len(word2)):
        letter = word2[a]
        for b in range(len(alphabet)):
            if alphabet[b] == letter:
                count[b] -= 1

    # sprawdzamy czy wszystkie wyrazy w count sa rowne 0
    # jesli tak to znaczy ze word1 i word2 sa anagramami
    for c in range(len(count)):
        if count[c] != 0:
            return False

    return True


# 2. Wersja O(n)
def checkanagrams(word1, word2):

    if len(word1) != len(word2):
        return False

    counters = alloc(2**16)

    for i in range(len(word1)):
        counters[ord(word1[i])] = 0

    for i in range(len(word1)):
        counters[ord(word1[i])] += 1
        counters[ord(word2[i])] -= 1

    for i in range(len(word1)):
        if counters[ord(word1[i])] != 0:
            return False

    return True



if __name__ == '__main__':
    alphabet = "ABCDEFGUPI"
    word1 = "DUPA"
    word2 = "APUD"
    print(word1, word2)
    print(checkanagrams1(word1, word2, alphabet))
    print(checkanagrams(word1, word2))
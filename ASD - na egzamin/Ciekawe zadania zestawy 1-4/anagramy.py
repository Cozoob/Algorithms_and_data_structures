# Created by Marcin "Cozoob" Kozub 25.06.2021
# Zadanie 3. Proszę zaproponować algorytm, który mając dane dwa słowa A i B o długości n, każde nad
# alfabetem długości k, sprawdza czy A i B są swoimi anagramami.
# 1. Proszę zaproponować rozwiązanie działające w czasie O(n + k).
# 2. Proszę zaproponować rozwiązanie działające w czasie O(n) (proszę zwrócić uwagę, że k może być dużo
# większe od n—np. dla alfabetu unicode; złożoność pamięciowa może być rzędu O(n + k)).
# Proszę zaimplementować oba algorytmy.

# 1. To counting sort i sortuje obie slowa i sprawdzam je.
# 2. Nie da sie zrobic w pythonie bo alokacja pamieci zajmie k i przez to ostatecznie i tak O(n + k).
# ALE gdyby nie to to alokujemy tablice dlugosci k (w C zajmuje to O(1)). Zerujemy wszystkie literki
# w tablicy ktore wystepuja w A i w B. Nastepnie dodajmeny +1 dla literek z A i B. I na koniec znow
# idac po literkach w A i B sprawdzamy czy wszystkie jest conajmniej 2.

def are_anagrams(A, B):
    if len(A) != len(B):
        return False

    n = len(A)
    k = 256
    # "alokuje" tablice
    inf = float("inf")
    T = [inf for _ in range(k)]
    for elem in A:
        T[ord(elem)] = 0
    for elem in B:
        T[ord(elem)] = 0

    for elem in A:
        T[ord(elem)] += 1
    for elem in B:
        T[ord(elem)] -= 1

    for elem in A:
        if T[ord(elem)] != 0:
            return False
    for elem in B:
        if T[ord(elem)] != 0:
            return False

    return True

if __name__ == '__main__':
    A = 'ac'
    B = 'bb'
    print(are_anagrams(A, B))
    A = 'a'
    B = 'fdfdsfsd'
    print(are_anagrams(A, B))
    A = 'care'
    B = 'race'
    print(are_anagrams(A, B))
    A = 'ala'
    B = 'laa'
    print(are_anagrams(A, B))
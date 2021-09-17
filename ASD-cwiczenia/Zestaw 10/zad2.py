# Created by Marcin "Cozoob" Kozub 12.06.2021
# Zadanie 2. (wyścigi) Król Bitocji postanowił zorganizować serię wyścigów samochodowych. Wyścigi
# mają się odbywać po trasach zamkniętych, składających się z odcinków autostrady łączących miasta Bitocji.
# Król chce, żeby każde miasto było zaangażowane w dokładnie jeden wyścig. W tym celu należy sprawdzić,
# czy da się wynająć odpowiednie odcinki autostad. Należy jednak pamiętać o następujących ograniczeniach:
# 1. w Bitocji wszystkie autostrady są jednokierunkowe,
# 2. z każdego miasta wychodzą co najwyżej dwa odcinki autostrady, którymi można dojechać do innych
# miast,
# 3. do każdego miasta dochodzą co najwyżej dwa odcinki autostrady, którymi można przyjechać z innych
# miast,
# Proszę zaproponować algorytm, który mając na wejściu opis sieci autostrad Bitocji sprawdza czy da się
# zorganizować serię wyścigów tak, żeby przez każde miasto przebiegała trasa dokładnie jednego.
# Utrudnienie: Każdy odcinek autostrady ma przedział dopuszczalnych cen i należy wybrać wspólną cenę
# dla wszystkich wynajętych odcinków.

# ZLE BO TRASY MUSZA BYC ZAMKNIETE
# Pomysł: Sortuje topologicznie graf, a nastepnie sprawdzam czy da sie zrobic taka serie wyscigow.
# Zakladam ze wierzcholek 0 ma dostep do wszystkich pozostalych (idk jak szukac takiego wierzcholka w racjonalnym czasie).
# Po posortowaniu jedynie patrze czy z wierzcholka i moge przejsc do i+1 jesli tak to super miedzy i, i+1 miastem bedzie
# przebiegac dalsza czesc wyscigu. Jesli nie to ktorys wyscig konczy sie w i-tym miescie a koleny zaczyna sie w i+1.
# Dodatkowo uzywam countera ktory sprawdza czy w tworzonych wyscigach sa co najmniej dwa miasta bo jesli nie to od razu
# moge zwrocic False.



def races(G):
    n = len(G)
    visited = [False for _ in range(n)]

    def visit(s):
        nonlocal visited, stack, n, G

        visited[s] = True
        for v in range(n):
            if G[s][v] != -1 and not visited[v]:
                visit(v)

        stack.append(s)

    stack = []
    for v in range(n):
        if not visited[v]:
            visit(v)

    stack = stack[::-1]

    counter = 1
    for i in range(n - 1):
        a = stack[i]
        b = stack[i + 1]
        if G[a][b] == -1:
            if counter == 1:
                return False
            counter = 1
        else:
            counter += 1

    # ewentulanie ostatnie miasto w stack moze nie brac udzialu
    if counter == 1:
        return False

    return True

if __name__ == '__main__':
    G0 = [
        [-1, 8, -1, -1, -1, 6, -1, -1],
        [-1, -1, 10, 2, -1, -1, -1, -1],
        [-1, -1, -1, -1, 1, -1, -1, -1],
        [-1, -1, 8, -1, 4, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, 2],
        [-1, -1, -1, 5, -1, -1, 7, -1],
        [-1, -1, -1, -1, -1, -1, -1, 3],
        [-1, -1, -1, -1, -1, -1, -1, -1]
    ]
    print(races(G0))
    G1 = [
        [-1, 2, 1, 3],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1]
    ]
    print(races(G1))
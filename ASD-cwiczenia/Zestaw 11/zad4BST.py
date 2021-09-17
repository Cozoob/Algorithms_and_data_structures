# Created by Marcin "Cozoob" Kozub 13.06.2021

# Zadanie 4. (klocki) Dany jest ciąg klocków (K1, . . . , Kn). Klocek Ki zaczyna sie na pozycji a_i
# i ciągnie
# się do pozycji b_i (wszystkie pozycje to nieujemne liczby naturalne) oraz ma wysokość 1. Klocki układane są po
# kolei–jeśli klocek nachodzi na któryś z poprzednich, to jest przymocowywany na szczycie poprzedzającego
# klocka). Na przykład dla klocków o pozycjach (1, 3), (2, 5), (0, 3), (8, 9), (4, 6) powstaje konstrukcja o
# wysokości trzech klocków. Proszę podać możliwie jak najszybszy algorytm, który oblicza wysokośc powstałej
# konstrukcji.

# Funkcja checker jest tylko po to zeby sprawdzic czy bedzie to dzialac
# Implementuje pomysl Adrianny.

def checker(T):
    n = len(T)
    b = T[0][0]
    for i in range(n):
        b = max(b, T[i][1])

    answers = [0 for _ in range(b + 1)]

    for i in range(n):
        a = T[i][0]
        b = T[i][1]
        for j in range(a, b + 1):
            answers[j] += 1

    return max(answers)


class BSTNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, new_key):
        root = self
        while root.left != None or root.right != None:
            if new_key[0] > root.key[0] or new_key[1] < root.key[1]:
                root.key[0] = min(new_key[0], root.key[0])
                root.key[1] = max(new_key[1], root.key[1])
                root = root.right
            else:
                root = root.left

        if new_key[0] > root.key[0] or new_key[1] < root.key[1]:
            root.key[0] = min(new_key[0], root.key[0])
            root.key[1] = max(new_key[1], root.key[1])
            root.right = BSTNode(new_key)
            root.right.parent = root
        else:
            root.left = BSTNode(new_key)
            root.left.parent = root

    def check_height(self, counter = 0):
        root = self
        w = root


        while root != None:
            if root.right != None:
                w = root.right
                counter += 1


            root = root.left


if __name__ == '__main__':
    T = [(1,3), (2,5), (0,3),(8,9),(4,6)]
    print(checker(T))

    tree = BSTNode(T[0])
    for i in range(1, len(T)):
        tree.insert(T[i])
    print(tree.key)
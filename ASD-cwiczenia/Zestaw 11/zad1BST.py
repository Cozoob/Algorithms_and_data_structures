# Created by Marcin "Cozoob" Kozub 12.06.2021
# Zadanie 1. (Indeksowane drzewa BST) Rozważmy drzewa BST, które dodatkowo w każdym węźle zawierają pole
# z liczbą węzłów w danym poddrzewie. Proszę opisać jak w takim drzewie wykonywać
# następujące operacje:
# 1. znalezienie i-go co do wielkości elementu,
# 2. wyznaczenie, którym co do wielkości w drzewie jest zadany węzeł
# Proszę zaimplementować obie operacje.

# Idea polega na przechodzeniu przez BST w odwrotnej kolejnosci, zachowujac liczbe odwiedzonych wezlow w counterze.
# Przechodze przez wszystkie wezly w kolejnosci malejacej, tj. odwiedzam prawy wezel, a nastepnie lewy
# i kontynuuje rekurencyjnie przez wezly. Podczas przechodzenia przez drzewo sprawdzam czy counter nie jest juz rowny k.
# Pomysl zajebany z geeksforgeeks

# Zlozonosc: O(k + h) = O(n + h) gdzie h to wysokosc drzewa, n to liczba wezlow w drzewie, k ktory k-ty elemeny
# szukamy w najgorszym wypadku k >= n ale wtedy wykona max n + 1 operacji stad O(n + h)

class BSTNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, new_key):
        root = self
        while root.right != None and root.left != None:
            if root.key > new_key:
                root = root.left
            else:
                root = root.right

        while root.right != None and root.key < new_key:
            root = root.right

        w = BSTNode(new_key)
        if root.key > new_key:
            root.left = w
        else:
            root.right = w

        w.parent = root

    def k_th_largest_element(self, k):
        counter = 0
        root = self
        answer = BSTNode(None)

        def rec(root, k):
            nonlocal counter, answer
            if answer.key != None:
                return answer

            if root == None or counter >= k:
                return answer

            # Najpierw ide do najwiekszego elementu wiec ciagle w prawo
            rec(root.right, k)

            # inkrementuje countera
            counter += 1
            # sprawdzam czy dotarlem do tego k-tego najwiekszego elementu w drzewie
            if counter == k:
                # print(root.key)
                answer = root
                return answer

            # jesli nie to zmierzam do lewa
            rec(root.left, k)
            return answer


        return rec(root, k)

if __name__ == '__main__':
    #      20
    #     /  \
    #    8    22
    #   / \
    #  4   12
    #     /  \
    #    10   14

    tree = BSTNode(20)
    tree.insert(22)
    tree.insert(8)
    tree.insert(12)
    tree.insert(4)
    tree.insert(10)
    tree.insert(14)

    k = tree.k_th_largest_element(0)
    print(k.key)
    k = tree.k_th_largest_element(1)
    print(k.key)
    k = tree.k_th_largest_element(2)
    print(k.key)
    k = tree.k_th_largest_element(3)
    print(k.key)
    k = tree.k_th_largest_element(4)
    print(k.key)
    k = tree.k_th_largest_element(5)
    print(k.key)
    k = tree.k_th_largest_element(6)
    print(k.key)
    k = tree.k_th_largest_element(7)
    print(k.key)
    k = tree.k_th_largest_element(8)
    print(k.key)
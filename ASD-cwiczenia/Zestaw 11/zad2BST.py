# Created by Marcin "Cozoob" Kozub 12.06.2021
# Zadanie 2. Proszę zapropnować algorytm, który oblicza sumę wszystkich wartości w drzewie binarnym
# zdefiniowanym na węzłach typu:
# class BNode:
# def __init__( self, value ):
# self.left = None
# self.right = None
# self.parent = None
# self.value = val
# Program może korzystać wyłącznie ze stałej liczby zmiennych (ale wolno mu zmieniać strukturę drzewa, pod
# warunkiem, że po zakończonych obliczeniach drzewo zostanie przywrócone do stanu początkowego.)

# O(n) bez pamieci i obracania ALE mam watpliwosc czy moze nie O(n^2)??? Na stack overflow niby O(n) podaja
# i ze approved answer


class BSTNode:

    # zamienilem tylko value na key
    # i dodaje takie bool czy consumed
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.consumed = False

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

    def find(self, key):
        root = self
        while root != None:
            if root.key == key:
                return root
            elif key < root.key:
                root = root.left
            else:
                root = root.right

def sum_all_Nodes(tree):
    answer = 0

    w = tree
    while w != None:

        if not w.consumed:
            answer += w.key
            w.consumed = True

        if w.left != None and w.left.consumed is False:
            w = w.left
        elif w.right != None and w.right.consumed is False:
            w = w.right
        else:
            w = w.parent

    return answer


if __name__ == '__main__':
    tree = BSTNode(20)
    tree.insert(22)
    tree.insert(8)
    tree.insert(4)
    tree.insert(12)
    tree.insert(10)
    tree.insert(14)

   # print(tree.left.right.left.key)
    #print(sum_all_Nodes(tree)) # odp 90

    tree.insert(5)
    tree.insert(7)
    tree.insert(6)

    # print(tree.left.left.right.right.left.key)
    print(sum_all_Nodes(tree)) # odp 90 + 5 + 6 + 7 = 108
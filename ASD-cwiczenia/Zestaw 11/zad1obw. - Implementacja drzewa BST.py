# Created by Marcin "Cozoob" Kozub 05.06.2021

# Zad1obw. Zaimplementuj poprzednika i nastepnika w drzewie BST.

# Ja zaimplementowałem po prostu cale drzewo BST z jego wszystkimi operacjami.

class BSTNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def find(self, key):
        root = self
        while root != None:
            if root.key == key:
                return root
            elif key < root.key:
                root = root.left
            else:
                root = root.right

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

    def max(self):
        root = self
        while root.right != None:
            root = root.right

    def min(self):
        root = self
        while root.left != None:
            root = root.left

    def remove(self, key):
        w = self.find(key)
        parent = w.parent

        if w.right == None and w.left == None:
            if parent.left == w:
                parent.left = None
            else:
                parent.right = None
        elif w.right == None:
            n = w.left
            n.parent = parent
            if parent.left == w:
                parent.left = n
            else:
                parent.right = n
        elif w.left == None:
            n = w.right
            n.parent = parent
            if parent.left == w:
                parent.left = n
            else:
                parent.right = n
        else:
            # szukamy nastepnika albo poprzednika bez znaczenia
            # ja tutaj zawsze szukam poprzednika
            n = w.left
            n.max()
            k = n.parent
            if k.left == n:
                k.left = None
            else:
                k.right = None

            if parent.left == w:
                parent.left = n
            else:
                parent.right = n

    # poprzednik
    def prev(self, key):
        root = self.find(key)
        if root.left != None:
            root = root.left
            root.max()
        else:
            parent = root.parent
            while parent.left == root:
                root = parent
                parent = parent.parent

                if parent == None:
                    return BSTNode(None)

            root = parent

        return root

    # nastepnik
    def next(self, key):
        root = self.find(key)
        if root.right != None:
            root = root.right
            root.min()
        else:
            parent = root.parent
            while parent.right == root:
                root = parent
                parent = parent.parent

                if parent == None:
                    return BSTNode(None)

            root = parent

        return root

if __name__ == '__main__':
    tree = BSTNode(21)
    # print(tree.key)
    # print(tree.right)
    # print(tree.left)
    # print(tree.parent)
    # print()
    tree.insert(15)
    # print(tree.left.key)
    tree.insert(37)
    # print(tree.right.key)
    # print()
    tree.insert(20)
    x = tree.find(20)
    # print(x.parent.key)
    # print()

    # w drzewie mam 21, 15, 37, 20
    print(tree.next(20).key)
    print(tree.prev(20).key)
    print(tree.next(37).key)
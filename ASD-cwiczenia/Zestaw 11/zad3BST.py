# Created by Marcin "Cozoob" Kozub 13.06.2021
# Zadanie 3. (geny) W pewnym laboratorium genetycznym powstał ciąg sekwencji DNA. Każda sekwencja
# to pewien napis składający się z symboli G, A, T, i C. Przed dalszymi badaniami konieczne jest upewnić się,
# że wszystkie sekwencje DNA są parami różne. Proszę opisać algorytm, który sprawdza czy tak faktycznie
# jest.

# Pomysł tworze sobie drzewo w stylu BST ale takim bardziej przykokszonym gdzie mam left, left-mid, right-mid, right
# dla kazdego wezla. Moim rootem moze byc Node albo literka "D" bo ord("T")>ord("G")> ord("D") >ord(ord("C")>ord("A").
# I po porstu kazda sekwencje DNA wrzucam do tego drzewa i tworze nowy wezel wtw gdy na danym poziomie nie istnieje
# jakas dalsza sekwencja. Uzywajac np flag moge stwierdzic czy nowo dodana sekwencja w drzwie dodala choc jeden nowy
# elemeny jesli nie to znaczy ze nie wszystkie sekwencje DNA sa parami rozne.


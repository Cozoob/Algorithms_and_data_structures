# Created by Marcin "Cozoob" Kozub 30.05.2021

# Zadanie 4. (logarytmy) Mamy dany graf G = (V, E) z wagami w∶ E → N−{0} (dodatnie liczby naturalne).
# Chcemy znalezc scieżkę z wierzchołka u do v tak, by iloczyn wag był minimalny. Omówic rozwiązanie (bez
# implementacji)

# Pomysl: Aby iloczyn wag byl minimalny to wystarczy wszystkie wagi zlogarytmowac i wtedy wykorzystac algorytm Dijkstry.
# Bo log(a) + log(b) = log(ab).
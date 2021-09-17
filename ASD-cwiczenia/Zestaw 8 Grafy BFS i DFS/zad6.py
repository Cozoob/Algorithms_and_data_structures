# Created by Marcin "Cozoob" Kozub 14.05.2021
# (bezpieczny przelot) Dany jest graf G = (V, E), którego wierzchołki reprezentują punkty
# nawigacyjne nad Bajtocją, a krawędzie reprezentują korytarze powietrzne między tymi punktami. Każdy
# korytarz powietrzny ei ∈ E powiązany jest z optymalnym pułapem przelotu pi ∈ N (wyrażonym w metrach).
# Przepisy dopuszczają przelot danym korytarzem jeśli pułap samolotu różni się od optymalnego najwyżej o t
# metrów. Proszę zaproponować algorytm (bez implementacji), który sprawdza czy istnieje możliwość przelotu
# z zadanego punktu x ∈ V do zadanego punktu y ∈ V w taki sposób, żeby samolot nigdy nie zmieniał pułapu.
# Algorytm powinien być poprawny i możliwie jak najszybszy. Proszę oszacować jego złożoność czasową.

# Pomysł: Nasz zakres pułapu po ktorym mozemy latac to P_X = [p_x - t, p_x + t], gdzie p_x to optymalny pułap
# w punkcie x; t to dozowolne odstepstwo od optym. pułapu. Skoro chcemy zeby samolot nigdy nie zmienial pułapu
# to wystarczy ze sprawdzimy BFS'em (lub DFS'em) czy lecac do wierzchołka v (zakres pułapu P_V = [p_v - t, p_v + t])
# pokrywa sie choc w jendym punkcie z zakresem P_X, tzn. czy P_X i P_V maja choc jeden punkt wspolny.
# Gdy mozemy doleciec do wierzcholka v to mamy nowy zakres pulapu P_N = P_X czesc wspolna z P_V.
# Czyli nasz nastepny zakres pulapu (najprawdopodobniej bo nie zawsze) zmniejszyl sie i teraz to wzgledem niego
# sprawdzamy czy do nastepnego wierzcholka mozemy doleciec. Jesli tak to znow bierzmy czesc wspolna itd...
# Jednoczesnie podczas wykonywania algorytmu mozemy sprawdzic czy juz nie dotarlismy do wierzcholka y.
# Jesli tak to zwracamy True. Jesli nasz samolot doleci wszedzie gdzie moze ale nie dolecial do y to zwracamy False.
# Zlozonosc czasowa: O(V + E) - takie jak BFS po prostu.
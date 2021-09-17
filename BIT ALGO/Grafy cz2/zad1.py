# Created by Marcin "Cozoob" Kozub at 10.05.2021 12:55
# Wyobraźmy sobie podziemny labirynt, złożony z ogromnych jaskiń połączonych wąskimi korytarzami.
# W jednej z jaskiń krasnoludy zbudowały swoją osadę, a w każdej z pozostałych jaskiń mieszka znana krasnoludom ilość trolli.
# Krasnoludy chcą zaplanować swoją obronę na wypadek ataku ze strony trolli. Zamierzają w tym celu zakraść się i podłożyć ładunek
# wybuchowy pod jeden z korytarzy, tak aby trolle mieszkające za tym korytarzem nie miały żadnej ścieżki, którą mogłyby dotrzeć do osady krasnoludów.
# Który korytarz należy wysadzić w powietrze, aby odciąć dostęp do krasnoludzkiej osady największej liczbie trolli?

# Pomysł: Znajduje najpierw wszystkie mosty w grafie (czyli krawedzie ktorych usuniecie spowoduje rozspojnienie grafu).
# Następnie wykonuje DFS od wierzcholka osady i zapisuje informacje o najblizszych mostach do osady.
# Dzieki tej informacji wykonuje DFS dla kazdego takiego najblizszego mostu i zliczam ile trolli moze przejsc przez taki most.
# I wybieram do wysadzenia taki most gdzie najwiecej trolli bedzie moglo przejsc.


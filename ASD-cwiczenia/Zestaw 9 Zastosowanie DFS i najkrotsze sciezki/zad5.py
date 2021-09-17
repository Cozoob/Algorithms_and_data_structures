# Created by Marcin "Cozoob" Kozub 30.05.2021

# Zadanie 5. (problem przewodnika turystycznego) Przewodnik chce przewieźć grupę K turystów z
# miasta A do miasta B. Po drodze jest jednak wiele innych miast i między różnymi miastami jeżdzą autobusy o
# różnej pojemności. Mamy daną listę trójek postaci (x, y, c), gdzie x i y to miasta między którymi bezpośrednio
# jeździ autobus o pojemności c pasażerów.
# Przewodnik musi wyznaczyć wspólną trasę dla wszystkich tursytów i musi ich podzielić na grupki tak,
# żeby każda grupka mogła przebyć trasę bez rodzielania się. Proszę podać algorytm, który oblicza na ile
# (najmniej) grupek przewodnik musi podzielić turystów (i jaką trasą powinni się poruszać), źeby wszyscy
# dostali się z A do B.

# Pomysł: Zwykly DFS, gdzie na biezaco sprawdzam jaka jest najmniejsza pojemnosc dla roznych sciezek z A do B.
# Czyli zapisuje w pomocniczej tablicy min_c dla danego wierzcholka jesli w dfs_visit(u) u jest rozne od A.
# Nastepnie wybieram te sciezki z A do B ktore moga wziac jak najwieksza grupe, tak zeby po drodze nie musiala
# sie rozdzielac.
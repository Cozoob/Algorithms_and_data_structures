# Created by Marcin "Cozoob" Kozub 05.06.2021

# zad2obw. Omów w jaki sposób znaleźć maksymalny przepływ w takiej sieci, w której jest
# możliwe kilka ujść i kilka źródeł.

# 1 pomysł: Zatem wystarczy te kilka zrodel/ujsc polaczyc ze soba w jedno zrodlo/ujscie i jesli
# jakies dwa rozne zrodla/ujscia mialy krawedzi do jakiegos wspolnego wierzcholka v, to
# nowa krawedzi z nowego jednego zrodla/ujscia jest suma przeplywow z wczesniejszych krawedzi do wierzcholka v.

# 2 pomysł: Mozna tez kilka zrodel polaczyc krawedziami z jednym "superzrodlem", gdzie krawedzie pomiedzy
# "superzrodlem" a zrodlami beda mialy przeplyw +inf. Analogicznie do ujsc, gdzie bedzie "superujscie".
# Created by Marcin "Cozoob" Kozub 15.05.2021
# Zadanie 3. (ładowanie przyczepy) Mamy przyczepę o pojemności K kilogramów oraz zbiór ładunków
# o wagach w1, . . . , wn. Waga każdego z ładunków jest potęgą dwójki (czyli, na przykład, dla siedmiu ładunków
# wagi mogą wynosić 2, 2, 4, 8, 1, 8, 16, a pojemność przyczepy K = 27). Proszę podać algorytm zachłanny (i
# uzasadnić jego poprawność), który wybiera ładunki tak, że przyczepa jest możliwie maksymalnie zapełniona
# (ale bez przekraczania pojemności) i jednocześnie użyliśmy możliwie jak najmniej ładunków. (Ale jeśli da się
# np. załadować przyczepę do pełna uzywając 100 ładunków, albo zaladować do pojemności K − 1 używając
# jednego ładunku, to lepsze jest to pierwsze rozwiązanie).

# Zawsze bierzemy najwiekszy mozliwy ładunek ktory nieprzekracza obecnej pojemnosci K' <= K. Jest to algorytm poprawny
# poniewaz wagi to co najmniej potegi dwojki.Tzn. ze stosunek dwoch roznych wag k >= 2 (ciezsza/lzejsza),
# co oznacza tyle ze kazda waga wi ZAWSZE moze byc stworzona z pewnej ilosci (2,4,8,...) wag wk, gdzie wi > wk, czyli nie ma sensu
# brac wag wk do rozwiazania bo bedzie ich wieksza ilosc, skoro mozna wziac jedna wage wi (ktora wlasnie moze byc skonstruowana z wag wk).
# XD takie se tlumaczenie ale do mnie przemawia.

def load_trailer(W, K):
    # sortuje wagi rosnąco, aby zawsze moc brac najciezszy mozliwy ladunek
    n = len(W) - 1
    W.sort()
    res = []
    while n > -1 and K > 0:
        if W[n] <= K:
            res.append(W[n])
            K -= W[n]
        n -= 1

    return res, K

if __name__ == '__main__':
    W = [2, 2, 4, 8, 1, 8, 16]
    K = 27
    print(load_trailer(W, K))
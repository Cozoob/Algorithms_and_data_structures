# Created by Marcin "Cozoob" Kozub 15.05.2021
# Zadanie 6. (suma odległości) Dana jest posortowana tablica A zawierająca n liczb i celem jest wyznaczenie liczby x takiej, że wartość
# (od i = 0 do n−1)∑ ∣A[i] − x∣ jest minimalna. Proszę zaproponować algorytm, uzasadnić jego poprawność oraz ocenić złożoność obliczeniową.

# Naszym x-em zawsze bedzie srodkowa wartosc(mediana) z liczb w talicy A.
# O(1)

def find_x(A):
    n = len(A)
    if n % 2 == 1:
        return A[n//2]
    return (A[n//2 - 1] + A[n//2]) / 2
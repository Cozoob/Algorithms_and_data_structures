# (wyszukiwanie binarne) Prosze zaimplementowac funkcje, która otrzymuje na wejsciu posortowana
# niemalejaco tablice A o rozmiarze n oraz liczbe x i sprawdza, czy x wystepuje w A. Jesli tak, to
# zwraca najmniejszy indeks, pod którym x wystepuje.

def binsearch(arr, target):

    def rek_binseaerch(arr, left, right, target):
        if left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                return rek_binseaerch(arr,left, mid - 1, target)
            else:
                return rek_binseaerch(arr,mid + 1, right, target)
        return "doesnt exist"

    return rek_binseaerch(arr, 0, len(arr) - 1, target)

if __name__ == '__main__':
    T = [0, 1, 1, 2, 5, 6, 24, 35, 78]
    print(binsearch(T, 2))
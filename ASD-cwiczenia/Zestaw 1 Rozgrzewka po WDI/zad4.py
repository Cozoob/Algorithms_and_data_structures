# Prosze zaimplementowac funkcje, która majac na wejsciu tablice n elementów
# oblicza jednoczesnie jej najwiekszy i najmniejszy element wykonujac 1.5n porównan.

def findmaxandmin(arr):
    smallest = arr[0]
    biggest = arr[0]
    for i in range(1, len(arr), 2):
        # sprawdzam dwa kolejne elementy ze soba i ten wiekszy
        # sprawdzam czy jest wieksza od biggesta ten mniejszy czy jest
        # mniejszy od smallest stad mam 3/2 porownan
        # problem moze sie nadarzyc gdy jest niaparzysta liczba
        # elementow w tablicy wtedy ostatni element porownujemy osobno
        # z biggest i smallest
        if i == len(arr) - 1:
            # czyli sytuacja gdy arr ma nieparzysta liczbe elementow
            if biggest < arr[i]:
                biggest = arr[i]
            elif smallest > arr[i]:
                smallest = arr[i]
        else:
            if arr[i] > arr[i + 1]:
                if arr[i] > biggest:
                    biggest = arr[i]
                if arr[i + 1] < smallest:
                    smallest = arr[i + 1]
            else:
                if arr[i+1] > biggest:
                    biggest = arr[i+1]
                if arr[i] < smallest:
                    smallest = arr[i]
    return smallest, biggest

if __name__ == '__main__':
    arr = [7, 4, 9, 1, 3, 5, 21, 67, 74]
    print(arr)
    print(findmaxandmin(arr))
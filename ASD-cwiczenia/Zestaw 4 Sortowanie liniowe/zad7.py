# Dana jest tablica A zawierajaca n elementów, z których kazdy ma jeden z k kolorów. Prosze
# podac mozliwie jak najszybszy algorytm, który znajduje indeksy i oraz j takie, ze wsród elementów
# A[i],A[i + 1], . . . ,A[j] wystepuja wszystkie k kolorów oraz wartosc j − i jest minimalna (innymi słowy,
# szukamy najkrótszego przedziału z wszystkimi kolorami).

def maxspan(A):
    n = len(A)
    min_ = A[0]
    max_ = A[0]
    # szukamy min i max w A zeby wiedziec jaki jest zakres
    for i in range(n):
        min_ = min(min_, A[i])
        max_ = max(max_, A[i])

    # tworze sobie n kubeczkow
    B = [[] for _ in range(n)]
    # x zawiera info jaka wielkosc maja przedzialy w kubeczkach
    x = (max_ + min_) / n

    for i in range(n):
        d = int((A[i] - min_)/x)
        B[d].append(A[i])

    result = 0
    prev_max = max(B[0])
    for i in range(1, n):
        if len(B[i]) != 0:
            act_min = min(B[i])
            result = max(result, act_min - prev_max)
            prev_max = max(B[i])

    return result
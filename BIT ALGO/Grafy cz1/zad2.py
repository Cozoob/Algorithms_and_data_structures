from queue import Queue
# Created by Marcin "Cozoob" Kozub at 08.05.2021 17:27
# Otrzymujemy na wejściu listę par ludzi, które się wzajemnie znają. Osoby są reprezentowane przez liczby od 0 do n - 1.
# Dnia pierwszego osoba 0 przekazuje pewną wiadomość wszystkim swoim znajomym. Dnia drugiego każdy ze znajomych przekazuje
# tę wiadomość wszystkim swoim znajomym, którzy jej jeszcze nie znali, i tak dalej.
# Napisz algorytm, który zwróci dzień, w którym najwięcej osób poznało wiadomość oraz ilość osób, które tego dnia ją otrzymały.

# znow korzystam z DFS pomysl dosc podobny jak do topologicznego sortowania tylko ze zapisuje time.

def chatter_dfs(graph, s):
    n = len(graph)
    visited = [False] * n
    time = [None] * n


    curr_time = 0
    def dfs_visited(u, curr_time):
        nonlocal graph, visited, time

        # zapisuje czas curr_time dotarcia plotki w talbicy time dla wierzcholka u
        visited[u] = True
        time[u] = curr_time
        curr_time += 1
        for v in graph[u]:
            if not visited[v]:
                dfs_visited(v, curr_time)

    dfs_visited(s, curr_time)
    # szukam maksymalnego czasu jednoczesnie zliczajac ile takich osob z maksymalnym czasem jest
    counter = 1
    max_time = time[0]
    for i in range(1, n):
        if time[i] == max_time:
            counter += 1
        if time[i] > max_time:
            max_time = time[i]
            counter = 1

    return time, max_time, counter

# ok niby z bfs lepsze rozwizanie zatem z bfs:
# imo to samo
def chatter_bfs(graph, s):
    n = len(graph)
    queue = Queue()
    visited = [False] * n
    time = [0] * n

    queue.put(s)
    visited[s] = True

    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                time[v] = time[u] + 1
                queue.put(v)

    counter = 1
    max_time = time[0]
    for i in range(1, n):
        if max_time == time[i]:
            counter += 1
        if max_time < time[i]:
            max_time = time[i]
            counter = 1

    return time, max_time, counter

if __name__ == '__main__':
    g1 = [
        [1],
        [0, 2, 3, 4],
        [1],
        [1],
        [1, 5, 6],
        [4],
        [4, 7],
        [6]
    ]
    print(chatter_dfs(g1,4))
    print(chatter_bfs(g1, 4))
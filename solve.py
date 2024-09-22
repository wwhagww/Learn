from heapq import heappush, heappop
V, E, st = map(int, input().split())
INF = int(1e9)

graph = [{} for _ in range(V)]
graph_inv = [{} for _ in range(V)]
for _ in range(E):
    a, b, t = map(int,input().split())
    graph[a-1][b-1] = t
    graph_inv[b-1][a-1] = t

table = [INF]*V
q = [(0, st-1)]
table[st-1] = 0
while q:
    d, i = heappop(q)
    if table[i] < d:
        continue
    for ni, nd in graph[i].items():
        if d+nd < table[ni]:
            table[ni] = d+nd
            heappush(q, (d+nd, ni))

table_inv = [INF]*V
q = [(0, st-1)]
table_inv[st-1] = 0
while q:
    d, i = heappop(q)
    if table_inv[i] < d:
        continue
    for ni, nd in graph_inv[i].items():
        if d+nd < table_inv[ni]:
            table_inv[ni] = d+nd
            heappush(q, (d+nd, ni))

max_time = 0
for i in range(V):
    if max_time < table[i]+table_inv[i]:
        max_time = table[i]+table_inv[i]
print(max_time)
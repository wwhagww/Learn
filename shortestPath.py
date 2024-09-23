from heapq import heappop, heappush

def dijkstra(graph, start):
    # graph는 인접리스트 [{인접노드: 거리, ...}, ...]
    # start는 출발 노드
    # dist(거리 리스트), prev(경로 위한..) return
    INF = int(1e9)
    dist = [INF] * len(graph)
    dist[start] = 0
    prev = [None] * len(graph)

    pq = [(0, start)] # (거리, 노드번호)
    while pq:
        cur_dist, cur_node = heappop(pq)
        if cur_dist > dist[cur_node]: continue
        for node, weight in graph[cur_node].items():
            new_dist = cur_dist + weight
            if new_dist < dist[node]:
                dist[node] = new_dist
                prev[node] = cur_node
                heappush(pq, (new_dist, node))
    return dist, prev

def trackPath(prev, st, ed):
    if prev[ed] is None: 
        return []
    cur = ed
    path = [ed]
    while cur != st:
        cur = prev[cur]
        path.append(cur)
    path.reverse()
    return path

# 코드 몸체

# V, E = map(int, input().split())
V = int(input())
E = int(input())

graph = [{} for _ in range(V)]
for _ in range(E):
    a, b, w = map(int, input().split())
    a, b = a-1, b-1 # 0-based index로 변환
    if (b in graph[a]) and (graph[a][b] < w):
        continue # 두 정점 사이 중복된 간선이 있을 때, 더 긴 간선은 무시
    graph[a][b] = w
    # graph[b][a] = w # 양방향 간선일 경우

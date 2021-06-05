from collections import defaultdict
import heapq


def dijkstra(v, graph, N):
    INF = 1001001001
    dist = [INF] * N
    dist[v] = 0
    heap = [(0, v)]
    heapq.heapify(heap)
    while heap:
        now_d, v = heapq.heappop(heap)
        # 上書きを防ぐ
        if dist[v] < now_d:
            continue
        dist[v] = now_d
        for next_v, d in graph[v]:
            # 候補外のものはheapにpushしない
            if now_d+d > dist[next_v]:
                continue
            heapq.heappush(heap, (now_d+d, next_v))
    return dist


def main():
    # data load
    N, M = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1;b -= 1
        graph[a].append((b, c))
        graph[b].append((a, c))

    # 始点0と終点N-1で2回ダイクストラ
    from_1 = dijkstra(0, graph, N)
    to_N = dijkstra(N-1, graph, N)
 
    # 結果を順に格納
    result = []
    for i in range(N):
        value = from_1[i] + to_N[i]
        result.append(value)
    
    # output
    print(*result, sep='\n')
    return


if __name__ == '__main__':
    main()

from collections import defaultdict, deque


def main():
    # data load
    N = int(input())
    edges = defaultdict(list)
    for _ in range(N-1):
        a, b = map(lambda x:int(x)-1, input().split())
        edges[a].append(b)
        edges[b].append(a)

    # 仮にv = 0 から捜索して, 一番遠い頂点を求める
    sv, dist = 0, [0] * N
    que = deque()
    que.append((sv, -1))
    while que:
        v, p = que.popleft()
        for next_v in edges[v]:
            if next_v == p:
                continue
            que.append((next_v, v))
            last_v = next_v
    que.append((last_v, -1))

    # 端っこの頂点(last_v)から初めて一番遠い頂点vを求め,
    # 2頂点を結んだ閉路の長さである dist[v]+1 が答えになる
    while que:
        v, p = que.popleft()
        for next_v in edges[v]:
            if next_v == p:
                continue
            dist[next_v] = dist[v] + 1
            que.append((next_v, v))
    
    # output
    print(max(dist)+1)
    return
if __name__ == '__main__':
    main()

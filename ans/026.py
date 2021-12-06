from collections import defaultdict, deque


def main():
    # data load
    N = int(input())
    tree = defaultdict(list)
    for _ in range(N-1):
        a, b = map(lambda x:int(x)-1,  input().split())
        tree[a].append(b)
        tree[b].append(a)
    
    color = [-1] * N
    q = deque([(0, -1)])
    color[0] = 0

    while q:
        v, p = q.popleft()
        for nxt_v in tree[v]:
            if nxt_v == p:
                continue
            color[nxt_v] = 1 - color[v]
            q.append((nxt_v, v))
    
    if color.count(0) < N // 2:
        # 1で塗られた色の方が多い.
        print(*[idx+1 for idx, c in enumerate(color) if c == 1][:N//2])
    else:
        print(*[idx+1 for idx, c in enumerate(color) if c == 0][:N//2])


if __name__ == '__main__':
    main()

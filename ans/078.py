from collections import defaultdict


def main():
    # data load
    N, M = map(int, input().split())
    edges = defaultdict(list)
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        edges[a].append(b)
        edges[b].append(a)
    
    # vより頂点番号が小さい隣接頂点がちょうど1つ存在するか否か
    def check(v: int) -> bool:
        cnt = 0
        for next_v in edges[v]:
            if next_v < v:
                cnt += 1
        if cnt == 1:
            return True
        return False
    
    # 各vについて計算し, output
    result = 0
    for v in range(N):
        result += check(v)
    print(result)


if __name__ == '__main__':
    main()

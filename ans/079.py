import sys


def main():
    # data load
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [list(map(int, input().split())) for _ in range(H)]

    cnt = 0
    dxdy = [(0, 0), (0, 1), (1, 0), (1, 1)]
    # 左上の合わせ方は一意に決まる. 帰納的にその隣接点についても一意に定まる.
    # xが端までくる or yが端まで来たときに一致してなかったらNo
    for x in range(H):
        for y in range(W):
            if A[x][y] == B[x][y]:
                continue
            if y == W - 1:
                if B[x][y] != A[x][y]:
                    print('No')
                    sys.exit()
            elif x == H - 1:
                if B[x][y] != A[x][y]:
                    print('No')
                    sys.exit()
            else:
                # B[x][y]の座標を合わせる.
                delta = B[x][y] - A[x][y]
                for dx, dy in dxdy:
                    B[x + dx][y + dy] -= delta
                cnt += abs(delta)
    
    # output
    print('Yes')
    print(cnt)


if __name__ == '__main__':
    main()

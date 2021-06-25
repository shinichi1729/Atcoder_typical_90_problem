def main():
    # data load
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]

    res = -1
    move = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def dfs(h, w, cnt):
        nonlocal res, sh, sw
        grid[h][w] = '#'
        for dh, dw in move:
            nh, nw = h+dh, w+dw
            if 0 <= nh < H and 0 <= nw < W:
                if grid[nh][nw] == '.':
                    dfs(nh, nw, cnt+1)
                elif nh == sh and nw == sw and cnt > 2:
                    res = max(res, cnt)
        grid[h][w] = '.'

    for h in range(H):
        for w in range(W):
            # 全ての座標をスタート位置にして全探索(DFS)
            if grid[h][w] == '.':
                sh, sw = h, w
                dfs(h, w, 1)

    # output
    print(res)
    return


if __name__ == '__main__':
    main()

def main():
    # data load
    N = int(input())
    data = []
    md = 0
    for _ in range(N):
        d, c, s = map(int, input().split())
        data.append((d, c, s))
        md = max(md, d)
    data.sort(key=lambda x:x[0])

    # dp[i][j]: i番目までの仕事の中で, j日目まで考慮した時に達成しうる最大値
    # メモリ削減のため直前のi-1番目までの値のみ記憶 (bitで反転させている)
    dp = [[0] * (md+1) for _ in range(2)]
    for i in range(N):
        bit = i % 2
        for j in range(1, md+1):
            if j >= data[i][1] and j <= data[i][0]:
                dp[bit][j] = max(dp[1-bit][j], dp[1-bit][j-data[i][1]] + data[i][2])
            dp[bit][j] = max(dp[bit][j], dp[bit][j-1], dp[1-bit][j])

    # output
    print(dp[bit][-1])
    return

if __name__ == '__main__':
    main()

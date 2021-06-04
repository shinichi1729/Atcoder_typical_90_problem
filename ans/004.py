def main():
    # data load
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    H_sum, W_sum = [], []

    # 横方向の和を求め, H_sumに格納
    for h in range(H):
        H_sum.append(sum(A[h]))

    # 縦方向の和を求め, W_sumに格納
    for w in range(W):
        W_sum.append(sum([A[i][w] for i in range(H)]))

    result = [[None] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            # 重複 (A[h][w]) を引くことを忘れない.
            result[h][w] = H_sum[h] + W_sum[w] - A[h][w]

    # output
    for line in result:
        print(*line)

if __name__ == '__main__':
    main()

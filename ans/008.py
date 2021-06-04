def main():
    # data load
    N = int(input())
    S = input()
    atcoder, mod = 'atcoder', 10**9+7

    # dp[i][j]: atcoderのi文字までを, Sのj文字目までで作れる総数
    dp = [[0] * (N+1) for _ in range(len(atcoder)+1)]
    dp[0] = [1] * (N+1)
    for i in range(1, len(atcoder)+1):
        for j in range(1, N+1):
            if atcoder[i-1] == S[j-1]:
                dp[i][j] += dp[i-1][j-1]
            dp[i][j] += dp[i][j-1]
            dp[i][j] %= mod

    # output
    print(dp[-1][-1])
    return

if __name__ == '__main__':
    main()

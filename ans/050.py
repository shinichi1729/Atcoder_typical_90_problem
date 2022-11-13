def main():
    MOD = 10**9+7
    # data load
    N, L = map(int, input().split())

    # cnt[k]: k段目にいるときの移動方法の総和のmod
    cnt = [0] * (N + 1)
    cnt[0] = 1
    for k in range(N):
        cnt[k+1] += cnt[k]
        cnt[k+1] %= MOD
        if k+L <= N:
            cnt[k+L] += cnt[k]
            cnt[k+L] %= MOD

    # output
    print(cnt[N] % MOD)


if __name__ == '__main__':
    main()

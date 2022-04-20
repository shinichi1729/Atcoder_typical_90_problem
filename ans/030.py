def main():
    # data load
    N, K = map(int, input().split())

    # エラトステネスの篩の考え方.
    sieve = [0] * (N+1)
    for p in range(2, N+1):
        if sieve[p]:
            # 素数ではないならスルー
            continue
        for np in range(p, N+1, p):
            sieve[np] += 1

    print(sum([s >= K for s in sieve]))
    return


if __name__ == '__main__':
    main()

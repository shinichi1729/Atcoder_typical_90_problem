def main():
    # data load
    N, K = map(int, input().split())

    mod = 10 ** 9 + 7
    if N == 1:
        res = K
    elif N == 2:
        res = K * max(0, K-1)
    else:
        res = K * max(0, K-1) * max(0, pow(K-2, N-2, mod))

    # output
    res %= mod
    print(res)
    return


if __name__ == '__main__':
    main()

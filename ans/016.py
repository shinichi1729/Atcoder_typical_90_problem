def main():
    # data load
    N = int(input())
    coins = sorted(list(map(int, input().split())))
    A, B, C = coins

    res = 1001001001
    for c in range(N // C, -1, -1):
        now = N - c * C
        for b in range(min(99999-c, now // B), -1, -1):
            if (now - b*B) % A == 0:
                a = (now - b*B) // A
                res = min(res, a+b+c)

    # output
    print(res)
    return


if __name__ == '__main__':
    main()

def main():
    # data load
    N = int(input())
    X, Y = [], []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    X.sort()
    Y.sort()
    # XとY独立に考えて中央値を選べば最小
    medium_x, medium_y = X[N//2], Y[N//2]
    res = 0
    for i in range(N):
        res += abs(X[i] - medium_x)
        res += abs(Y[i] - medium_y)

    # output
    print(res)
    return


if __name__ == '__main__':
    main()

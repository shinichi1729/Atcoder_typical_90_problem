def main():
    # data load
    N = int(input())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    # 交錯する場合は交錯しないように選んだ時より必ず大きくなる
    # よってsortした(A,B)を端から順に絶対値をとっていったときの総和が答え
    res = 0
    for i in range(N):
        res += abs(A[i] - B[i])
    print(res)
    return


if __name__ == '__main__':
    main()

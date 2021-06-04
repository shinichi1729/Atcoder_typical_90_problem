def main():
    # data load
    N, K = map(int, input().split())
    data = [None] * 10**5

    # もし同じ数字が出てきたらbreakして周期を求める
    cnt = 0  # 何回変化させたかをcntに格納
    while True:
        if data[N] is not None or K < cnt-1:
            cnt -= 1
            break
        data[N] = cnt
        cnt += 1
        N += sum([int(i) for i in str(N)])
        N %= 10**5

    # output
    if K <= cnt:  # Kが２周期以降に入らない場合
        print(data.index(K))
    else:
        K -= data[N]
        cycle = cnt - data[N] + 1
        K %= cycle
        K = K+data[N]
        print(data.index(K))


if __name__ == '__main__':
    main()

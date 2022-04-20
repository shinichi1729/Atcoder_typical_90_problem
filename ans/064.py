def main():
    # data load
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    dx = []  # 一つ前との値の差を管理する配列
    total = 0
    for i in range(N-1):
        dx.append(A[i+1] - A[i])
        total += abs(dx[-1])

    for _ in range(Q):
        l, r, v = map(int, input().split())
        if l != 1:
            before = dx[l-2]
            nxt = before + v
            dx[l-2] = nxt
            total -= abs(before) - abs(nxt)
        if r != N:
            before = dx[r-1]
            nxt = before - v
            dx[r-1] = nxt
            total -= abs(before) - abs(nxt)
        print(total)

    return


if __name__ == '__main__':
    main()

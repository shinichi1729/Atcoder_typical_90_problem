import bisect


def main():
    # data load
    N = int(input())
    A = sorted(list(map(int, input().split())))
    Q = int(input())
    B = []
    for _ in range(Q):
        B.append(int(input()))

    # 2分探索
    result = []
    for b in B:
        value = 1001001001
        right = bisect.bisect_right(A, b)
        left = right - 1
        if right < N:
            value = abs(A[right] - b)
        value = min(value, abs(A[left] - b))
        result.append(value)

    # output
    print(*result, sep='\n')
    return


if __name__ == '__main__':
    main()

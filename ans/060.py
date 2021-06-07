# 二分探索でvalueの入る位置の右側探索
def check(dp, now, value):
    left, right = -1, now
    while right-left > 1:
        mid = (left + right) // 2
        if dp[mid] <= value:
            left = mid
        else:
            right = mid
    return right


def solve(N, A):
    dp = [0] * N
    dp[0] = A[0]
    now = 1  # dp[now]: 一番左にある0のindex
    res = [0] * N
    res[0] = 1
    for i in range(1, N):
        a = A[i]
        insert = check(dp, now, a)
        if insert == 0 or dp[insert-1] != a:
            dp[insert] = a
            if insert == now:
                now += 1
        res[i] = now
    return res


def main():
    # data load
    N = int(input())
    A = list(map(int, input().split()))

    # 左から見た結果をres1 / 右から見た結果をres2に保存
    res1 = solve(N, A)
    res2 = solve(N, list(reversed(A)))

    # output
    res = 0
    for i in range(N):
        res = max(res, res1[i]+res2[N-i-1] - 1)
    print(res)
    return


if __name__ == '__main__':
    main()

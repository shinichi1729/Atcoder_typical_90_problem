# 区間dpによる解法
def main():
    # data load
    N = int(input())
    A = list(map(int, input().split()))

    INF = ''
    dp = [[INF] * (2*N) for i in range(2*N, 0, -1)]
    for left in range(2*N-1, -1, -1):
        for right in range(left+1, 2*N, 2):
            if right-left == 1:
                dp[left][right] = abs(A[left] - A[right])
                continue
            dp[left][right] = dp[left+1][right-1]+abs(A[right]-A[left])
            for k in range(1, right-left, 2):
                dp[left][right] = min(dp[left][right], dp[left][left+k]+dp[left+k+1][right])
    print(dp[0][-1])


if __name__ == '__main__':
    main()

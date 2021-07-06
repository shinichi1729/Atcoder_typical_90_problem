import sys


def two_dim_cumulative_sum(grid, rows, cols) -> None:
    for row in range(rows):
        for col in range(1, cols):
            grid[row][col] += grid[row][col-1]
    for row in range(1, rows):
        for col in range(cols):
            grid[row][col] += grid[row-1][col]
    return


def main():
    # data load
    N, K = map(int, input().split())
    data = []
    for _ in range(N):
        A, B = map(int, input().split())
        data.append((A, B))

    # gridにデータを当てはめて二次元累積和
    grid = [[0]*5001 for _ in range(5001)]
    rows, cols = len(grid), len(grid[0])
    for a, b in data:
        grid[a][b] += 1
    # for line in grid[:100]:
    #     print(line[:100])
    # sys.exit()
    two_dim_cumulative_sum(grid, rows, cols)

    # 左上を決めると他の三点も一意に定まる. 左上の候補を全探索
    result = 0
    for row in range(5001-K-1):
        for col in range(5001-K-1):
            upper_left, upper_right = grid[row][col], grid[row][col+K+1]
            lower_left, lower_right = grid[row+K+1][col], grid[row+K+1][col+K+1]
            value = lower_right - upper_right - lower_left + upper_left
            result = max(result, value)

    # output
    print(result)
    return


if __name__ == '__main__':
    main()

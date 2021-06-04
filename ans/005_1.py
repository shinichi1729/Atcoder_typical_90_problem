# 行列の積を求める関数 (各値はmod 10 ** 9 + 7 をとっている)
def dot(x, y):
    mod = 10**9 + 7
    z = [[0] * len(y[0]) for _ in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x)):
            for k in range(len(x)):
                z[i][k] += x[i][j] * y[j][k]
                z[i][k] %= mod
    return z

# 行列のN乗をO(logN)で計算
def powers(matrix, N):
    # 2分累乗の値をここに入れていく.
    data = [None] * 64
    data[0] = matrix
    for i in range(1, 64):
        data[i] = dot(data[i-1], data[i-1])

    identity_matrix = [[1 if i == j else 0 for i in range(len(matrix))]
                       for j in range(len(matrix))]
    matrix_pow = identity_matrix
    for i in range(62):
        if (1 << i) & N:
            matrix_pow = dot(matrix_pow, data[i])
    return matrix_pow


# 行列累乗による解法
def main():
    # data load
    N, B, K = map(int, input().split())
    C = list(map(int, input().split()))

    # 行列生成
    matrix = [[0] * B for _ in range(B)]
    for i in range(B):
        for k in range(K):
            next = (i*10+C[k]) % B
            matrix[i][next] += 1

    # 行列累乗
    matrix_pow = powers(matrix, N)

    # output -> 答えはmatrix_pow * [1, 0, 0, .., 0] の積
    print(matrix_pow[0][0])
    return


if __name__ == '__main__':
    main()

def main():
    # data load
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    # 今どれだけ右shiftしたかを変数shiftで管理. Nでmodを取ることを忘れない
    result, shift = [], 0
    for _ in range(Q):
        t, x, y = map(int, input().split())
        if t == 1:
            X, Y = (x-shift-1) % N, (y-shift-1) % N
            A[X], A[Y] = A[Y], A[X]
        elif t == 2:
            shift += 1
            shift %= N
        else:
            result.append(A[x-shift-1])

    # output
    print(*result, sep='\n')
    return


if __name__ == '__main__':
    main()



def main():
    # data load
    N = int(input())
    S = input()

    # leftは同じ色で何個続くか, 結果にleftの候補(N-left-1)個とleftの積を足していく
    left, result = 0, 0
    while left < N:
        cnt = 1
        while left < N-1 and S[left] == S[left+1]:
            left += 1
            cnt += 1
        result += cnt * (N-left-1)
        left += 1

    # output
    print(result)
    return


if __name__ == '__main__':
    main()

import operator


def solve(right_side, mod, ope=operator.add):
    left_side, res = 1, 0
    # 桁ごとに演算する, left_sideからrの区間は常に桁が等しい.
    while left_side <= right_side:
        r = min(right_side, left_side*10-1)
        value = (((r+left_side)*(r-left_side+1)) // 2 % mod)\
                * len(str(left_side))
        res = ope(res, value)
        left_side *= 10
    return res


def main():
    # data load
    L, R = map(int, input().split())
    L -= 1
    result, mod = 0, 10**9+7
    
    result += solve(R, mod)
    result += solve(L, mod, ope=operator.sub)

    # output
    print(result % mod)
    return


if __name__ == '__main__':
    main()

from typing import List


# 最小値の最大化は2分探索
def check(value: int, K: int, A: List[int]) -> bool:
    cnt, block = 0, 0
    for i in range(1, len(A)):
        if block + (A[i]-A[i-1]) >= value:
            cnt += 1
            block = 0
        else:
            block += (A[i]-A[i-1])
    if cnt >= K+1:
        return True
    return False


def main():
    # data load
    N, L = map(int, input().split())
    K = int(input())
    A = [0] + list(map(int, input().split())) + [L]

    # binary search
    ok, ng = 1, L+1
    while ng-ok > 1:
        mid = (ng+ok) // 2
        if check(mid, K, A):
            ok = mid
        else:
            ng = mid

    # output
    print(ok)
    return


if __name__ == '__main__':
    main()


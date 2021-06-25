import sys
from typing import List


def judge(numbers: List[int], target) -> bool:
    N = len(numbers)
    left, right = 0, 1
    while left < N-1 and right < N:
        if numbers[right] - numbers[left] > target:
            left += 1
        elif numbers[right] - numbers[left] < target:
            right += 1
        else:
            return True
    return False


def main():
    # data load
    N = int(input())
    A = list(map(int, input().split()))

    tenth = sum(A) / 10
    if not tenth.is_integer():
        print('No')
        sys.exit()

    A_accum = [0, A[0]]
    flag = False
    for i in range(1, N):
        A_accum.append(A[i]+A_accum[-1])

    # 答えは2パターン
    # Aを巡回的に取る. -> ..A1+A0+AN+AN-1+..
    if judge(A_accum, tenth):
        flag = True
    # そのまま部分列を取る -> Al+Al+1+..Ar
    if judge(A_accum, A_accum[-1] - tenth):
        flag = True

    if flag:
        print('Yes')
    else:
        print('No')
    return


if __name__ == '__main__':
    main()

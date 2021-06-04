from collections import defaultdict
import bisect


def main():
    # data load
    N, K = map(int, input().split())
    S = input()

    # 各アルファベットのインデックスをdictで管理
    position = defaultdict(list)
    for i in range(N):
        s = S[i]
        position[s].append(i)
    position = list(zip(position.keys(), position.values()))
    position.sort(key = lambda x: x[0])

    # 今どこまで加えたかをnowで更新
    result, now = '', -1
    for i in range(K):
        rest = K - i - 1
        for key, value in position:
            left = bisect.bisect_left(value, now+1)
            right = bisect.bisect_right(value, N-rest-1)
            if right - left >= 1:
                result += key
                now = value[left]
                break

    # output
    print(result)
    return


if __name__ == '__main__':
    main()

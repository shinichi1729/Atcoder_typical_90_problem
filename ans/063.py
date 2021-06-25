from collections import defaultdict


def main():
    # data load
    H, W = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(H)]

    res = 0
    # bit で選ぶ行を決める
    for bit in range(1, 2**H):
        line = []
        count = defaultdict(int)
        for i in range(H):
            if bit >> i & 1:
                line.append(i)
        # 選んだ行で全てnumで同じ成分ならcount[num] += 1
        for w in range(W):
            if all([P[line[0]][w] == P[h][w] for h in line]):
                count[P[line[0]][w]] += 1
        # 同じ成分の数*選んだ行の数でresを更新
        for key, value in count.items():
            res = max(res, value*len(line))

    # output
    print(res)
    return


if __name__ == '__main__':
    main()

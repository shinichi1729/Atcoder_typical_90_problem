from collections import Counter


def main():
    # data load
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # mod46 の世界で要素を考える
    A = Counter([a % 46 for a in A])
    B = Counter([b % 46 for b in B])
    C = Counter([c % 46 for c in C])

    # 全探索 o(46^3)
    ans = 0
    for a in range(46):
        for b in range(46):
            for c in range(46):
                if (a + b + c) % 46 == 0:
                    ans += A[a] * B[b] * C[c]

    # output
    print(ans)
    return


if __name__ == '__main__':
    main()

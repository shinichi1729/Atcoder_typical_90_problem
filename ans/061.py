from collections import deque


def main():
    # data load
    Q = int(input())
    deq = deque()  # 両端キュー(double-ended que)を使う

    result = []
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            deq.append(x)
        elif t == 2:
            deq.appendleft(x)
        else:
            result.append(deq[-x])

    # output
    print(*result, sep='\n')
    return


if __name__ == '__main__':
    main()


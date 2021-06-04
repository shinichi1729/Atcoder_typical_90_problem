def main():
    # data load
    N = int(input())
    classes = [[0], [0]]
    for _ in range(N):
        a, b = map(int, input().split())
        a -= 1
        classes[a].append(b+classes[a][-1])
        classes[1-a].append(classes[1-a][-1])

    # クエリ処理
    result = []
    Q = int(input())
    for _ in range(Q):
        left, right = map(int, input().split())
        class1 = classes[0][right] - classes[0][left-1]
        class2 = classes[1][right] - classes[1][left-1]
        result.append((class1, class2))

    # output
    for score in result:
        print(*score)
    return


if __name__ == '__main__':
    main()

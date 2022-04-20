def main():
    # data load
    N, K = map(int, input().split())

    scores = []
    for _ in range(N):
        a, b = map(int, input().split())
        scores.append(a-b)
        scores.append(b)

    # greedyに取り出す
    print(sum(sorted(scores, reverse=True)[:K]))
    return


if __name__ == '__main__':
    main()

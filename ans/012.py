class UnionFind(object):
    def __init__(self, size):
        self.parent = [-1] * size

    def union(self, x, y):
        x, y = self.root(x), self.root(y)
        if x == y:
            return
        if self.parent[x] > self.parent[y]:
            x, y = y, x

        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return

    def root(self, x):
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)


def main():
    # data load / make instance ..
    H, W = map(int, input().split())
    uf = UnionFind(H*W)
    grid = [[0] * W for _ in range(H)]
    move = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    # query 処理
    Q = int(input())
    result = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        # 1 -> (h, w) をまわり4つで赤いものとunion
        if query[0] == 1:
            h, w = query[1:]
            h -= 1;w -= 1
            grid[h][w] = 1
            for dh, dw in move:
                sh, sw = h+dh, w+dw
                if 0 <= sh < H and 0 <= sw < W and grid[sh][sw]:
                    uf.union(h*W+w, sh*W+sw)
        # 2 -> same関数で同グループかを調べ, 結果をresultに格納
        else:
            h1, w1, h2, w2 = query[1:]
            h1 -= 1;w1 -= 1;h2 -= 1;w2 -= 1
            if uf.same(h1*W+w1, h2*W+w2) and grid[h1][w1]:
                result.append('Yes')
            else:
                result.append('No')

    # output
    print(*result, sep='\n')
    return


if __name__ == '__main__':
    main()

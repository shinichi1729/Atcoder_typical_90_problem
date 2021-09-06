from collections import defaultdict


X_SIZE, Y_SIZE = 1001, 1001


# いわゆるimos法というやり方でクエリをまとめて処理して線形時間で処理
def imos(array):
    for x in range(1, X_SIZE+1):
        for y in range(1, Y_SIZE+1):
            array[y][x] += array[y-1][x]
    for y in range(1, Y_SIZE+1):
        for x in range(1, X_SIZE+1):
            array[y][x] += array[y][x-1]

def main():
    # data load
    N = int(input())
    array = [[0]*(X_SIZE+1) for _ in range(Y_SIZE+1)]
    for _ in range(N):
        lx, ly, rx, ry = map(lambda x:int(x)+1, input().split())
        # 前処理パート(imos法)
        array[ly][lx] += 1
        array[ly][rx] -= 1
        array[ry][lx] -= 1
        array[ry][rx] += 1
    # arrayの整形
    imos(array)

    # 配列内を全探索してcounter[k]を数える
    counter = defaultdict(int)
    for x in range(1, X_SIZE+1):
        for y in range(1, Y_SIZE+1):
            counter[array[y][x]] += 1

    # output
    for k in range(1, N+1):
        print(counter[k])



if __name__ == '__main__':
    main()

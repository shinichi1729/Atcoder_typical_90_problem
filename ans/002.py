# bit全探索
def main():
    # data load
    N = int(input())
    parentheses = {'left': '(', 'right': ')'}

    # Exception handling
    if N % 2:
        return

    result = []
    for bit in range(2 ** N):
        string = ''
        amari = 0
        for i in range(N):
            # 1 が立ってるなら ( を右から挿入
            if (bit >> i) & 1:
                string += parentheses['left']
                amari += 1
            else:
                # ) の数が その時点の ( の数を上回ると満たさない
                if amari == 0:
                    break
                string += parentheses['right']
                amari -= 1
        if len(string) == N and not amari:
            result.append(string)

    # output
    result.sort()
    print(*result, sep='\n')
    return


if __name__ == '__main__':
    main()


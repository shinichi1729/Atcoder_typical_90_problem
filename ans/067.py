def eight_to_nine(number: str) -> str:
    number10 = 0
    for i, num in enumerate(reversed(number)):
        number10 += 8**i * int(num)
    number9 = ''
    while number10:
        number9 += str(number10 % 9)
        number10 //= 9
    return ''.join(reversed(number9))

def main():
    # data load
    N, K = input().split()
    K = int(K)

    # 8進数 -> 10進数 -> 9進数 -> 8を5に変換
    for _ in range(K):
        N = eight_to_nine(N)
        N = ''.join(num if num != '8' else '5' for num in N)

    # output
    if not N:
        print(0)
    else:
        print(N)
    return


if __name__ == '__main__':
    main()

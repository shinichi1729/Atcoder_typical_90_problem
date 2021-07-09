import math


def main():
    # data load
    A, B = map(int, input().split())

    # python の場合はオーバーフローを気にする必要はない.
    gcd = math.gcd(A, B)
    res = A*B // gcd if A*B//gcd <= 10**18 else "Large"

    # output
    print(res)
    return


if __name__ == '__main__':
    main()

def main():
    # data load
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # sum(A)+Kの偶奇は常に一定. => sum(B) % 2 == sum(A)+K % 2 .. ①
    # 各要素 a, bについて sum(|a-b|) <= K .. ②
    if sum(B) % 2 != (sum(A)+K) % 2:
        print("No")
    elif sum([abs(A[i]-B[i]) for i in range(N)]) > K:
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    main()

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    A, B, C = map(int, input().split())
    
    # A, B, C の最大公約数が立方体の最大の一辺の長さ
    g = gcd(gcd(A, B), C)
    
    # 切れ目は各辺の長さLに対して (L // g) - 1 個
    print((A+B+C) // g - 3)


if __name__ == '__main__':
    main()

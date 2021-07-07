# https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56
# o(√n)で返り値も整列された状態なので扱いやすい.
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def main():
    # data load
    K = int(input())

    divisors = make_divisors(K)

    result = 0
    for i, a in enumerate(divisors):
        for j in range(i, len(divisors)):
            b = divisors[j]
            c = K // (a*b)
            if a <= b <= c and a * b * c == K:
                result += 1

    # output
    print(result)
    return


if __name__ == '__main__':
    main()

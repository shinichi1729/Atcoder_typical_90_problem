from typing import List


def add_and_div(number, n, prime_list) -> int:
    prime_list.append(n)
    number //= n
    return number


def prime_factorize(number: int) -> List[int]:
    prime_list = []
    while number % 2 == 0:
        number = add_and_div(number, 2, prime_list)
    while number % 3 == 0:
        number = add_and_div(number, 3, prime_list)

    for num in range(5, int(number**0.5)+1, 6):
        while number % num == 0:
            number = add_and_div(number, num, prime_list)
        while number % (num+2) == 0:
            number = add_and_div(number, num+2, prime_list)

    if number != 1:
        prime_list.append(number)
    return prime_list


def main():
    # data load
    N = int(input())
    prime_list = prime_factorize(N)

    # 答えは2^(n-1) < len(prime_list) <= 2^n を満たすn
    # 偏りがなく分解していく方が魔法の適用範囲が広がる
    len_prime_list = len(prime_list)
    cnt = 0
    while len_prime_list != 1:
        len_prime_list = len_prime_list % 2 + len_prime_list // 2
        cnt += 1
    print(cnt)
    return


if __name__ == '__main__':
    main()

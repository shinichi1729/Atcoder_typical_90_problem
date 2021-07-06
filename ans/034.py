from collections import defaultdict

def main():
    # data load
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    type_cnt = 0
    type_data = defaultdict(int)

    # しゃくとり法
    left, right = 0, 0
    result = 0
    while right < N:
        type_data[A[right]] += 1
        if type_data[A[right]] == 1:
            type_cnt += 1
        while type_cnt == K + 1:
            type_data[A[left]] -= 1
            if type_data[A[left]] == 0:
                type_cnt -= 1
            left += 1
        result = max(result, right-left+1)
        right += 1
    
    # output
    print(result)


if __name__ == '__main__':
    main()

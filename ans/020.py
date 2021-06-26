def main():
    # data load
    a, b, c = map(int, input().split())

    # log2a < blog2c <=> a < c^b
    if a < c**b:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()

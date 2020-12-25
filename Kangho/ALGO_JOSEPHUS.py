def josepus():
    m = n
    idx = 0
    while m != 2:
        army.pop(idx)
        idx += k - 1
        m -= 1
        idx %= m


if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().split())
        army = [str(a) for a in range(1, n+1)]
        josepus()
        print(" ".join(army))

def josepus():
    m = n
    idx = k - 1
    answer = []
    while True:
        answer.append(army.pop(idx))
        idx += k - 1
        m -= 1
        if m == 0:
            break
        idx %= m
    return answer


if __name__ == '__main__':
    n, k = map(int, input().split())
    army = [str(a) for a in range(1, n+1)]
    print("<" + ", ".join(josepus()) + ">")

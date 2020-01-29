Range, number = map(int, input().split())
check = [False]*Range
a = []


def p(count):
    if count == number:
        print(" ".join(map(str, a)))
        return
    else:
        for i in range(Range):
            if not check[i]:
                a.append(i+1)
                p(count+1)
                a.pop()

p(0)
Range, number = map(int, input().split())
check = [False]*Range
a = []


def p(count):
    if count == number:
        print(" ".join(map(str, a)))
        return
    else:
        for i in range(Range):
            if a:
                if not check[i] and a[count-1] <= i+1:
                    a.append(i+1)
                    p(count+1)
                    a.pop()
            else:
                a.append(i+1)
                p(count+1)
                a.pop()
p(0)
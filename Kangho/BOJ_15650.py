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
                if a[count-1] < i+1 and not check[i]:
                    check[i] = True
                    a.append(i+1)
                    p(count+1)
                    a.pop()
                    check[i] = False
            else:
                a.append(i+1)
                check[0] = True
                p(count+1)
                a.pop()
                check[i] = False

p(0)
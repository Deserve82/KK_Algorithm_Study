Range, number = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
check = [False]*Range
answer = []

def p(count):
    if count == number:
        print(" ".join(map(str, answer)))
        return
    else:
        for i in range(Range):
            if not check[i]:
                check[i] = True
                answer.append(a[i])
                p(count+1)
                answer.pop()
                check[i] = False
p(0)
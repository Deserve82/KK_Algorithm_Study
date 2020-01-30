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
            if answer:
                if not check[i] and answer[count-1] <= a[i]:
                    answer.append(a[i])
                    p(count+1)
                    answer.pop()
                    check[i] = False
            else:
                answer.append(a[i])
                p(count+1)
                answer.pop()
                check[i] = False
p(0)
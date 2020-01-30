Range, number = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
answer = []

def p(count):
    if count == number:
        print(" ".join(map(str, answer)))
        return
    else:
        for i in range(Range):
            if answer:
                answer.append(a[i])
                p(count+1)
                answer.pop()
            else:
                answer.append(a[i])
                p(count+1)
                answer.pop()
p(0)
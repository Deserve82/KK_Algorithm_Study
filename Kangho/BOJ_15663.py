Range, number = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
check = [False]*Range
answer = []
answer_list = []


def p(count):
    if count == number:
        if " ".join(map(str, answer)) in answer_list:
            pass
        else:
            answer_list.append(" ".join(map(str, answer)))
            print(" ".join(map(str, answer)))
        return
    else:
        for i in range(Range):
            if answer:
                if not check[i]:
                    check[i] = True
                    answer.append(a[i])
                    p(count+1)
                    answer.pop()
                    check[i] = False
            else:
                check[i] = True
                answer.append(a[i])
                p(count+1)
                answer.pop()
                check[i] = False


p(0)
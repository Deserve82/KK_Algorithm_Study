n = int(input())
answer = []


def rec(idx, friends_list):
    global count
    if len(answer) == n:
        count += 1
        return
    else:
        for i in range(idx, m):
            if friends_list[i * 2] not in answer and friends_list[i * 2 + 1] not in answer:
                answer.extend([friends_list[i * 2], friends_list[i * 2 + 1]])
                rec(i, friends_list)
                answer.pop()
                answer.pop()
        return


for _ in range(n):
    count = 0
    n, m = map(int, input().split())
    friends_list = list(map(int, input().split()))
    rec(0, friends_list)
    print(count)

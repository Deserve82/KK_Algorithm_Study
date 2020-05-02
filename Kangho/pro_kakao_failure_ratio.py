def solution(N, stages):
    answer = []
    percent = [[i, 0] for i in range(1, N+1)]
    stages.sort()
    total_user = len(stages)
    for i in range(total_user):
        if stages[i] > N:
            pass
        else:
            percent[stages[i]-1][1] += 1
    ls = []
    for i in percent:
        if total_user == 0:
            ls.append((i[0], 0))
        else:
            ls.append((i[0], i[1]/total_user))
            total_user -= i[1]
    ls = sorted(ls, key=lambda x: x[1], reverse=True)
    for k in ls:
        answer.append(k[0])
    return answer

print(solution(4, [4, 4, 4, 4]))
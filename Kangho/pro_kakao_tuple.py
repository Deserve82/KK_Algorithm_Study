def solution(s):
    answer = []
    ss = s[1:-1]
    ans = []
    temp = []
    num = ''
    for s in ss:
        if s == '{':
            num = ''
        elif s == ',':
            if num != '':
                temp.append(int(num))
                num = ''
        elif s == '}':
            temp.append(int(num))
            ans.append(temp)
            num = ''
            temp = []
        else:
            num += s
    ans.sort(key=lambda x: len(x))
    pivot = set()
    for a in ans:
        answer.extend(list(set(a) - pivot))
        pivot = set(a)
    return answer

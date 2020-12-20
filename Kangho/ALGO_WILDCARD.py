def wildcard(wild_idx, com_idx):
    if cache[wild_idx][com_idx] != -1:
        return cache[wild_idx][com_idx]

    while wild_idx < len_ws and com_idx < len_s and (ws[wild_idx] == '?' or ws[wild_idx] == s[com_idx]):
        wild_idx += 1
        com_idx += 1

    if wild_idx == len_ws:
        cache[wild_idx][com_idx] = int(com_idx == len_s)
        return cache[wild_idx][com_idx]

    if ws[wild_idx] == '*':
        for i in range(com_idx, len_s+1):
            if wildcard(wild_idx+1, i):
                cache[wild_idx][com_idx] = 1
                return cache[wild_idx][com_idx]

    cache[wild_idx][com_idx] = 0
    return cache[wild_idx][com_idx]


answers = []
for _ in range(int(input())):
    ws = input()
    strs = []
    for _ in range(int(input())):
        strs.append(input())
    ans = []
    for s in strs:
        len_ws = len(ws)
        len_s = len(s)
        cache = [[-1]*(len_s+1) for _ in range(len_ws+1)]
        if wildcard(0, 0):
            ans.append(s)
        else:
            continue
    answers.extend(sorted(ans))
for a in answers:
    print(a)

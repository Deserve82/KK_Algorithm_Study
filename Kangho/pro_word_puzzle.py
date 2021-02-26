def solution(strs, t):
    lt = len(t)
    cache = [20000] * (lt+1)
    cache[0] = 0
    for i in range(lt):
        for str in strs:
            if str[0] == t[i]:
                val = i+len(str)
                if t[i:val] == str:
                    cache[val] = min(cache[i] + 1, cache[val])
    answer = cache[lt]
    if answer >= 20000:
        answer = -1
    return answer

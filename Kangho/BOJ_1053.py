from itertools import combinations


def swap_char(a, b, st):
    c = st[b]
    st = st[:b] + st[a] + st[b+1:]
    st = st[:a] + c + st[a+1:]
    return st


def factory(start_idx, end_idx, string):
    if start_idx >= end_idx:
        return 0

    if cache[start_idx][end_idx] != -1:
        return cache[start_idx][end_idx]

    ret = 1000000000
    if string[start_idx] == string[end_idx]:
        ret = min(ret, factory(start_idx+1, end_idx-1, string))

    ret = min(
        ret,
        factory(start_idx + 1, end_idx, string) + 1,
        factory(start_idx, end_idx - 1, string) + 1,
        factory(start_idx + 1, end_idx - 1, string) + 1
    )
    cache[start_idx][end_idx] = ret
    return ret


S = input()
s_len = len(S)
change_two = list(combinations([i for i in range(s_len)], 2))
answer = 1000000000
cache = [[-1]*51 for _ in range(51)]
answer = min(answer, factory(0, s_len-1, S))
for com in change_two:
    cache = [[-1] * 51 for _ in range(51)]
    s = swap_char(com[0], com[1], S)
    answer = min(answer, factory(0, s_len-1, s) + 1)
print(answer)

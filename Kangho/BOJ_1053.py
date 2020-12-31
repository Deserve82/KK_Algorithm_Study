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

    while start_idx < end_idx:
        if string[start_idx] == string[end_idx]:
            start_idx += 1
            end_idx -= 1
        else:
            break

    if start_idx >= end_idx:
        return 0

    ret = 1000000000
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


# 전에 오답처리 되었던 점화식, 당연히 first가 고정되어있기 떄문에 오답이 나오겠다는 생각이 들었다. - dp를 위한 맞춤 풀이 
#     ret = min(
#         ret,
#         factory(start_idx, end_idx, string[:end_idx] + string[start_idx] + string[end_idx + 1:]) + 1,
#         factory(start_idx, end_idx + 1, string[:end_idx+1] + string[start_idx] + string[end_idx+1:]) + 1,
#         factory(start_idx, end_idx - 1, string[:end_idx] + string[end_idx+1:]) + 1,
#     )


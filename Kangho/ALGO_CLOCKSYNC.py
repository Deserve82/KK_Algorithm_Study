buttons = [
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]
]


def push(button_idx):
    for bi, p in enumerate(buttons[button_idx]):
        if p == 1:
            curr_clock[bi] += 3


def check_all12():
    for t in curr_clock:
        if t % 12 != 0:
            return False
    return True

# 종만북 풀이
def clock(idx):
    if check_all12():
        return 0

    if idx > 9:
        return float('inf')
    ret = float('inf')
    for c in range(4):
        ret = min(ret, c + clock(idx + 1))
        push(idx)
    return ret


n = int(input())
for _ in range(n):
    curr_clock = list(map(int, input().split()))
    ans = clock(0)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)


# 내 풀이
# def clock(idx):
#     global pushed_number, cnt
#     if check_all12():
#         answer.append(pushed_number)
#         return
# 
#     if idx > 9:
#         return
# 
#     for c in range(4):
#         push(idx, False, c)
#         pushed_number += c
#         clock(idx+1)
#         push(idx, True, c)
#         pushed_number -= c

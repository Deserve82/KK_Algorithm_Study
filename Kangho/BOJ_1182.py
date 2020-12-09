n, goal = map(int, input().split())
nums = list(map(int, input().split()))
c = [False] * n
gs = 0
cnt = 0


def check(start):
    global gs, cnt
    if gs == goal:
        cnt += 1
    for i in range(start, n):
        if not c[i]:
            c[i] = True
            gs += nums[i]
            check(i)
            c[i] = False
            gs -= nums[i]


check(0)
if goal == 0:
    cnt -= 1
print(cnt)

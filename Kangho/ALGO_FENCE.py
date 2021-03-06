def dq(left, right):
    if left == right:
        return sticks[left]

    mid = (left + right) // 2
    ret = max(dq(left, mid), dq(mid+1, right))

    lo, hi = mid, mid+1
    height = min(sticks[lo], sticks[hi])
    ret = max(ret, height * 2)

    while left < lo or hi < right:
        if hi < right and (left == lo or sticks[lo-1] < sticks[hi+1]):
            hi += 1
            height = min(height, sticks[hi])
        else:
            lo -= 1
            height = min(height, sticks[lo])
        ret = max(ret, (hi-lo+1) * height)
    return ret


for _ in range(int(input())):
    n = int(input())
    sticks = list(map(int, input().split()))
    print(dq(0, n-1))

    
# swiping algorithm을 사용한 방법 시간 복잡도는 O(n)
def solve_stack():
    remaining = []
    h.append(0)
    ret = 0
    for i in range(len(h)):
        while remaining and h[remaining[-1]] >= h[i]:
            j = remaining.pop()
            if not remaining:
                width = i
            else:
                width = (i - remaining[-1] - 1)
            ret = max(ret, h[j] * width)
        remaining.append(i)
    return ret


for _ in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    print(solve_stack())

import sys


def fence(left, right):
    if left == right:
        return sticks[left]

    mid = (left + right) // 2
    ret = max(fence(left, mid), fence(mid+1, right))

    lo, hi = mid, mid + 1
    height = min(sticks[lo], sticks[hi])
    ret = max(ret, height * 2)

    while left < lo or hi < right:

        if hi < right and (left == lo or sticks[lo-1] < sticks[hi+1]):
            hi += 1
            height = min(sticks[hi], height)
        else:
            lo -= 1
            height = min(sticks[lo], height)

        ret = max(ret, (hi - lo + 1) * height)

    return ret


n = int(sys.stdin.readline())
sticks = []
for _ in range(n):
    sticks.append(int(sys.stdin.readline()))
print(fence(0, n-1))

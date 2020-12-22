def min_error(lo, hi):
    if lo == 0:
        sum = pSum[hi]
        sqSum = pSqSum[hi]
    else:
        sum = pSum[hi] - pSum[lo-1]
        sqSum = pSqSum[hi] - pSqSum[lo-1]

    m = int(float(sum) / (hi - lo + 1) + 0.5)
    ret = sqSum - 2 * m * sum + m * m * (hi - lo + 1)
    return ret


def quantize(f, p):
    if f == num:
        return 0
    if p == 0:
        return 1000000000
    if cache[f][p-1] != -1:
        return cache[f][p-1]

    ret = cache[f][p-1] = 1000000000
    for i in range(f, num):
        ret = min(ret, min_error(f, i) + quantize(i+1, p-1))
        cache[f][p-1] = ret
    return ret


for _ in range(int(input())):
    num, pick_num = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    pSum = [0]*101
    pSqSum = [0]*101
    pSum[0] = A[0]
    pSqSum[0] = A[0]*A[0]
    for i in range(1, num):
        pSum[i] = pSum[i-1] + A[i]
        pSqSum[i] = pSqSum[i-1] + A[i] * A[i]
    cache = [[-1]*10 for _ in range(num + 1)]
    print(quantize(0, pick_num))

# 풀이는 종만북 출처..

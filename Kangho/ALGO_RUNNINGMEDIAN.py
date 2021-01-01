import sys
import heapq
MOD = 20090711


for _ in range(int(input())):
    N, a, b = map(int, sys.stdin.readline().split())
    max_hq = []
    min_hq = []
    value = 1983
    sum_val = 0
    for i in range(N):
        if len(max_hq) == len(min_hq):
            heapq.heappush(max_hq, -value)
        else:
            heapq.heappush(min_hq, value)

        if i == 0:
            sum_val += -max_hq[0]
            value = (value * a + b) % MOD
            continue

        if -max_hq[0] > min_hq[0]:
            max_v = -heapq.heappop(max_hq)
            min_v = heapq.heappop(min_hq)
            heapq.heappush(min_hq, max_v)
            heapq.heappush(max_hq, -min_v)

        sum_val += -max_hq[0]
        sum_val %= MOD
        value = (value * a + b) % MOD
    print(sum_val % MOD)

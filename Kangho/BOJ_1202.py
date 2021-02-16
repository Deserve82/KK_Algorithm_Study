import sys
import heapq as hq
input = sys.stdin.readline
N, K = map(int, input().split())
jewels = []
for _ in range(N):
    weight, cost = map(int, input().split())
    hq.heappush(jewels, (weight, cost))
bags = []
for _ in range(K):
    bags.append(int(input()))
bags.sort()
total_cost = 0
heap = []
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        hq.heappush(heap, -hq.heappop(jewels)[1])
    if heap:
        total_cost -= hq.heappop(heap)
print(total_cost)

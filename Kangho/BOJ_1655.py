import sys
import heapq
N = int(input())
first_max = []
second_min = []
for _ in range(N):
    a = int(sys.stdin.readline())
    if len(first_max) == len(second_min):
        heapq.heappush(first_max, -a)
    else:
        heapq.heappush(second_min, a)
    if first_max and second_min:
        if -first_max[0] > second_min[0]:
            fm = heapq.heappop(first_max)
            sm = heapq.heappop(second_min)
            heapq.heappush(second_min, -fm)
            heapq.heappush(first_max, -sm)
    print(-first_max[0])

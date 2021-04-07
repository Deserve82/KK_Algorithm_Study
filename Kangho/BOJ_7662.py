import heapq as hq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    max_pq = []
    min_pq = []
    idx = 0
    is_valid = [True] * N
    for _ in range(N):
        c, num = input().split()
        num = int(num)
        if c == 'I':
            hq.heappush(max_pq, (-num, idx))
            hq.heappush(min_pq, (num, idx))
            idx += 1
        else:
            if num == -1:
                while min_pq and not is_valid[min_pq[0][1]]:
                    hq.heappop(min_pq)
                if min_pq:
                    _, index = hq.heappop(min_pq)
                    is_valid[index] = False
            elif num == 1:
                while max_pq and not is_valid[max_pq[0][1]]:
                    hq.heappop(max_pq)
                if max_pq:
                    _, index = hq.heappop(max_pq)
                    is_valid[index] = False
    while max_pq:
        if is_valid[max_pq[0][1]]:
            break
        else:
            hq.heappop(max_pq)
    while min_pq:
        if is_valid[min_pq[0][1]]:
            break
        else:
            hq.heappop(min_pq)
    answers = set()
    if max_pq:
        a = hq.heappop(max_pq)
        answers.add(-a[0])
    if min_pq:
        answers.add(hq.heappop(min_pq)[0])
    if answers:
        print(max(answers), min(answers))
    else:
        print("EMPTY")

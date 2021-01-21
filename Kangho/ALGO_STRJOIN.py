import heapq as hq
for _ in range(int(input())):
    N = int(input())
    pq = []
    numbers = list(map(int, input().split()))
    for number in numbers:
        hq.heappush(pq, number)
    answer = 0
    while True:
        min_val1 = hq.heappop(pq)
        min_val2 = hq.heappop(pq)
        answer += min_val1 + min_val2
        if len(pq) == 0:
            break
        hq.heappush(pq, min_val1+min_val2)
    print(answer)

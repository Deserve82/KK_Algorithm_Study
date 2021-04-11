import heapq as hq
def solution(n, works):
    answer = 0
    pq = []
    for w in works:
        hq.heappush(pq, -w)
    
    while n:
        max_val = hq.heappop(pq)
        if max_val == 0:
            break
        else:
            hq.heappush(pq, max_val+1)
            n -= 1
    for i in pq:
        answer += i * i
    return answer

def solution(stones, k):
    left, right = 0, max(stones) * 2
    while left < right:
        mid = (left + right) // 2
        cnt = 0
        mv = 0
        for stone in stones:
            if stone - mid <= 0:
                cnt += 1
            else:
                mv = max(mv, cnt)
                cnt = 0
        mv = max(mv, cnt)

        if mv >= k:
            right = mid
        else:
            left = mid + 1
    answer = right
    return answer

def solution(stones, k):
    answer = 0
    left = 0
    right = k*stones[0] + 10000
    while left < right:
        mid = (left + right) // 2
        mx_kk = 0
        str_falling = 0
        for stone in stones:
            stone -= mid
            if stone > 0:
                str_falling = 0
            else:
                str_falling += 1
                mx_kk = max(mx_kk, str_falling)
        
        if mx_kk < k:
            left = mid + 1
        else:
            right = mid
    answer = right
    return answer

def solution(distance, rocks, n):
    answer = 0
    left, right = 0, distance + 1
    rocks.sort()
    rocks.append(distance)
    while left <= right:
        mid = (left + right) // 2
        curr = 0
        mid_dis = float('inf')
        cnt = 0

        for rock in rocks:
            diff = rock - curr
            if diff < mid:
                cnt += 1
            else:
                curr = rock
                mid_dis = min(mid_dis, diff)

        if cnt > n:
            right = mid - 1
        else:
            answer = mid_dis
            left = mid + 1
    return answer

def solution(cookie):
    lc = len(cookie)
    mv = 0
    for m in range(lc-1):
        left = m
        right = m + 1
        first_total = cookie[left]
        second_total = cookie[right]
        while left >= 0 and right <= lc - 1:
            if first_total < second_total:
                left -= 1
                if left < 0:
                    break
                first_total += cookie[left]
            if second_total < first_total:
                right += 1
                if right > lc - 1:
                    break
                second_total += cookie[right]
            if first_total == second_total:
                mv = max(first_total, mv)
                left -= 1
                right += 1
                if left < 0 or right > lc - 1:
                    break
                first_total += cookie[left]
                second_total += cookie[right]
    return mv


print(solution([1, 1, 1, 99, 1, 99]))
print(solution([1, 1, 1, 1, 1, 1]))
print(solution([1, 1, 1, 1, 1, 1, 1, 1]))
print(solution([1, 1, 2, 5]))
print(solution([1, 2, 4, 5]))

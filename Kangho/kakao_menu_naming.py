from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        pivot = []
        for order in orders:
            order = "".join(sorted(list(order)))
            pivot.extend(list(combinations(order, c)))
        count_val = Counter(pivot)
        if count_val:
            mv = max(count_val.values())
            for key, val in count_val.items():
                if val == mv and val > 1:
                    answer.append("".join(key))
    answer.sort()
    return answer


order = ["XYZ", "XWY", "WXA"]
c = [2, 3, 4]

solution(order, c)

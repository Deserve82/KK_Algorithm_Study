import math


def solution(n, stations, w):
    answer = 0
    start = 0
    broad_band = 2 * w + 1
    for station in stations:
        end = station - w - 1
        answer += math.ceil((end - start) / broad_band)
        start = station + w
    if start <= n:
        answer += math.ceil((n - (start)) / broad_band)
    return answer

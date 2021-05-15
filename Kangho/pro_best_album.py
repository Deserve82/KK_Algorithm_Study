import heapq as hq


def solution(genres, plays):
    answer = []
    g_point = {}
    g_idxes = {}
    lg = len(genres)
    for i in range(lg):
        if genres[i] not in g_point:
            g_point[genres[i]] = plays[i]
        else:
            g_point[genres[i]] += plays[i]
        if genres[i] not in g_idxes:
            g_idxes[genres[i]] = []
        hq.heappush(g_idxes[genres[i]], (-plays[i], i))

    pq = []
    for k, v in g_point.items():
        hq.heappush(pq, (-v, k))

    while pq:
        _, curr_max = hq.heappop(pq)
        if len(g_idxes[curr_max]) > 1:
            one, two = hq.heappop(g_idxes[curr_max]), hq.heappop(g_idxes[curr_max])
            answer.extend([one[1], two[1]])
        else:
            one = hq.heappop(g_idxes[curr_max])
            answer.append(one[1])
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

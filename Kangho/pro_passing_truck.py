from collections import deque


def solution(bridge_length, weight, truck_weights):
    q = deque()
    last = len(truck_weights)
    truck_idx = 0
    total_weight = 0
    time = 0
    while truck_idx < last or q:
        time += 1
        if q:
            if q[0][1] == time:
                total_weight -= q.popleft()[0]
        if truck_idx < last:
            if total_weight + truck_weights[truck_idx] <= weight:
                q.append((truck_weights[truck_idx], time + bridge_length))
                total_weight += truck_weights[truck_idx]
                truck_idx += 1
    answer = time
    return answer

def search(pivot, compare, idx, n):
    right_min_idx, right_dis = n, [n, n]
    left_min_idx, left_dis = n, [n, n]
    if pivot[idx] != compare[idx]:
        return idx, 0
    else:
        for i in range(1, (n//2)+1):
            ri = (i + idx) % n
            if pivot[ri] != compare[ri]:
                right_dis[0] = min(right_dis[0], i)
                right_dis[1] = i
                if right_min_idx == n:
                    right_min_idx = ri
            li = (n-i + idx) % n
            if pivot[li] != compare[li]:
                left_dis[0] = min(left_dis[0], i)
                left_dis[1] = i
                if left_min_idx == n:
                    left_min_idx = li

        if left_dis[0] == right_dis[0]:
            if right_dis[1] > left_dis[1]:
                return left_min_idx, left_dis[0]
            else:
                return right_min_idx, right_dis[0]
        elif left_dis[0] > right_dis[0]:
            return right_min_idx, right_dis[0]
        else:
            return left_min_idx, left_dis[0]


def solution(name):
    answer = 0
    n = len(name)
    curr_idx = 0
    points_board = {}
    forward = "ABCDEFGHIJKLMN"
    backward = "OPQRSTUVWXYZ"
    backward = backward[::-1]
    for point, a in enumerate(forward):
        points_board[a] = point
    for point, a in enumerate(backward):
        points_board[a] = point + 1
    curr_state = ["A"] * n
    name = list(name)
    while "".join(name) != "".join(curr_state):
        next_idx, dis = search(name, curr_state, curr_idx, n)
        answer += dis
        answer += points_board[name[next_idx]]
        curr_state[next_idx] = name[next_idx]
        curr_idx = next_idx
    return answer

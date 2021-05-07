from copy import deepcopy
check = []
bad_ids = []
curr_state = set()
answer = 0


def get_bad_users(user_ids, banned_id):
    results = []
    for user_id in user_ids:
        is_bad = True
        if len(user_id) != len(banned_id):
            continue
        else:
            for a, b in zip(user_id, banned_id):
                if b == '*' or a == b:
                    continue
                else:
                    is_bad = False
                    break
        if is_bad:
            results.append(user_id)
    return results


def get_combis(bad_idx, pivot):
    global curr_state, answer
    if bad_idx == pivot:
        if curr_state not in check:
            check.append(deepcopy(curr_state))
            answer += 1
        return

    for i in range(len(bad_ids[bad_idx])):
        if bad_ids[bad_idx][i] not in curr_state:
            curr_state.add(bad_ids[bad_idx][i])
            get_combis(bad_idx + 1, pivot)
            curr_state.remove(bad_ids[bad_idx][i])


def solution(user_id, banned_id):
    for bid in banned_id:
        bad_ids.append(get_bad_users(user_id, bid))
    get_combis(0, len(banned_id))
    return answer

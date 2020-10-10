def solution(k, score):
    answer = len(score)
    score_board = {}
    idx_count = {}
    prev_score = score[0]
    for i, s in enumerate(score):
        if i == 0:
            continue
        else:
            deduct_val = str(prev_score - s)
            if score_board.get(deduct_val):
                score_board[deduct_val].add(i-1)
                score_board[deduct_val].add(i)
                idx_count[deduct_val] += 1
            else:
                score_board[deduct_val] = {i-1, i}
                idx_count[deduct_val] = 1
            prev_score = s
    total_idx = []
    for score, val in idx_count.items():
        if val >= k:
            total_idx.extend(score_board[score])
    adjusted_scores = len(set(total_idx))
    if adjusted_scores == 0:
        answer = 0
    else:
        answer -= adjusted_scores
    return answer



print(solution(3, [24,22,20,10,5,3,2,1]))

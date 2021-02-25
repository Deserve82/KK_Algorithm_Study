from itertools import permutations

N = int(input())
innings = []
for _ in range(N):
    players = list(map(int, input().split()))
    innings.append(players)
pp = [1, 2, 3, 4, 5, 6, 7, 8]
candis = set((permutations(pp)))
answer = 0
for can in candis:
    candi = [*can[:3], 0, *can[3:]]
    tmp_ans = 0
    player_idx = 0
    for inning in innings:
        fb, sb, tb = 0, 0, 0
        out_cnt = 0
        while out_cnt < 3:
            if inning[candi[player_idx]] == 0:
                out_cnt += 1
            elif inning[candi[player_idx]] == 1:
                tmp_ans += tb
                fb, sb, tb = 1, fb, sb
            elif inning[candi[player_idx]] == 2:
                tmp_ans += (tb+sb)
                fb, sb, tb = 0, 1, fb
            elif inning[candi[player_idx]] == 3:
                tmp_ans += (tb+sb+fb)
                fb, sb, tb = 0, 0, 1
            else:
                tmp_ans += (tb+sb+fb+1)
                fb, sb, tb = 0, 0, 0
            player_idx += 1
            player_idx %= 9
    answer = max(answer, tmp_ans)
print(answer)

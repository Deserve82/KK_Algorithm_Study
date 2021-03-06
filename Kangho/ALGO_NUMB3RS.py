import sys


def catch_me_if_you_can(loc, day):
    if day == 0:
        if loc == pri_vil:
            return 1
        return 0

    if cache[loc][day] > -0.5:
        return cache[loc][day]

    cache[loc][day] = 0.0
    for i in range(vils):
        if board[loc][i] == 1:
            cache[loc][day] += (catch_me_if_you_can(i, day - 1) / connected_to_vil[i])
    return cache[loc][day]


if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        vils, days, pri_vil = map(int, sys.stdin.readline().split())
        board = []
        for _ in range(vils):
            board.append(list(map(int, sys.stdin.readline().split())))

        connected_to_vil = [1] * vils
        for k in range(vils):
            cnt = 0
            for j in range(vils):
                if board[k][j] == 1:
                    cnt += 1
            connected_to_vil[k] = cnt
        pos_vil = int(input())
        possible_villages = list(map(int, sys.stdin.readline().split()))
        answer = ''
        cache = [[-1.0] * 101 for _ in range(51)]
        for q in possible_villages:
            answer += str(round((catch_me_if_you_can(q, days)), 8)) + " "
        print(answer)
